from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    availability_status = models.BooleanField(default=True)
    metadata = models.TextField(null=True, blank=True)
