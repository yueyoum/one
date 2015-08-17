# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150816_1731'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='orignal_url',
            new_name='original_url',
        ),
    ]
