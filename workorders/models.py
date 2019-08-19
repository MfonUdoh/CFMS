from django.conf import settings
from django.db import models
from django.utils import timezone
from assets.models import Asset


class WorkOrder(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    urgent = models.BooleanField()
    targetuser = models.CharField(max_length=30, default='All')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    assigned_asset = models.ForeignKey(Asset, on_delete=models.CASCADE,)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
