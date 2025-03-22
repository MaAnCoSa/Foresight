from actions.fighter_str_actions import fighter_str_actions
import random

class Bard():
  def __init__(self):
    aux_stats = ["STR", "DEX", "CON", "INT", "WIS"]
    random.shuffle(aux_stats)
    self._priority_stats = ["CHA"] + aux_stats
    self._hit_die = 8

  def __str__(self):
    return "Bard"

class Barbarian():
  def __init__(self):
    aux_stats = ["DEX", "INT", "WIS", "CHA"]
    random.shuffle(aux_stats)
    self._priority_stats = ["STR", "CON"] + aux_stats
    self._hit_die = 12

  def __str__(self):
    return "Barbarian"

class Cleric():
  def __init__(self):
    aux_stats = ["STR", "DEX", "CON", "INT", "CHA"]
    random.shuffle(aux_stats)
    self._priority_stats = ["WIS"] + aux_stats
    self._hit_die = 8

  def __str__(self):
    return "Cleric"

class Druid():
  def __init__(self):
    aux_stats = ["STR", "DEX", "CON", "INT", "CHA"]
    random.shuffle(aux_stats)
    self._priority_stats = ["WIS"] + aux_stats
    self._hit_die = 8

  def __str__(self):
    return "Druid"

class FighterStr():
  def __init__(self):
    aux_stats = ["DEX", "INT", "WIS", "CHA"]
    random.shuffle(aux_stats)
    self._priority_stats = ["STR", "CON"] + aux_stats
    self._hit_die = 10
    self._actions = fighter_str_actions

  def __str__(self):
    return "Fighter (STR)"



class FighterDex():
  def __init__(self):
    aux_stats = ["STR", "INT", "WIS", "CHA"]
    random.shuffle(aux_stats)
    self._priority_stats = ["DEX", "CON"] + aux_stats
    self._hit_die = 10

  def __str__(self):
    return "Fighter (DEX)"

class Monk():
  def __init__(self):
    aux_stats = ["STR", "CON", "INT", "CHA"]
    random.shuffle(aux_stats)
    self._priority_stats = ["DEX", "WIS"] + aux_stats
    self._hit_die = 8

  def __str__(self):
    return "Monk"

class Paladin():
  def __init__(self):
    aux_stats = ["DEX", "CON", "INT", "WIS"]
    random.shuffle(aux_stats)
    self._priority_stats = ["CHA", "STR"] + aux_stats
    self._hit_die = 8 # TODO: Checar esto bien en el libro.

  def __str__(self):
    return "Paladin"

class Ranger():
  def __init__(self):
    aux_stats = ["STR", "CON", "INT", "CHA"]
    random.shuffle(aux_stats)
    self._priority_stats = ["DEX", "WIS"] + aux_stats
    self._hit_die = 10

  def __str__(self):
    return "Ranger"

class Rogue():
  def __init__(self):
    aux_stats = ["STR", "CON", "INT", "WIS", "CHA"]
    random.shuffle(aux_stats)
    self._priority_stats = ["DEX"] + aux_stats
    self._hit_die = 8

  def __str__(self):
    return "Rogue"

class Sorcerer():
  def __init__(self):
    aux_stats = ["STR", "DEX", "CON", "INT", "WIS"]
    random.shuffle(aux_stats)
    self._priority_stats = ["CHA"] + aux_stats
    self._hit_die = 6

  def __str__(self):
    return "Sorcerer"

class Wizard():
  def __init__(self):
    aux_stats = ["STR", "DEX", "CON", "WIS", "CHA"]
    random.shuffle(aux_stats)
    self._priority_stats = ["INT"] + aux_stats
    self._hit_die = 6

  def __str__(self):
    return "Wizard"
