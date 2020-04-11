# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-24 08:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import easy_uploader.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='カテゴリ名')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='タイトル')),
                ('src', models.FileField(upload_to=easy_uploader.models.get_upload_to, verbose_name='ファイル')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('category', models.ForeignKey(default=easy_uploader.models.default_category, on_delete=django.db.models.deletion.PROTECT, to='easy_uploader.Category', verbose_name='カテゴリ')),
            ],
        ),
    ]