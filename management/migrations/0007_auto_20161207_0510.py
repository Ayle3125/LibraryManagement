# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_auto_20161207_0112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='book_back_time',
        ),
        migrations.RemoveField(
            model_name='record',
            name='book_borrowed_time',
        ),
        migrations.AddField(
            model_name='record',
            name='borrow_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 7, 5, 10, 34, 648718)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='record',
            name='real_back_time',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='record',
            name='should_back_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 6, 5, 10, 34, 648748)),
            preserve_default=True,
        ),
    ]
