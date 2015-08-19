from django.contrib import admin

from main.models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'original_url', 'width', 'height', 'Link',
        'process_done', 'display',
        'result',
    )

    def Link(self, obj):
        return '<a href="{0}">{0}</a>'.format(obj.link_url())
    Link.allow_tags = True
