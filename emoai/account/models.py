from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mbti = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=50, blank=True)
    create_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

# Signal to create or update the user profile
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()

