# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       app
Date Created:   2015-08-18 00:05
Description:

"""

from django.apps import AppConfig

class MainConfig(AppConfig):
    name = 'main'

    def ready(self):
        import main.handlers
