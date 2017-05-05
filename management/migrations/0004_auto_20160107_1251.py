# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20160107_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book_borrowed_time', models.DateTimeField()),
                ('book_back_time', models.DateTimeField(null=True)),
                ('book', models.ForeignKey(to='management.Book')),
                ('borrow_by_user', models.ForeignKey(to='management.MyUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='bookborrow',
            name='book',
        ),
        migrations.RemoveField(
            model_name='bookborrow',
            name='borrow_by_user',
        ),
        migrations.DeleteModel(
            name='BookBorrow',
        ),
        migrations.AddField(
            model_name='myuser',
            name='school_ID',
            field=models.CharField(default=b'', max_length=10),
            preserve_default=True,
        ),
    ]
