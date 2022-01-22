from django.db import models

class Table(models.Model):
    result = models.JSONField()
    time_in_s = models.FloatField(null=False)
    max_memory_in_MB = models.FloatField(null=False)

