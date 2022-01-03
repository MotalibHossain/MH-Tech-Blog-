from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone=models.CharField(max_length=15, null=True, blank=True)
    bio=models.CharField(max_length=150, null=True, blank=True)
    address=models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username +'-' +str(self.pk)

