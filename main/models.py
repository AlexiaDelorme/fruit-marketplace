from django.contrib.auth.models import User


class UserType(models.Model):
    USER_TYPE_CHOICES = [
        (A, 'Farmer'),
        (B, 'Client')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)