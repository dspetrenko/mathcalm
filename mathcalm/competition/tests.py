from django.test import TestCase

from .models import Competition

# Create your tests here.


class CompetitionTestCase(TestCase):

    def test_creation(self):

        import datetime

        competition = Competition()
        competition.title = 'Math talent competition'
        competition.text = "It's best competition for young brains. " \
                           "Best community. Hard tasks."

        competition.start = datetime.datetime.now()
        duration = 1
        competition.end = competition.start + datetime.timedelta(days=duration)

        competition.save()
