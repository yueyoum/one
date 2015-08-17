from django.db import models


class Image(models.Model):
    original_url = models.CharField(max_length=255)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    url = models.CharField(max_length=255, blank=True)
    process_done = models.BooleanField(default=False)
    display = models.BooleanField(default=False)
    result = models.TextField(blank=True)

    class Meta:
        db_table = 'image'

