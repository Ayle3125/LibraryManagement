# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_auto_20161207_0510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='borrow_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 8, 6, 27, 3, 749612)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='record',
            name='should_back_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 7, 6, 27, 3, 749689)),
            preserve_default=True,
        ),
    ]
