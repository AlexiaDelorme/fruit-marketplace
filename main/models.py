from django.db import models
from django.contrib.auth.models import User


class UserType(models.Model):
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
