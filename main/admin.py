from django.contrib import admin

from main.models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'width', 'height', 'url',
        'process_done', 'display'
    )
