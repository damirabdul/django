from django.contrib.auth.models import User
from django.db import models


class Picture(models.Model):
    picture = models.ImageField(upload_to='pictures',blank=True,null=True)
    owner = models.ForeignKey(User)
