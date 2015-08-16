# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       task
Date Created:   2015-08-17 00:52
Description:

"""

import uwsgidecorators

@uwsgidecorators.spool
def image_process(args):
    from main.models import Image
    import time

    print args
    time.sleep(5)
    image_id = int(args['image_id'])
    Image.objects.filter(id=image_id).update(
        url=str(time.time()),
        display=True
    )

