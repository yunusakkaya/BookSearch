from django.db import models
from django.contrib.auth.models import User
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.CharField(max_length=20)  # String olarak bırakıldı
    summary = models.TextField(blank=True, null=True)
    genre = models.CharField(max_length=100, default="Roman")  # Varsayılan değer olarak "Roman" eklendi
    tfidf_vector = models.BinaryField(blank=True, null=True)  # TF-IDF vektörü için alan

    def save(self, *args, **kwargs):
        if self.summary:
            summaries = Book.objects.values_list('summary', flat=True)
            summaries = list(summaries) + [self.summary]
            vectorizer = TfidfVectorizer()
            tfidf_matrix = vectorizer.fit_transform(summaries)

            self.tfidf_vector = pickle.dumps(tfidf_matrix[-1])
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_price_as_float(self):
        # TL ve virgülleri kaldırarak fiyatı float olarak döndür
        return float(self.price.replace(' TL', '').replace(',', '.'))

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    liked_books = models.ManyToManyField(Book)

    def __str__(self):
        return self.user.username
