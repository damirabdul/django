# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20141223_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'pictures', blank=True),
            preserve_default=True,
        ),
    ]
