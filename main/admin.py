from django.contrib import admin

from main.models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'original_url', 'width', 'height', 'Img',
        'process_done', 'display',
        'result',
    )

    list_per_page = 50

    def Img(self, obj):
        return '<a href="{0}" target="_blank"><img src="{0}" width="200px"/></a>'.format(obj.link_url())
    Img.allow_tags = True
