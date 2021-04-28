from django.db import models


class Station(models.Model):
    name = models.CharField(max_length=25)
    coordinate = models.CharField(max_length=25)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name
