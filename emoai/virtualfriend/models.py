from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    # File will be uploaded to MEDIA_ROOT/user_data/<username>/friend_avatars/<filename>
    return 'user_data/{0}/friend_avatars/{1}'.format(instance.user.username, filename)


class VirtualFriend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend_name = models.CharField(max_length=255)
    friend_mbti = models.CharField(max_length=50, null = True, blank=True)
    friend_mbti_variant = models.CharField(max_length=50, null = True, blank=True)
    friend_initial_prompt = models.TextField(null = True, blank=True)
    friend_avatar = models.ImageField(upload_to=user_directory_path, null=True, blank=True)


