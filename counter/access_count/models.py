from django.db import models

class Count(models.Model):
    count = models.IntegerField(default=0)
