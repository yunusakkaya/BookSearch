from django.db.models import Q
from rest_framework import generics, views
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from .utils import normalize_text

class BookList(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        query = self.request.query_params.get('q')
        if query:
            query = normalize_text(query)
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(author__icontains=query) | Q(price__icontains=query) | Q(genre__icontains=query)
            )
        return queryset

class SearchBooks(views.APIView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '').strip()
        author = request.GET.get('author', '').strip()
        min_price = request.GET.get('min_price', '').strip()
        max_price = request.GET.get('max_price', '').strip()
        genre_query = request.GET.get('genre', '').strip()

        filters = Q()
        if query:
            query = normalize_text(query)
            filters &= Q(title__icontains=query) | Q(summary__icontains=query)
        if author:
            filters &= Q(author__icontains=author)

        books = Book.objects.filter(filters)

        if min_price:
            books = [book for book in books if book.get_price_as_float() >= float(min_price)]
        if max_price:
            books = [book for book in books if book.get_price_as_float() <= float(max_price)]

        if genre_query:
            genre_query = normalize_text(genre_query)
            genres = [normalize_text(book.genre) for book in books if book.genre]
            if genres:
                vectorizer = TfidfVectorizer()
                vectorizer.fit(genres)
                genre_vec = vectorizer.transform([genre_query])
                genre_similarities = []
                for book in books:
                    book_genre_vec = vectorizer.transform([normalize_text(book.genre)])
                    sim_score = cosine_similarity(genre_vec, book_genre_vec)
                    genre_similarities.append((book, sim_score[0][0]))
                books = [book[0] for book in sorted(genre_similarities, key=lambda x: x[1], reverse=True) if book[1] > 0.1]

        if not books:
            return Response({"error": "No books found matching the criteria"}, status=404)

        summaries = [book.summary for book in books if book.summary]
        if not summaries:
            return Response({"error": "No summaries available for books"}, status=404)

        vectorizer = TfidfVectorizer()
        vectorizer.fit(summaries)
        query_vec = vectorizer.transform([query])

        similarities = []
        for book in books:
            if book.tfidf_vector:
                book_vec = pickle.loads(book.tfidf_vector)
                book_vec_transformed = vectorizer.transform([book.summary])
                sim_score = cosine_similarity(query_vec, book_vec_transformed)
                similarities.append((book, sim_score[0][0]))

        sorted_books = sorted(similarities, key=lambda x: x[1], reverse=True)
        result = [{'id': book[0].id, 'title': book[0].title, 'author': book[0].author, 'price': book[0].price, 'summary': book[0].summary, 'genre': book[0].genre, 'score': book[1]} for book in sorted_books]
        return Response(result)

class RecommendBooksView(views.APIView):
    def post(self, request, *args, **kwargs):
        book_ids = request.data.get('book_ids', [])
        selected_books = Book.objects.filter(id__in=book_ids)

        if not selected_books:
            return Response({"error": "No selected books found"}, status=404)

        selected_summaries = [book.summary for book in selected_books if book.summary]
        if not selected_summaries:
            return Response({"error": "No summaries available for selected books"}, status=404)

        vectorizer = TfidfVectorizer()
        vectorizer.fit(selected_summaries)
        selected_vecs = vectorizer.transform(selected_summaries)

        all_books = Book.objects.exclude(id__in=book_ids)
        all_summaries = [book.summary for book in all_books if book.summary]

        if not all_summaries:
            return Response({"error": "No summaries available for all books"}, status=404)

        all_vecs = vectorizer.transform(all_summaries)

        similarities = cosine_similarity(selected_vecs, all_vecs)
        avg_similarities = similarities.mean(axis=0)
        sorted_indices = avg_similarities.argsort()[::-1]

        recommended_books = [all_books[int(i)] for i in sorted_indices[:10]]

        result = [{'id': book.id, 'title': book.title, 'author': book.author, 'price': book.price, 'summary': book.summary, 'genre': book.genre} for book in recommended_books]
        return Response(result)
