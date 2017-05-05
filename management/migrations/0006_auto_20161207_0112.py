# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_auto_20161206_2302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='borrow_by_user',
            new_name='user',
        ),
        migrations.AddField(
            model_name='record',
            name='state',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
