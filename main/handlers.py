# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       handlers
Date Created:   2015-08-18 00:06
Description:

"""

import json

from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from main.models import Image

@receiver(post_save, sender=Image, dispatch_uid='Image.post_save')
def image_save(instance, **kwargs):
    from tasks import task
    if not instance.process_done:
        data = {
            'image_id': instance.id,
            'original_url': instance.original_url
        }

        data=json.dumps(data)
        task.image_put(data=data)

@receiver(post_delete, sender=Image, dispatch_uid='Image.post_delete')
def image_delete(instance, **kwargs):
    from tasks import task

    data = {'key': instance.url}
    data = json.dumps(data)
    task.image_delete(data=data)
