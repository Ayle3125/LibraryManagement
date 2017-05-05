# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookBorrow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_borrowed', models.BooleanField(default=False)),
                ('book_borrowed_time', models.DateTimeField()),
                ('book_back_time', models.DateTimeField(null=True)),
                ('book', models.ForeignKey(to='management.Book')),
                ('borrow_by_user', models.ForeignKey(to='management.MyUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
