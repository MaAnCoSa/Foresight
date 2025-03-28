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
    while self._monster_group._status == "alive" and self._party._status == "alive":
      for turn in self._turn_order:
        
        # If it's a player's turn:
        if turn["combatant"]._type == "player":
          player = turn["combatant"]

          if player._status == "conscious":
            print(f'\nTURN {i} - {player._type} - {player._class}')
            print(f"Party: {self._party._status} - Monster Group: {self._monster_group._status}")

            monster_dead = True
            while monster_dead:
              monster = random.choice(self._monsters)
              if monster._status == "conscious":
                monster_dead = False

            # TODO: Faltan acciones y sus ponderaciones para cada clase.
            action = player.use_action()
            print(f"ACTION: {action}", player._class, player._status)

            # If the action is to heal a teammate:
            if action["type"] == "heal":
              for teammate in self._party.heal_priority()[:action["creatures"]]:
                result = teammate.receive_action(action)
                print(f"RESULT: {result}", teammate._class, teammate._status)

            # If the action is against a monster:
            else:
              result = monster.receive_action(action)
              print(f"RESULT: {result}", monster._name, monster._status)

          elif player._status == "death_saves":
            print(f'\nTURN {i} - {player._type} - {player._class}')
            print(f"Party: {self._party._status} - Monster Group: {self._monster_group._status}")
            player.throw_death_save()
            player.check_status()
            print(f"DEATH SAVE - Current count: {player._death_saves}")



        # If it's a monster's turn:
        if turn["combatant"]._type == "monster" and turn["combatant"]._status == "conscious":
          print(f'\nTURN {i} - {turn["combatant"]._type} - {turn["combatant"]._name}')
          print(f"Party: {self._party._status} - Monster Group: {self._monster_group._status}")
          monster = turn["combatant"]

          # Werandomize the player target:
          target_weights = []
          for pc in self._players:
            if pc._status == "conscious":
              target_weights.append(6.0)
            elif pc._status == "death_saves":
              target_weights.append(2.0)
            else:
              target_weights.append(0.0)

          total = sum(target_weights)
          target_weights_norm = []
          for weight in target_weights:
              target_weights_norm.append(weight / total)

          player = random.choices(population=self._players, weights=target_weights_norm)[0]

          action = monster.use_action(random.choice(monster._actions))
          print(f"ACTION: {action}", monster._name, monster._status)
          result = player.receive_action(action)
          print(f"RESULT: {result}", player._class, player._status)

        self._party.check_status()
        self._monster_group.check_status()

        if self._monster_group._status == "dead" or self._party._status == "dead":
          break
        i += 1
