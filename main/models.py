from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """ Adding user type field to default user model """

    USER_TYPES_CHOICES = [
        ('A', 'Farmer'),
        ('B', 'Client')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(
        max_length=20,
        blank=False,
        # default='A',
        choices=USER_TYPES_CHOICES
    )


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
