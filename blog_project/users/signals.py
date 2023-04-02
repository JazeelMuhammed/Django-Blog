# POST_SAVE is a signal that triggered when an object is saved.
from django.db.models.signals import post_save

# User model is the sender, means sending the signal
from django.contrib.auth.models import User

# a RECEIVER is a function that takes the signal and perform some task.
from django.dispatch import receiver
from .models import User_Profile

# When a User is received it sends a signal called "post_save" and this "post_save"
# signal is received by the @receiver.Here "receiver" is the "create_user_profile"
# function which takes all the params that our "post_save" signal passes.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # IF A "USER" IS CREATED A "USER_PROFILE" IS CREATING ALONG WITH IT
    if created:
        User_Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.user_profile.save()









