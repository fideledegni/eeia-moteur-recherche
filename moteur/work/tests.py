import unittest
from models.default import default_model
from test_data.data import TEST_CASES, articles_list, searches_list


class TestDefaultModel(unittest.TestCase):

  def test_default_model(self):
    for text, expected in TEST_CASES.items():
      self.assertEqual(
        default_model(text, articles_list, searches_list),
        expected
      )

if __name__ == '__main__':
  unittest.main()
