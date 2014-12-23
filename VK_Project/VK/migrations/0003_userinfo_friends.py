# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VK', '0002_dislike_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='friends',
            field=models.ManyToManyField(related_name='friends_rel_+', to='VK.UserInfo'),
            preserve_default=True,
        ),
    ]
