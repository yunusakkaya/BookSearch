# BookSearch

BookSearch is an application where users can search for books, like them, and receive new recommendations based on the books they liked. It is developed using Django and React.

## Features

- **Book Search:** Users can search for books by title, author, price range, and genre.
- **Like Books:** Users can mark books they like.
- **Recommendations:** Users receive new book recommendations on the same page based on the books they liked.

## Installation

### Requirements

- Python 3.8+
- Node.js 12+

### Steps

#### Backend Setup

1. Create and activate a Python virtual environment in the project directory:
   ```bash
   python -m venv env
   source env/bin/activate  # MacOS/Linux
   .\env\Scripts\activate  # Windows

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py import_books path/to/your/csvfile.csv

cd booksearch-frontend

npm install

npm start


















