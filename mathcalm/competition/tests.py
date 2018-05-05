from django.test import TestCase

from .models import Competition
from .models import Event

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


class EventTestCase(TestCase):
    @staticmethod
    def get_competition():
        import datetime

        competition = Competition()
        competition.title = 'Math talent competition'
        competition.text = "It's best competition for young brains. " \
                           "Best community. Hard tasks."

        competition.start = datetime.datetime.now()
        duration = 1
        competition.end = competition.start + datetime.timedelta(days=duration)

        competition.save()
        return competition

    def test_creation(self):

        import datetime

        event = Event()
        event.competition = EventTestCase.get_competition()
        event.title = 'First step'
        event.description = 'First time you should solve few simple tests.'

        event.start = datetime.datetime.now()
        duration = 1
        event.end = event.start + datetime.timedelta(days=duration)

        event.save()
