from django.db import models
from django.contrib.auth.models import User

class VirtualFriend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend_name = models.CharField(max_length=255)
    friend_initial_prompt = models.TextField()


