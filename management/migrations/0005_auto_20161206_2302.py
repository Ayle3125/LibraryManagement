# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20160107_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='num',
            field=models.IntegerField(default=1, max_length=11),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='record',
            name='book_back_time',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='record',
            name='book_borrowed_time',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
