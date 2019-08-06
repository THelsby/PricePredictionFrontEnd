import datetime
from django.db import models
from django.utils import timezone


class HouseInput(models.Model):
    test = models.CharField(max_length=200)
    testDate = models.DateTimeField('date published')

    def __str__(self):
        return self.test

    def was_published_recently(self):
        return self.testDate >= timezone.now() - datetime.timedelta(days=1)
