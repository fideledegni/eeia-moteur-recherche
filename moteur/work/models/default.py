from unidecode import unidecode

def remove_accent(string):
  string = string.lower()
  return unidecode(string)


def default_model(text, articles_list, searches_list):
  text = remove_accent(text)

  def ranker(article):
    found = text in remove_accent(article['name'])
    return found
  # shuffle(articles_list)
  # return sorted(articles_list, key=ranker, reverse=True)

  return list(filter(ranker, articles_list))
