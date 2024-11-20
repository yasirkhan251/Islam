from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.utils import timezone
from datetime import timedelta
import os
# import uuid

class MyUser(AbstractUser):

    is_user = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    server_id = models.CharField(max_length=10, null=True,blank=True, unique=True)
    doj = models.DateField(default=date.today)
    profile = models.ImageField(upload_to='static/img', null=True, blank=True)

    def delete(self, *args, **kwargs):
        if self.profile:
            if os.path.isfile(self.profile.path):
                os.remove(self.profile.path)
        super().delete(*args, **kwargs)

def default_expiry_time():
    return timezone.now() + timedelta(minutes=5)
class Forgotpassword(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    token = models.CharField(max_length=6, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=default_expiry_time)  # Callable

    def is_token_valid(self):
        return self.expires_at > timezone.now()

# Create your models here.


