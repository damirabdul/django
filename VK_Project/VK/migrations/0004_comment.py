# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VK', '0003_userinfo_friends'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_date', models.DateTimeField()),
                ('comment_text', models.CharField(max_length=255)),
                ('post', models.ForeignKey(to='VK.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
