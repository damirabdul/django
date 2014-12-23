from django.contrib.auth.models import User
from django.db import models

class Message(models.Model):
    from_whom = models.ForeignKey(User, related_name="from")
    to_who = models.ForeignKey(User, related_name="to")
    message_date = models.DateTimeField()
    message_text = models.CharField(max_length=255)