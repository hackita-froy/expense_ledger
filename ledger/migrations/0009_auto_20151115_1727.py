# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0008_expense_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='slug',
        ),
        migrations.AlterField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
