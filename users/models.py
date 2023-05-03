from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(default=0)
    age = models.IntegerField()
    bio = models.TextField()
    # add other fields here

    def __str__(self):
        return self.user.username