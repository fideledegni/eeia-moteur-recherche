from django.core.management.base import BaseCommand
from moteur.models import Article, Search
from pathlib import Path
from time import time
import json

# USAGE
# python manage.py seed --mode=(refresh | clear)

MODE_REFRESH = 'refresh' # Clear all data and creates addresses
MODE_CLEAR   = 'clear'   # Clear all data and do not create any object


class Command(BaseCommand):
  help = "Seed database for testing and development."

  def add_arguments(self, parser):
    parser.add_argument('--mode', type=str, help="Mode")

  def handle(self, *args, **options):
    self.stdout.write('Seeding data...')
    start = time()
    run_seed(options['mode'])
    end = time()
    self.stdout.write(f'Done in {end-start:.2f}s.')

# Open dummy data
MOTEUR_DIR = Path(__file__).resolve().parent.parent.parent

file_path = MOTEUR_DIR / "data/articles.json"

with file_path.open(encoding="utf8") as file:
  articles = json.load(file)


def clear_data():
  Search.objects.all().delete()
  Article.objects.all().delete()


def dump_data():
  for article in articles:
    new_article = Article(name=article['name'], image_name=article['image_name'], description=article['description'])
    new_article.save()

def run_seed(mode):
  """Seed database based on mode

  Args:
    mode (str): refresh / clear
  """
  clear_data()
  if mode == MODE_CLEAR:
    return
  dump_data()
