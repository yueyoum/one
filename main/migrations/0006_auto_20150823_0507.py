# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150819_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='original_url',
            field=models.CharField(unique=True, max_length=255),
        ),
    ]
