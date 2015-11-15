    # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ledger', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='expense_date',
        ),
        migrations.AddField(
            model_name='expense',
            name='created_on',
            field=models.DateTimeField(editable=False, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=-1),
            preserve_default=False,
        ),
    ]
