from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.username}"

class Division(models.Model):
    name = models.CharField(max_length=254)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
