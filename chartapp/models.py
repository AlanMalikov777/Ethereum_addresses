from django.db import models
from . import jigan
# Create your models here.

class Ether(models.Model):
    account = models.CharField(max_length=100, null=False, blank=False)
    balance = models.FloatField()

    def __str__(self):
        return f'{self.account} - {self.balance}'
        
