# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0003_auto_20151114_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
