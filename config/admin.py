from django.contrib import admin

from config.models import GoogleFullAdsShowConfig

@admin.register(GoogleFullAdsShowConfig)
class GoogleFullAdsShowConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'min_click_times', 'max_click_times')
