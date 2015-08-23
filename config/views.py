from django.http import JsonResponse
from config.models import GoogleFullAdsShowConfig


def get_config(request):
    config = GoogleFullAdsShowConfig.objects.get(id=1)
    data = {
        'min_times': config.min_click_times,
        'max_times': config.max_click_times,
    }

    response = {
        'googleconfig': data
    }

    return JsonResponse(response)

