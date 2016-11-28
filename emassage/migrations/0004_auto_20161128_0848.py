# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('emassage', '0003_mobileid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, null=True, blank=True)),
                ('content', models.TextField(null=True, blank=True)),
                ('points', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(null=True, to='emassage.Thread', related_name='comments', blank=True)),
                ('user', models.ForeignKey(related_name='threads', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='mobileid',
            name='user',
            field=models.ForeignKey(related_name='tokens', to=settings.AUTH_USER_MODEL),
        ),
    ]
