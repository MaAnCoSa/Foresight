from actions.fighter_str_actions import fighter_str_actions
from actions.barbarian_actions import barbarian_actions
from actions.bard_actions import bard_actions
import random

class Bard():
  def __init__(self):
    self._name = "Bard"
    
    aux_stats = ["STR", "DEX", "CON", "INT", "WIS"]
    random.shuffle(aux_stats)
    self._priority_stats = ["CHA"] + aux_stats
    self._hit_die = 8

    self._actions = bard_actions

  def __str__(self):
    return "Bard"

class Barbarian():
  def __init__(self):
    self._name = "Barbarian"
    
    aux_stats = ["DEX", "INT", "WIS", "CHA"]
    random.shuffle(aux_stats)
    self._priority_stats = ["STR", "CON"] + aux_stats
    self._hit_die = 12
    
    self._rage_bonus = {
      1: 2,
      2: 2,
      3: 2,
      4: 2,
      5: 2,
      6: 2,
      7: 2,
      8: 2,
      9: 3,
      10: 3,
      11: 3,
      12: 3,
      13: 3,
      14: 3,
      15: 3,
      16: 4,
      17: 4,
      18: 4,
      19: 4,
      20: 4
    }
    
    self._actions = barbarian_actions

  def __str__(self):
    return "Barbarian"

class Cleric():
  def __init__(self):
    self._name = "Cleric"
    
    aux_stats = ["STR", "DEX", "CON", "INT", "CHA"]
    random.shuffle(aux_stats)
    self._priority_stats = ["WIS"] + aux_stats
    self._hit_die = 8

    self._actions = barbarian_actions

  def __str__(self):
    return "Cleric"

class Druid():
  def __init__(self):
    self._name = "Druid"
    
    aux_stats = ["STR", "DEX", "CON", "INT", "CHA"]
    random.shuffle(aux_stats)
    self._priority_stats = ["WIS"] + aux_stats
    self._hit_die = 8

    self._actions = barbarian_actions

  def __str__(self):
    return "Druid"

class FighterStr():
  def __init__(self):
    self._name = "FighterStr"
    
    aux_stats = ["DEX", "INT", "WIS", "CHA"]
    random.shuffle(aux_stats)
    self._priority_stats = ["STR", "CON"] + aux_stats
    self._hit_die = 10

    self._actions = fighter_str_actions

  def __str__(self):
    return "Fighter (STR)"

class FighterDex():
  def __init__(self):
    self._name = "FighterDex"
    
    aux_stats = ["STR", "INT", "WIS", "CHA"]
    random.shuffle(aux_stats)
    self._priority_stats = ["DEX", "CON"] + aux_stats
    self._hit_die = 10

    self._actions = barbarian_actions

  def __str__(self):
    return "Fighter (DEX)"

class Monk():
  def __init__(self):
    self._name = "Monk"
    
    aux_stats = ["STR", "CON", "INT", "CHA"]
    random.shuffle(aux_stats)
    self._priority_stats = ["DEX", "WIS"] + aux_stats
    self._hit_die = 8

    self._actions = barbarian_actions

  def __str__(self):
    return "Monk"

class Paladin():
  def __init__(self):
    self._name = "Paladin"
    
    aux_stats = ["DEX", "CON", "INT", "WIS"]
    random.shuffle(aux_stats)
    self._priority_stats = ["CHA", "STR"] + aux_stats
    self._hit_die = 10

    self._actions = barbarian_actions

  def __str__(self):
    return "Paladin"

class Ranger():
  def __init__(self):
    self._name = "Ranger"
    
    aux_stats = ["STR", "CON", "INT", "CHA"]
    random.shuffle(aux_stats)
    self._priority_stats = ["DEX", "WIS"] + aux_stats
    self._hit_die = 10

    self._actions = barbarian_actions

  def __str__(self):
    return "Ranger"

class Rogue():
  def __init__(self):
    self._name = "Rogue"
    
    aux_stats = ["STR", "CON", "INT", "WIS", "CHA"]
    random.shuffle(aux_stats)
    self._priority_stats = ["DEX"] + aux_stats
    self._hit_die = 8

    self._actions = barbarian_actions

  def __str__(self):
    return "Rogue"

class Sorcerer():
  def __init__(self):
    self._name = "Sorcerer"
    
    aux_stats = ["STR", "DEX", "CON", "INT", "WIS"]
    random.shuffle(aux_stats)
    self._priority_stats = ["CHA"] + aux_stats
    self._hit_die = 6

    self._actions = barbarian_actions

  def __str__(self):
    return "Sorcerer"

class Wizard():
  def __init__(self):
    self._name = "Wizard"
    
    aux_stats = ["STR", "DEX", "CON", "WIS", "CHA"]
    random.shuffle(aux_stats)
    self._priority_stats = ["INT"] + aux_stats
    self._hit_die = 6

    self._actions = barbarian_actions

  def __str__(self):
    return "Wizard"
