from django.db import models
from random import randint


# Create your models here.

class Die(models.Model):
    name = models.TextField()
    number = models.IntegerField()

    def roll(self):
        return randint(1, self.number)


class PlayerCharacter(models.Model):
    character_name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return str(self.character_name)


class Abilities(models.Model):
    ability_name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return str(self.ability_name)

class AbilityValues(models.Model):
    name = models.CharField(max_length=50, blank=False)
    value = models.IntegerField()

    def __str__(self):
        return str(self.name)

class PCValue(models.Model):
    character = models.ForeignKey(PlayerCharacter)
    ability = models.ForeignKey(Abilities)
    die_value = models.ForeignKey(AbilityValues)

    def __str__(self):
        return str(self.character.character_name) + str(self.ability.ability_name) + str(self.die_value.name)
