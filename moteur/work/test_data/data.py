from pathlib import Path
import json
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
cases_path = BASE_DIR / "test_cases.json"
articles_path = BASE_DIR / "liste_des_articles.csv"
searches_path = BASE_DIR / "liste_des_recherches.csv"

articles_df = pd.read_csv(articles_path)
searches_df = pd.read_csv(searches_path)
articles_df.fillna("", inplace=True)
searches_df.fillna("", inplace=True)

def get_elem_from_serie(line, titles):
  res = {}
  for key in titles: res[key] = line[key] if key != "image_name" else ""
  return res

article_titles = ["description", "image_name", "name"]
searches_titles = ["id", "search_text", "search_date", "clicked_article_1", "clicked_article_2", "clicked_article_3"]



articles_list = [get_elem_from_serie(line, article_titles) for (_, line) in articles_df.iterrows()]

searches_list = [get_elem_from_serie(line, searches_titles) for (_, line) in searches_df.iterrows()]

with cases_path.open(encoding="utf8") as file:
  TEST_CASES = json.load(file)
