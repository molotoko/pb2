# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paste', '0002_auto_20151020_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
