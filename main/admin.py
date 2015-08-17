from django.contrib import admin
from django.conf import settings

from main.models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'original_url', 'width', 'height', 'Link',
        'process_done', 'display',
        'result',
    )

    def Link(self, obj):
        url = "https://s3.amazonaws.com/{0}/{1}".format(settings.S3_BUCKET_NAME, obj.url)
        return '<a href="{0}">{0}</a>'.format(url)
    Link.allow_tags = True
