# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='from_whom',
            field=models.ForeignKey(related_name='fromm', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
