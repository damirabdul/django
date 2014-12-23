from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=140)
    text = models.CharField(max_length=140)
    p_date =models.DateTimeField()