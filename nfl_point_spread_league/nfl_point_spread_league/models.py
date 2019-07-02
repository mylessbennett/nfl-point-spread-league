from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=255)
    division = models.CharField(max_length=255)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    ties = models.IntegerField(default=0)

    def __str__(self):
        return self.city + ' ' + self.name


