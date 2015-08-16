from django.db import models
from django.db.models.signals import post_save


class Image(models.Model):
    orignal_url = models.CharField(max_length=255)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    url = models.CharField(max_length=255, blank=True)
    process_done = models.BooleanField(default=False)
    display = models.BooleanField(default=False)

    class Meta:
        db_table = 'image'



def on_save(instance, **kwargs):
    from task import image_process
    if not instance.process_done:
        image_process(image_id=instance.id)


post_save.connect(
    on_save,
    sender=Image,
    dispatch_uid='Image.post_save'
)
