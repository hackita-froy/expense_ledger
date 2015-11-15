# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0004_auto_20151114_1107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='user',
        ),
    ]
