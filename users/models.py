from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.files.storage import default_storage as storage
from PIL import Image

"""This class is used for the users profile and contains all the information required for the users account"""
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30, default='First Name')
    lastname = models.CharField(max_length=30, default='Last Name')
    profile_intro = models.TextField(default='Default intro. Change this to tell other users a little more about yourself')
    image = models.ImageField(default='user-default.jpg', upload_to='user_images')

    def __str__(self):
        return f'{self.user.username} Profile'

    #Resize the image as it's saved so it doesn't take too much space. If no image given then the 'user-default.jpg' image will be used for that user.
    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)
        if self.image:
            size = 250, 250
            profile_image = Image.open(self.image)
            profile_image.thumbnail(size, Image.ANTIALIAS)
            fh = storage.open(self.image.name, "w")
            profile_image.save(fh)
            fh.close()