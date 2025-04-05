import random
import numpy as np

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

  def combat(self, verbose=0):
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
            if verbose >= 1:
              print(f'\nTURN {i} - {player._type} - {player._class}')
              print(f"Party: {self._party._status} - Monster Group: {self._monster_group._status}")

            num_actions = 1
            if player._class._name == "FighterStr":
              if player._class._action_surges > 0:
                p = 2/(player._turns_since_action_surge+3)
                print(f"Prob of using Action Surge: {1-p}")
                player._use_action_surge = random.choices(population=[True, False], weights=[1-p, p])[0]
                print(f"USE ACTION SURGE: {player._use_action_surge}")

              print(player._use_action_surge)
              if player._use_action_surge == True:
                print("use_action_surge is True")
                num_actions += 1
                player._use_action_surge = False
                player._class._action_surges -= 1
                player._turns_since_action_surge = 0
              else:
                player._turns_since_action_surge += 1

            
            print(f"NUM ACTIONS: {num_actions}")
            for _ in range(num_actions):
              action = player.use_action(verbose)
              if verbose >= 1:
                print(f"ACTION: {action}", player._class, player._status)


              # If the action is to heal a teammate:
              if action["type"] == "heal":
                for teammate in self._party.heal_priority()[:action["creatures"]]:
                  result = teammate.receive_action(action)
                  if verbose >= 1:
                    print(f"RESULT: {result}", teammate._class, teammate._status)

              # If the action is against a monster:
              elif action["type"] in ["attack", "dc"]:
                possible_targets = []
                
                for monster in self._monster_group._monsters:
                  if monster._status == "conscious":
                    possible_targets.append(monster)

                if len(possible_targets) != 0:
                  targets = []
                  if action["target_type"] == "creature_amount":
                    for j in range(action["amount_creatures"]):
                      choice = random.choice(possible_targets)
                      targets.append(choice)
                      possible_targets.remove(choice)
                  elif action["target_type"] == "aoe":
                    j = 0
                    random.shuffle(possible_targets)
                    for possible_target in possible_targets:
                      p = 1/(j+1) # Probability of enemy being in range.
                      in_range = random.choices(population=[True, False], weights=[p, 1-p])
                      if in_range == True:
                        targets.append(possible_target)
                      
                  for target in targets:
                    result = target.receive_action(action)
                    if verbose >= 1:
                      print(f"RESULT: {result}", monster._name, monster._status)
                else:
                  if verbose >= 1:
                    print(f"RESULT: No valid targets for action: {action['name']}")
  
          elif player._status == "death_saves":
            if verbose >= 1:
              print(f'\nTURN {i} - {player._type} - {player._class}')
              print(f"Party: {self._party._status} - Monster Group: {self._monster_group._status}")
            player.throw_death_save()
            player.check_status()
            if verbose >= 1:
              print(f"DEATH SAVE - Current count: {player._death_saves}")
          
          i += 1


        # If it's a monster's turn:
        if turn["combatant"]._type == "monster" and turn["combatant"]._status == "conscious":
          if verbose >= 1:
            print(f'\nTURN {i} - {turn["combatant"]._type} - {turn["combatant"]._name}')
            print(f"Party: {self._party._status} - Monster Group: {self._monster_group._status}")
          monster = turn["combatant"]
          action = monster.use_action(verbose)
          if verbose >= 1:
            print(f"ACTION: {action}", monster._name, monster._status)

          # We randomize the player target:
          possible_targets = []
          target_weights = []
              
          for player in self._party._pcs:
            if player._status == "conscious":
              possible_targets.append(player)
              target_weights.append(6.0)
            elif player._status == "death_saves":
              possible_targets.append(player)
              target_weights.append(2.0)

          total = sum(target_weights)
          target_weights_norm = []
          for weight in target_weights:
              target_weights_norm.append(weight / total)

          targets = []
          if action["target_type"] == "creature_amount":
            targets = np.random.choice(possible_targets, action["amount_creatures"],replace=False, p=target_weights_norm)
              
          elif action["target_type"] == "aoe":
            j = 0
            random.shuffle(possible_targets)
            for possible_target in possible_targets:
              p = 1/(j+1) # Probability of enemy being in range.
              in_range = random.choices([True, False], weights=[p, 1-p])[0]
              if in_range == True:
                targets.append(possible_target)
              
          #print(f"TARGETS: {targets}")
          for target in targets:
            result = target.receive_action(action)
            if verbose >= 1:
              print(f"RESULT: {result}", target._class, target._status)

          i += 1

          # result = player.receive_action(action)
          # if verbose == 1:
          #   print(f"RESULT: {result}", player._class, player._status)

        self._party.check_status()
        self._monster_group.check_status()

        if self._monster_group._status == "dead" or self._party._status == "dead":
          break
