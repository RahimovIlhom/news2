from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users', null=True, blank=True)
    phone_number = models.CharField(max_length=12, default=None, null=True)
    birth_of_day = models.DateTimeField(null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.user} - profili"
