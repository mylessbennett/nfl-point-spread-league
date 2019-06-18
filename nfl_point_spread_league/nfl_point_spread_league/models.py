from django.db import models
from django.contrib.auth.models import User

# class Division(models.Model):
#     name = models.CharField(max_length=254)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

# class Team(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     name = models.CharField(max_length=254)
#     division = models.ForeignKey(Division, on_delete=models.CASCADE)
