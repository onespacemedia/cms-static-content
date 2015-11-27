# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaticContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Short name used to identify the content object within the admin', max_length=b'4096')),
                ('url', models.CharField(max_length=b'4096', unique=True, null=True, blank=True)),
                ('content_type', models.CharField(default=b'text/plain', max_length=b'4096')),
                ('content', models.TextField(null=True, blank=True)),
                ('base64', models.BooleanField(default=False, help_text=b'Check if content is base64 encoded')),
            ],
        ),
    ]
