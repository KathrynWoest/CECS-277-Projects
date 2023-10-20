import entity
import random


class Hero(entity.Entity):
  '''Represents a hero
  Attributes:
  name : name of the hero
  max_hp : the maximum health of the hero
  hp : the current health of the hero
  '''
  
  def basic_attack(self, other):
    """Description: attacks the dragon with a basic attack (2 D6)
    Input: the object representing the dragon
    Output/Return: returns a string describing what happened"""
    damage = random.randint(1, 6) + random.randint(1, 6)
    other.take_damage(damage)
    return self._name + " slashes the "+ other._name + " with their sword for " + str(damage) + " damage!"
  
  def special_attack(self, other):
    """Description: attacks the dragon with a special attack (1 D12)
    Input: the object representing the dragon
    Output/Return: returns a string describing what happened"""
    damage = random.randint(1, 12)
    other.take_damage(damage)
    return self._name + " hits the "+ other._name + " with an arrow for " + str(damage) + " damage!"
