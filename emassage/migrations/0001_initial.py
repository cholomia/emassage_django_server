# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('objective', models.TextField(blank=True)),
                ('sequence', models.IntegerField(unique=True)),
                ('coverImage', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('objective', models.TextField(blank=True)),
                ('sequence', models.IntegerField(unique=True)),
                ('coverImage', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('sequence', models.IntegerField(unique=True)),
                ('coverImage', models.FileField(blank=True, null=True, upload_to='')),
                ('pdf', models.FileField(upload_to='')),
                ('category', models.ForeignKey(related_name='lessons', to='emassage.Category')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='course',
            field=models.ForeignKey(related_name='categories', to='emassage.Course'),
        ),
    ]
