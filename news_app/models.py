from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=New.Status.Published)


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)

    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_news', args=[str(self.slug)])


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

    def get_absolute_url(self):
        return reverse('single', args=[str(self.slug)])

    def get_category_url(self):
        return reverse('category_news', args=[str(self.category.slug)])


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.subject}, {self.email}"


class Comment(models.Model):
    news = models.ForeignKey(New, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    create_time = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        ordering = ['-create_time']

    def __str__(self):
        return f"{self.news} - {self.user}: {self.comment}"


class ReplyComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='reply_comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reply_comments')
    reply_comment = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        ordering = ['-create_time']

    def __str__(self):
        return f"{self.user} - {self.reply_comment}"


class CountView(models.Model):
    count = models.GenericIPAddressField()
