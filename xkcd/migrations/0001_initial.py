# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-02 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveIntegerField(unique=True)),
                ('title', models.CharField(max_length=256)),
                ('safe_title', models.CharField(max_length=256)),
                ('date', models.DateField()),
                ('img', models.CharField(max_length=256)),
                ('alt', models.TextField(blank=True)),
                ('link', models.CharField(blank=True, max_length=256)),
                ('news', models.TextField(blank=True)),
                ('transcript', models.TextField(blank=True)),
                ('local_img', models.ImageField(blank=True, max_length=512, null=True, upload_to=b'xkcd/img/%Y/%m/%d', verbose_name=b'local comic image')),
            ],
            options={
                'ordering': ('date',),
            },
        ),
    ]
