from django.db import models

# Create your models here.


class Competition(models.Model):

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
