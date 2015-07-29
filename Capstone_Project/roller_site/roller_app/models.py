from django.db import models
from random import randint

# Create your models here.

class Die(models.Model):
    name = models.TextField()
    number = models.IntegerField()

    def roll(self):
        return str(self.name), + randint(1, self.number)














