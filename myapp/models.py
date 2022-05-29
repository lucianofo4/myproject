from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Name(models.Model):
    name_value = models.CharField(max_length=100, default="Some String")
    hora = models.CharField(max_length=255, default="Some String")

    def __str__(self):  # if Python 2 use __unicode__
        return self.name_value
