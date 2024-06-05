from django.core.management.base import BaseCommand
from books.models import Book

class Command(BaseCommand):
    help = 'Clean and update the price field of existing books'

    def handle(self, *args, **options):
        books = Book.objects.all()
        for book in books:
            try:
                clean_price = book.price.replace(' TL', '').replace(',', '.')
                book.price = clean_price
                book.save()
                self.stdout.write(self.style.SUCCESS(f"Successfully updated price for book '{book.title}'"))
            except Exception as e:
                self.stderr.write(f"Error updating price for book '{book.title}': {e}")

        self.stdout.write(self.style.SUCCESS('Successfully cleaned and updated all book prices'))
