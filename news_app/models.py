from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=New.Status.Published)


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class New(models.Model):

    class Status(models.TextChoices):
        Draft = 'DF', "Draft"
        Published = 'PB', "Published"

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images', null=True, blank=True)
    publish_time = models.DateTimeField(auto_now=timezone.now)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.Draft
    )

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.subject}, {self.email}"
