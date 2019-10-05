from django.conf import settings
from django.db import models


class BucketList(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    to_do = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    completed_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.to_do