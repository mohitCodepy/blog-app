from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfile(models.Model):
    """
    UserProfile
        Contains the user related information 
        such as profile_pic, bio, username, password management etc...
    """

    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(blank=True, null=True, upload_to='user-media/')
    bio = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}"
    

