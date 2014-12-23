
from django.core import serializers
def get_users(request):
    result = ", ".join([u.username for u in User.objects.all()])

us = serializers.serialize('json',  User.objects.all(), fields=('username'))