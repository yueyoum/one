# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_image_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='url',
            new_name='key',
        ),
    ]
