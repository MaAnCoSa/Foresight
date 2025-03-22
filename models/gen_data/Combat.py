import random

class Combat:
  
  def __init__(self, party, monster_group):
    self._party = party
    self._monster_group = monster_group
    self._players = [pc for pc in self._party._pcs]
    self._monsters = [monster for monster in self._monster_group._monsters]
    self._combatants = self._players + self._monsters
    self._turn_order = []
    for combatant in self._combatants:
      iniative_roll = random.randint(1, 20) + combatant._initiative
      self._turn_order.append({
          "combatant": combatant,
          "initiative": iniative_roll
      })

    self._turn_order.sort(key=lambda x: x["initiative"], reverse=True)

  def combat(self):
    # TODO: adapt it for any action, not just unarmed strike.
    unarmed_strike = {
        "type": "attack",
        "attack_stat": "STR",
        "dmg_roll": 1
    }
    
    i = 1
    while self._monster_group._status != "dead" and self._party._status != "dead":
      for turn in self._turn_order:
        print(f'\nTURN {i} - {turn["combatant"]._type} - {turn["combatant"]._class}')
        print(f"Party: {self._party._status} - Monster Group: {self._monster_group._status}")
        if turn["combatant"]._type == "player" and turn["combatant"]._status == "conscious":
          player = turn["combatant"]
          monster = random.choice(self._monsters)

          action = player.use_action(unarmed_strike)
          print(f"ACTION: {action}", player._class, player._status)
          result = monster.receive_action(action)
          print(f"RESULT: {result}", monster._class, monster._status)


        if turn["combatant"]._type == "monster" and turn["combatant"]._status == "conscious":
          monster = turn["combatant"]
          player = random.choice(self._players)

          action = monster.use_action(unarmed_strike)
          print(f"ACTION: {action}", monster._class, monster._status)
          result = player.receive_action(action)
          print(f"RESULT: {result}", player._class, player._status)

        self._party.check_status()
        self._monster_group.check_status()

        if self._monster_group._status == "dead" or self._party._status == "dead":
          break
        i += 1
