from django.test import TestCase
# import datetime
# from django.utils import timezone
# from .models import Search, Article

# Create your tests here.

class QuestionModelTests(TestCase):

  def test_was_published_recently_with_future_question(self):
    """
    A dummy test
    """
    # time = timezone.now() + datetime.timedelta(days=30)
    # future_search = Search(search_date=time)
    # self.assertIs(future_search.was_searched_recently(), False)
    self.assertEqual(len([1, 2, 3]), 3)
