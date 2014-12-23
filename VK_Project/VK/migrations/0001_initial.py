# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_date', models.DateTimeField()),
                ('post_text', models.CharField(max_length=255)),
                ('from_whom', models.ForeignKey(related_name='from_whom', to=settings.AUTH_USER_MODEL)),
                ('to_who', models.ForeignKey(related_name='to_who', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=100, null=True, blank=True)),
                ('birthday', models.DateField(null=True, blank=True)),
                ('interests', models.CharField(max_length=255, null=True, blank=True)),
                ('avatar', models.ImageField(null=True, upload_to=b'avatars', blank=True)),
                ('sex', models.CharField(max_length=1)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
