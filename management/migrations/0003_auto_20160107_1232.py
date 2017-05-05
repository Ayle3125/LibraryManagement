# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_bookborrow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookborrow',
            name='is_borrowed',
        ),
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(default=b'Available', max_length=20, choices=[('Available', 'Available'), ('Borrowed', 'Borrowed')]),
            preserve_default=True,
        ),
    ]
