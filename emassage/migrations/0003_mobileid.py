# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('emassage', '0002_auto_20161128_0645'),
    ]

    operations = [
        migrations.CreateModel(
            name='MobileId',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('token', models.CharField(max_length=1000)),
                ('user', models.ForeignKey(related_name='threads', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
