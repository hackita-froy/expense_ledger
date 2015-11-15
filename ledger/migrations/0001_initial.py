# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('expense_date', models.DateTimeField(verbose_name='expense ledger')),
                ('amount', models.DecimalField(max_digits=5, decimal_places=2)),
                ('details', models.CharField(max_length=300)),
            ],
        ),
    ]
