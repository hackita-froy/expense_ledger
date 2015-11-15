# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0006_auto_20151115_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
