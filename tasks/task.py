# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       task
Date Created:   2015-08-17 00:52
Description:

"""

import json
import hashlib
import traceback
import mimetypes
from cStringIO import StringIO

from django.conf import settings

import uwsgidecorators
import requests
from PIL import Image
import boto3


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0',
}

@uwsgidecorators.spool
def image_put(args):
    from main.models import Image as ModelImage

    data = json.loads(args['data'])
    image_id = data['image_id']
    original_url = data['original_url']

    try:
        req = requests.get(original_url, headers=HEADERS)
        if not req.ok:
            raise Exception("status code = {0}".format(req.status_code))


        content = req.content
        buf = StringIO(content)

        im = Image.open(buf)
        width, height = im.size
        name = '{0}.{1}'.format(
            hashlib.md5(content).hexdigest(),
            im.format
        )

        content_type, _ = mimetypes.guess_type(name)
        if not content_type:
            raise Exception("Invalid ContentType.")

        s3 = boto3.resource('s3')
        bucket = s3.Bucket(settings.S3_BUCKET_NAME)
        bucket.put_object(ACL='public-read', Key=name, Body=content, ContentType=content_type)
    except:
        ModelImage.objects.filter(id=image_id).update(
            result=traceback.format_exc()
        )
    else:
        ModelImage.objects.filter(id=image_id).update(
            width=width,
            height=height,
            key=name,
            process_done=True,
            display=True,
            result='OK'
        )


@uwsgidecorators.spool
def image_delete(args):
    data = json.loads(args['data'])
    key = data['key']

    s3 = boto3.resource('s3')
    obj = s3.Object(settings.S3_BUCKET_NAME, key)
    obj.delete()
