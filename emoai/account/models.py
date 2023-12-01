from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mbti = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=50, blank=True)
    mbti_variant = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username

# # Signal to create or update the user profile
# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     else:
#         instance.profile.save()

# # Signal to create or update the user profile
# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     profile_defaults = kwargs.get('profile_defaults', {})
#     if created:
#         Profile.objects.create(user=instance, **profile_defaults)
#     instance.profile.save()

# Signal to create or update the user profile
# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created and not hasattr(instance, 'profile'):
#         Profile.objects.create(user=instance)
#     elif hasattr(instance, 'profile'):
#         instance.profile.save()



