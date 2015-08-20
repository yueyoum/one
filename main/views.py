import random

from django.http import JsonResponse
from django.db import connection

from main.models import Image

def get_images(request):
    with connection.cursor() as c:
        c.execute("select max(id) from {0}".format(Image._meta.db_table))
        maxid = c.fetchone()[0]

    amount = 50 if maxid > 50 else maxid

    data = []
    while not data:
        data = do_get(maxid, amount)

    return JsonResponse({'images': data})


def do_get(maxid, amount):
    ids = random.sample(xrange(1, maxid+1), amount)

    data = []
    for i in Image.objects.filter(id__in=ids):
        if not i.display:
            continue

        image = {
            'url': i.link_url(),
            'w': i.width,
            'h': i.height,
        }

        data.append(image)

    random.shuffle(data)
    return data
