# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paste', '0004_auto_20151109_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='paste',
            name='expiration',
            field=models.IntegerField(default=0, choices=[(0, b'Never'), (1, b'10 Minutes'), (2, b'1 Hour'), (3, b'1 Day'), (4, b'1 Week'), (5, b'2 Weeks'), (6, b'1 Month')]),
        ),
    ]
