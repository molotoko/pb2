# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paste', '0003_auto_20151108_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='content',
            field=models.TextField(),
        ),
    ]
