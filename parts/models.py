from django.conf import settings
from django.db import models
from django.utils import timezone


class Part(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    quantity = models.IntegerField(default=1)
    assigned_asset = models.ForeignKey('assets.asset.name', on_delete=models.CASCADE,)
    created_date = models.DateTimeField(default.timezone.now)

    def __str__(self):
        return self.name
