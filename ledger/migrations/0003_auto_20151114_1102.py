# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0002_auto_20151114_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='created_on',
            field=models.DateTimeField(editable=False),
        ),
    ]
