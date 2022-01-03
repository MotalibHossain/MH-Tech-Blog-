from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_author")
    title=models.CharField(max_length=80)
    slug=models.CharField(max_length=80, unique=True)
    blog_content=models.TextField(verbose_name="What is on your mind?")
    blog_image=models.ImageField(upload_to="Articles/", verbose_name="Image")
    publish_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date',]

    def __str__(self) -> str:
        return self.title

class comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment")
    blog=models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_comment")
    comment=models.TextField()
    publish_date=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.comment


class like(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_like")
    blog=models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_like")

