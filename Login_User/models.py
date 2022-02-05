from ast import Pass
from django.db import models
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls import reverse_lazy,reverse


class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone=models.CharField(max_length=15, null=True, blank=True)
    bio=models.CharField(max_length=150, null=True, blank=True)
    address=models.CharField(max_length=50, null=True, blank=True)


    def get_absulate_url(self):
        # return reverse_lazy('Login_User:Profile', args=[self.user.username])
        return reverse("Login_User:Profile", kwargs={'username':self.user.username})
    def __str__(self) -> str:
        return self.user.username +'-' +str(self.pk)

