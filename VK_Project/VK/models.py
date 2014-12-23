from django.contrib.auth.models import User
from django.db import models


class UserInfo(models.Model):
    user = models.OneToOneField(User)
    city = models.CharField(max_length=100, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    interests = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    sex = models.CharField(max_length=1)
    friends = models.ManyToManyField("self")

class Post(models.Model):
    from_whom = models.ForeignKey(User, related_name="from_whom")
    to_who = models.ForeignKey(User, related_name="to_who")
    post_date = models.DateTimeField()
    post_text = models.CharField(max_length=255)

class Like(models.Model):
    from_whom = models.ForeignKey(User)
    post = models.ForeignKey(Post)

class DisLike(models.Model):
    from_whom = models.ForeignKey(User)
    post = models.ForeignKey(Post)

class Comment(models.Model):
    post = models.ForeignKey(Post)
    comment_date = models.DateTimeField()
    comment_text = models.CharField(max_length=255)
    owner = models.ForeignKey(User,blank=True,null=True)
