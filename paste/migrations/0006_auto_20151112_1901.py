# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('paste', '0005_paste_expiration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paste',
            name='id',
        ),
        migrations.AddField(
            model_name='paste',
            name='uu_id',
            field=models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True),
        ),
    ]
