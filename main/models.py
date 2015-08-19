from django.conf import settings
from django.db import models


class Image(models.Model):
    original_url = models.CharField(max_length=255)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    key = models.CharField(max_length=255, blank=True)
    process_done = models.BooleanField(default=False)
    display = models.BooleanField(default=False)
    result = models.TextField(blank=True)

    class Meta:
        db_table = 'image'


    def link_url(self):
        url = "https://s3.amazonaws.com/{0}/{1}".format(settings.S3_BUCKET_NAME, self.key)
        return url

