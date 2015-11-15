# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paste',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('title', models.CharField(max_length=30, blank=True)),
                ('syntax', models.IntegerField(default=0, choices=[(0, b'Plain'), (1, b'Python'), (2, b'HTML'), (3, b'SQL'), (4, b'Javascript'), (5, b'CSS')])),
                ('poster', models.CharField(max_length=30, blank=True)),
                ('expiration', models.IntegerField(default=0, choices=[(0, b'Never'), (1, b'10 Minutes'), (2, b'1 Hour'), (3, b'1 Day'), (4, b'1 Week'), (5, b'2 Weeks'), (6, b'1 Month')])),
                ('exposure', models.IntegerField(default=0, choices=[(0, b'Public'), (1, b'Unlisted'), (2, b'Private')])),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('uu_id', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
