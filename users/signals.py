from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


"""The receiver receives inputs of a sender, which in this case is the user and a signal of post_save which is triggered when a user is saved"""
#The receiver here is the create_profile function, which takes the four parameters
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#**Kwargs takes any extra keywork arguments
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()