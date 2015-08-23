from django.db import models

class GoogleFullAdsShowConfig(models.Model):
    id = models.IntegerField(primary_key=True)
    min_click_times = models.IntegerField()
    max_click_times = models.IntegerField()

    class Meta:
        db_table = 'config_google_full_ads'
