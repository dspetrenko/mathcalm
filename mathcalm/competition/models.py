from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Competition(models.Model):

    organizer = models.ForeignKey(to=User, on_delete=models.CASCADE)

    title = models.CharField(max_length=250)
    description = models.TextField()

    start = models.DateTimeField()
    end = models.DateTimeField()


class Event(models.Model):

    title = models.CharField(max_length=250)
    description = models.TextField()

    start = models.DateTimeField()
    end = models.DateTimeField()

    competition = models.ForeignKey(to=Competition, on_delete=models.CASCADE)
