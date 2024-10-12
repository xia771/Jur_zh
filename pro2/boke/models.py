from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    author_user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, blank=True, null=True,
                                    related_name='commented_as_author_user')
    anonymous_name = models.CharField(max_length=200, null=True, blank=True)