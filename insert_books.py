# import_books.py
import csv
from datetime import datetime
from game.models import Book  # Replace 'myapp' with your actual app name

# Configurar la variable de entorno DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app_educativa.settings")

# Configurar Django
django.setup()

def import_books(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Book.objects.create(
                title=row['title'],
                author=row['author'],
                published_date=datetime.strptime(row['published_date'], '%Y-%m-%d').date(),
                price=row['price']
            )

if __name__ == '__main__':
    csv_file_path = 'books.csv'  # Replace with your actual file path
    import_books(csv_file_path)