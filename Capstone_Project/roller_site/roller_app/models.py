from django.db import models
from random import randint

# Create your models here.

class Die(models.Model):
    name = models.TextField()
    number = models.IntegerField()

    def roll(self):
        return randint(1, self.number)


class PlayerCharacter(models.Model):
    character_name= models.CharField(max_length=50, default="Enter name here")
    ability_score= ['agility', 'smarts', 'strength', 'spirit', 'vigor']

    def __str__(self):
        return str(self.character_name) + str(self.ability_score)


# class PlayerSkills(models.Model):
#
# class PlayerEdges(models.Model):
#

















