import csv
import os
from django.core.management.base import BaseCommand
from books.models import Book
from django.db.utils import IntegrityError

class Command(BaseCommand):
    help = 'Import books from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        # Dosya adından türü çıkar
        genre = os.path.splitext(os.path.basename(csv_file_path))[0]

        try:
            with open(csv_file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Başlık satırını atla

                for row in reader:
                    try:
                        # Price alanındaki virgül ve TL ibaresini kaldırarak kaydet
                        price = row[5].replace(' TL', '').replace(',', '.')
                        book = Book(
                            title=row[2],
                            author=row[3],
                            price=price,
                            summary=row[7],
                            genre=genre  # Dosya adından alınan tür
                        )
                        book.save()
                    except IntegrityError as e:
                        self.stderr.write(f"Error saving book '{row[2]}': {e}")
                    except IndexError as e:
                        self.stderr.write(f"Error processing row: {row} - {e}")

            self.stdout.write(self.style.SUCCESS('Successfully imported books'))

        except FileNotFoundError as e:
            self.stderr.write(f"Error: {e}")
        except Exception as e:
            self.stderr.write(f"Unexpected error: {e}")
