# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orignal_url', models.CharField(max_length=255)),
                ('width', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('url', models.CharField(default=b'', max_length=255)),
                ('process_done', models.BooleanField(default=False)),
                ('display', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'image',
            },
        ),
    ]
