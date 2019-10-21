from django.conf import settings
from django.db import models
import uuid


class BucketList(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.IntegerField(null=True,unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    to_do = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    completed_date = models.DateTimeField(blank=True, null=True)
    complete = models.BooleanField(null=True, default=False)

    def __str__(self):
        return "{} {}".format(self.id, self.to_do)

    # def increment_order():

class ProjectList(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.IntegerField(null=True,unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.id, self.project_name)
