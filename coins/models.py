from django.db import models


class Coin(models.Model):
    title = models.CharField(max_length=200)
    action = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    quant = models.DecimalField(max_digits=10, decimal_places=2)
