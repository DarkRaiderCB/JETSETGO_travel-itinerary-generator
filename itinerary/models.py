from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User


# defines a Profile model linked to the User model with one-to-one relationship
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


# signal to automatically create and save a Profile instance whenever a User is created or saved.
@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(instance, **kwargs):
    instance.profile.save()
