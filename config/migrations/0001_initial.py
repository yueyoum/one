# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleFullAdsShowConfig',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('min_click_times', models.IntegerField()),
                ('max_click_times', models.IntegerField()),
            ],
            options={
                'db_table': 'config_google_full_ads',
            },
        ),
    ]
