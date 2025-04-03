import random
import math

class Monster:
    def __init__(self, monster_data, spells_data):
        self._name = monster_data["name"]
        self._type = "monster"
        self._stats = {"STR": monster_data["strength"], "DEX": monster_data["dexterity"], "CON": monster_data["constitution"], "INT": monster_data["intelligence"], "WIS": monster_data["wisdom"], "CHA": monster_data["charisma"]}
        self._modifiers = {}
        for stat in self._stats.keys():
          score = self._stats[stat]
          modifier = math.floor((score - 10) / 2)
          self._modifiers[stat] = modifier

        self._challenge_rating = monster_data["challenge_rating"]
        self._prof_bonus = 2

        self._hp_max = monster_data["hit_points"]
        self._hp = self._hp_max
        self._ac = monster_data["armor_class"][0]["value"]
        self._initiative = self._modifiers["DEX"]
        self._status = "conscious"

        self._death_saves = {"successes": 0, "failures": 0}

        self._proficiency_bonus = 2
        self._proficiencies = {
            "saving_throws": [],
            "skills": []
        }
        for proficiency in monster_data["proficiencies"]:
          profType = proficiency["proficiency"]["name"].split(": ")
          if profType[0] == "Saving Throw":
            self._proficiencies["saving_throws"].append({
                "stat": profType[1],
                "value": proficiency["value"]
              })
          elif profType[0] == "Skill":
            self._proficiencies["skills"].append({
                "skill": profType[1],
                "value": proficiency["value"]
              })
        
        self._dmg_vulnerabilities = monster_data['damage_vulnerabilities']
        self._dmg_resistances = monster_data['damage_resistances']
        self._dmg_immunities = monster_data['damage_immunities']
        self._condition_immunities = monster_data['condition_immunities']

        print(f"DMG VULNERABILITIES: {self._dmg_vulnerabilities}")
        print(f"DMG RESISTANCES: {self._dmg_resistances}")
        print(f"DMG IMMUNITIES: {self._dmg_immunities}")
        print(f"CONDITION IMMUNITIES: {self._condition_immunities}")

        self._actions = []
        multiattack_actions = []
        for original_action in monster_data["actions"]:
          print("OG Action:\t" + str(original_action))
          if original_action["name"] not in multiattack_actions:
            if original_action["name"] == "Multiattack":
              print("MULTIATTACK")

              attacks = []
              for multi_act in original_action["actions"]:
                print("Multi act: " + str(multi_act))

                for act in monster_data["actions"]:
                  print("\t" + str(act))
                  if act["name"] == multi_act["action_name"] and act["name"] != "Multiattack" and multi_act["type"] != "ability":
                    print("FOUND:\t" + str(act))

                    for count in range(multi_act["count"]):
                      attack = {
                          "attack_bonus": act["attack_bonus"],
                          "sources": []
                      }
                      for source in act['damage']:
                        if 'choose' not in source:
                          dmg_parts = source["damage_dice"].split("+")
                          if len(dmg_parts) == 1:
                             dmg_bonus = 0
                          else:
                             dmg_bonus = int(dmg_parts[1])

                          dmg_parts = dmg_parts[0].split("d")
                          if len(dmg_parts) == 1:
                             count = 0
                             dmg_dice = int(dmg_parts[0])
                          else:
                             count = int(dmg_parts[0])
                             dmg_dice = int(dmg_parts[1])

                          attack["sources"].append({
                              "dmg_type": source["damage_type"]["name"],
                              "dmg_dice": dmg_dice,
                              "count": count,
                              "dmg_bonus": dmg_bonus
                          })

                      multiattack_actions.append(act["name"])
                      attacks.append(attack)
              action = {
                "name": original_action["name"],
                "type": "attack#physical",
                "target_type": "creature_amount",
                "amount_creatures": 1,
                "attacks": attacks
              }
              self._actions.append(action)
            elif "usage" in original_action:
              action = {
                "name": original_action["name"],
                "type": "attack#physical",
                "attack_type": "usage"
              }
            elif "dc" in original_action:
              action = {
                "name": original_action["name"],
                "type": "dc#physical",
                "dc_stat": original_action["dc"]["dc_type"]["name"],
                "dc_value": original_action["dc"]["dc_value"]
              }

            else:
              action = {
                  "name": original_action["name"],
                  "type": "attack#physical",
                  "attacks": [{
                    "attack_bonus": original_action["attack_bonus"],
                    "sources": []
                  }]
                }
              for source in original_action['damage']:
                if 'choose' not in source:
                  dmg_parts = source["damage_dice"].split("+")
                  if len(dmg_parts) == 1:
                      dmg_bonus = 0
                  else:
                      dmg_bonus = int(dmg_parts[1])

                  dmg_parts = dmg_parts[0].split("d")
                  if len(dmg_parts) == 1:
                      count = 0
                      dmg_dice = int(dmg_parts[0])
                  else:
                      count = int(dmg_parts[0])
                      dmg_dice = int(dmg_parts[1])

                  action["attacks"][0]["sources"].append({
                      "dmg_type": source["damage_type"]["name"],
                      "dmg_dice": dmg_dice,
                      "count": count,
                      "dmg_bonus": dmg_bonus
                  })
              self._actions.append(action)
            
        for ability in monster_data["special_abilities"]:

          if "spellcasting" in ability:
            print("HAS SPELLCASTING")

            self._spellcasting = True
            spellcasting_info = ability["spellcasting"]
            self._since_last_spell = 5

            self._spellcasting_modifier = self._modifiers[spellcasting_info["ability"]["name"]]
            self._spellcasting_dc = spellcasting_info["dc"]
            if "slots" in spellcasting_info:
              self._spell_slots = spellcasting_info["slots"]
              self._remaining_spell_slots = self._spell_slots
            else:
              self._spell_slots = {}
            
            # We add each spell.
            for spell in spellcasting_info["spells"]:
              for original_spell in spells_data:
                if original_spell["name"] == spell["name"]:
                  print(original_spell["name"])
                  if "damage" in original_spell:
                    print("Considered spell action.")
                    spell_action = {}

                    spell_action["name"] = original_spell["name"]
                    
                    if "dc" in original_spell:
                      spell_action["type"] = "dc"
                      spell_action["st"] = original_spell["dc"]["dc_type"]["name"]
                      if original_spell["dc"]["dc_success"] == "half":
                        spell_action["half"] = True
                      else:
                        spell_action["half"] = False
                    else:
                      spell_action["type"] = "attack"

                    if spell["level"] == 0:
                      spell_action["type"] += "#cantrip"
                    else:
                      spell_action["type"] += "#spell"

                    spell_action["level"] = spell["level"]

                    if "area_of_effect" in original_spell:
                      spell_action["target_type"] = "aoe"
                      spell_action["radius"] = original_spell["area_of_effect"]["size"]
                    else:
                      spell_action["target_type"] = "creature_amount"
                      spell_action["amount_creatures"] = 1 # Not always, but we can't parse the creature amount yet.
                    
                    if "damage_at_slot_level" in original_spell["damage"]:
                      spell_dmg = original_spell["damage"]["damage_at_slot_level"][str(original_spell["level"])]
                    elif "damage_at_character_level" in original_spell["damage"]:
                      for i in list(original_spell["damage"]["damage_at_character_level"].keys()):
                        if int(spellcasting_info["level"]) > int(i):
                          level_to_use = i
                      spell_dmg = original_spell["damage"]["damage_at_character_level"][level_to_use]
                    
                    dmg_parts = spell_dmg.split(" + ")
                    if dmg_parts[-1] == "MOD":
                       dmg_bonus = int(self._spellcasting_modifier)
                    else:
                       dmg_bonus = 0
                    dmg_roll = dmg_parts[0].split("d")
                    if "dc" in original_spell:
                      dmg_rolls = [{
                          "count": int(dmg_roll[0]),
                          "dmg_dice": int(dmg_roll[1]),
                          "dmg_bonus": int(dmg_bonus),
                          "dmg_type": original_spell["damage"]["damage_type"]["index"]
                      }]
                      spell_action["dmg_rolls"] = dmg_rolls
                    else:
                      attacks = [{
                        "attack_bonus": self._spellcasting_modifier,
                        "sources": [{
                            "count": int(dmg_roll[0]),
                            "dmg_dice": int(dmg_roll[1]),
                            "dmg_bonus": int(dmg_bonus),
                            "dmg_type": original_spell["damage"]["damage_type"]["index"]
                        }]
                      }]
                      spell_action["attacks"] = attacks
                    

                    self._actions.append(spell_action)
                    if "slots" not in spellcasting_info:
                      if str(spell_action["level"]) not in self._spell_slots:
                        self._spell_slots[str(spell_action["level"])] = 1
                      else:
                        self._spell_slots[str(spell_action["level"])] += 1
          else:
            self._spellcasing = False
                
        print("MONSTER ACTIONS:")
        for action in self._actions:
           print(action)

    def use_action(self):
        action_weights = []
        consider_healing = False
        i = 0
        for action in self._actions:
            print(action["name"])
            action_type = action["type"].split("#")

            if action_type[1] == "spell":
                print("SPELL SLOTS:", self._remaining_spell_slots)
                if self._remaining_spell_slots[str(action["level"])] == 0:
                    print("No slots, weight = 0")
                    action_weights.append(0.0)
                    continue

            # if action_type[0] in ["heal"]:
            #     _, max_status = self._party.check_party_health()

            #     # If someoneis below half HP, we consider healing.
            #     if max_status > 1:
            #         max_heal = action["heal_dice"] + self._modifiers[action["heal_bonus"]]
            #         action_weights.append(math.pow(max_heal, 3)*max_status)
            #     else:
            #         action_weights.append(0.0)
            

            if action_type[0] == "dc":
                print("DC action")
                max_dmg = sum([int(dmg_roll["count"]) * int(dmg_roll["dmg_dice"]) for dmg_roll in action["dmg_rolls"]])
                if action_type[1] == "spell":
                    action_weights.append(math.pow(max_dmg, 2) * (self._since_last_spell/10))
                else:
                    action_weights.append(math.pow(max_dmg, 2))

            elif action_type[0] == "attack":
                print("attack action")
                max_dmg = 0
                for attack in action["attacks"]:
                    max_dmg += sum([int(dmg_roll["count"]) * int(dmg_roll["dmg_dice"]) for dmg_roll in attack["sources"]])
                if action_type[1] == "spell":
                    action_weights.append(math.pow(max_dmg, 2) * (self._since_last_spell/10))
                else:
                    action_weights.append(math.pow(max_dmg, 2)) 

            else:
                action_weights.append(0.0)

            # print("ACTION:")
            # print(action)
            # print(action_weights[i])

            i += 1
            print(action_weights)

        print("\nMONSTER ACTIONS:")
        for action in self._actions:
          print(action["name"])

        print("\nACTION WEIGHTS:")
        for weight in action_weights:
          print(weight)

        for j, action in enumerate(self._actions):
          print(action)
          print(action_weights[j])

        total = sum(action_weights)
        action_weights_norm = []
        for weight in action_weights:
            action_weights_norm.append(weight / total)

        action = random.choices(population=self._actions, weights=action_weights_norm)[0]

        print(f"CHOSEN ACTION: {action["name"]}")
        
        action_type = action["type"].split("#")

        if action_type[1] == "spell":
          self._since_last_spell = 0
          self._remaining_spell_slots[str(action["level"])] -= 1
        elif self._spellcasting == True:
          self._since_last_spell += 1
                
        if action_type[0] == "attack":
            attacks = []
            for attack in action["attacks"]:

              attack_roll = (
                  random.randint(1, 20) + attack["attack_bonus"]
              )

              dmg_rolls = []
              for dmg_roll in attack["sources"]:
                print(f"dmg_roll[dmg_dice]: {dmg_roll['dmg_dice']}")
                dmg_rolls.append({
                  "dmg_roll": dmg_roll["count"] * (random.randint(1, int(dmg_roll["dmg_dice"])) + int(dmg_roll["dmg_bonus"])),
                  "dmg_type": dmg_roll["dmg_type"]
                })

              attacks.append({"attack_roll": attack_roll, "dmg_roll": dmg_rolls})
            
            action_used = {
                "name": action["name"],
                "type": "attack",
                "target_type": action["target_type"],
                "attacks": attacks
            }
            if action["target_type"] == "creature_amount":
                action_used["amount_creatures"] = action["amount_creatures"]
            elif action["target_type"] == "aoe":
                action_used["raduis"] = action["radius"]
            
            
            return action_used
        
        elif action_type[0] == "dc":
            dmg_rolls = [ {"dmg": sum([random.randint(1, int(dmg_roll["dmg_dice"])) for _ in range(int(dmg_roll["count"]))]), "dmg_type": dmg_roll["dmg_type"]} for dmg_roll in action["dmg_rolls"]]

            action_used = {
                "name": action["name"],
                "type": "dc",
                "target_type": action["target_type"],
                "st": action["st"],
                "dc": self._spellcasting_dc,
                "half": action["half"],
                "dmg_rolls": dmg_rolls
            }
            if action["target_type"] == "creature_amount":
                action_used["amount_creatures"] = action["amount_creatures"]
            elif action["target_type"] == "aoe":
                action_used["raduis"] = action["radius"]

            return action_used
        
    def get_total_dmg(self, dmg_rolls):
      total_dmg = 0
      for dmg_roll in dmg_rolls:
        if dmg_roll["dmg_type"] in self._dmg_vulnerabilities:
          dmg = 2 * dmg_roll["dmg"]
          total_dmg += dmg
        elif dmg_roll["dmg_type"] in self._dmg_resistances:
          dmg = math.floor(dmg_roll["dmg"] / 2)
          total_dmg += dmg
        else:
          dmg = dmg_roll["dmg"]
          total_dmg += dmg
      return total_dmg

    def receive_action(self, action):
        action_type = action["type"].split("#")
        if action_type[0] == "attack":
            received_attacks = []
            for attack in action["attacks"]:
              if attack["attack_roll"] >= self._ac:
                  if self._status == "death_saves":
                      self._death_saves["failures"] += 2
                  elif self._status == "conscious":
                      total_dmg = self.get_total_dmg(attack["dmg_rolls"])
                      self._hp -= total_dmg
                      received_attacks.append({
                          "status": "hit",
                          "AC": self._ac,
                          "dmg": total_dmg,
                          "max_HP": self._hp_max,
                          "HP": self._hp,
                      })
              else:
                  received_attacks.append({
                      "status": "miss",
                      "AC": self._ac,
                      "dmg": 0,
                      "max_HP": self._hp_max,
                      "HP": self._hp,
                  })
            
            received_action = {
                "name": action["name"],
                "type": "attack",
                "received_attacks": received_attacks
            }
            
        elif action_type[0] == "dc":
          st_roll = random.randint(1, 20) + self._modifiers[action["st"]]
          if st_roll < action["dc"]:
            total_dmg = self.get_total_dmg(action["dmg_rolls"])
            self._hp -= total_dmg
            st_result = "failed"
          elif action["half"] == True:
            total_dmg = math.floor(self.get_total_dmg(action["dmg_rolls"]) / 2)
            self._hp -= total_dmg
            st_result = "succeed"
          else:
            total_dmg = 0
            st_result = "succeed"

          received_action = {
                    "name": action["name"],
                    "type": "dc",
                    "status": st_result,
                    "half": action["half"],
                    "st": action["st"],
                    "st_roll": st_roll,
                    "dmg": total_dmg,
                    "max_HP": self._hp_max,
                    "HP": self._hp,
                  }
        self.check_status()
        return received_action
               
    def check_status(self):
        if self._hp <= 0 and self._status == "conscious":
            self._status = "dead"
            