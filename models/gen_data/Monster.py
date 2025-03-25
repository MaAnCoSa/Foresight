import random
import math

class Monster:
    def __init__(self, monster_data):
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
        self._dmg_immunities = monster_data['condition_immunities']

        self._actions = []
        multiattack_actions = []
        for original_action in monster_data["actions"]:
          #print("OG Action:\t" + str(original_action))
          if original_action["name"] not in multiattack_actions:
            if original_action["name"] == "Multiattack":
              #print("MULTIATTACK")

              attacks = []
              for multi_act in original_action["actions"]:
                #print("Multi act: " + str(multi_act))

                for act in monster_data["actions"]:
                  #print("\t" + str(act))
                  if act["name"] == multi_act["action_name"] and act["name"] != "Multiattack" and multi_act["type"] != "ability":
                    #print("FOUND:\t" + str(act))

                    for count in range(multi_act["count"]):
                      attack = {
                          "attack_bonus": act["attack_bonus"],
                          "sources": []
                      }
                      for source in act['damage']:
                        if 'choose' not in source:
                          dmg = source["damage_dice"].split("+")
                          attack["sources"].append({
                              "dmg_type": source["damage_type"]["name"],
                              "dmg_dice": dmg[0].split("d")[1],
                              "dmg_bonus": dmg[1]
                          })
                      multiattack_actions.append(act["name"])
                      attacks.append(attack)
              action = {
                "name": original_action["name"],
                "type": "attack",
                "attacks": attacks
              }
              #self._actions.append(action)
            elif "usage" in original_action:
              action = {
                "name": original_action["name"],
                "type": "attack",
                "attack_type": "usage"
              }
            elif "dc" in original_action:
              action = {
                "name": original_action["name"],
                "type": "dc",
                "dc_stat": original_action["dc"]["dc_type"]["name"],
                "dc_value": original_action["dc"]["dc_value"]
              }

            else:
              action = {
                  "name": original_action["name"],
                  "type": "attack",
                  "attacks": [{
                    "attack_bonus": original_action["attack_bonus"],
                    "sources": []
                  }]
                }
              for source in original_action['damage']:
                if 'choose' not in source:
                  dmg = source["damage_dice"].split("+")
                  action["attacks"][0]["sources"].append({
                      "dmg_type": source["damage_type"]["name"],
                      "dmg_dice": dmg[0].split("d")[1],
                      "dmg_bonus": dmg[1]
                  })
              self._actions.append(action)
            
            #self._actions.append(action)
           
    def use_action(self, action):
        if action["type"] == "attack":
            attacks = []
            for attack in action["attacks"]:

              attack_roll = (
                  random.randint(1, 20)
                  + attack["attack_bonus"]
              )

              dmg_rolls = []
              for source in attack["sources"]:
                dmg_rolls.append({
                    "dmg_roll": random.randint(1, int(source["dmg_dice"])) + int(source["dmg_bonus"]),
                    "dmg_type": source["dmg_type"]
                })

              attacks.append({"attack_roll": attack_roll, "dmg_roll": dmg_rolls})
            return {"type": "attack", "attacks": attacks}

    def receive_action(self, action):
        action_type = action["type"].split("#")
        if action_type[0] == "attack":
            if action["attack_roll"] >= self._ac:
                if self._status == "death_saves":
                    self._death_saves["failures"] += 2
                elif self._status == "conscious":
                    self._hp -= action["dmg_roll"]
                    self.check_status()
                    return {
                        "type": "attack",
                        "status": "hit",
                        "AC": self._ac,
                        "dmg": action["dmg_roll"],
                        "max_HP": self._hp_max,
                        "HP": self._hp,
                    }
            else:
                return {
                    "type": "attack",
                    "status": "miss",
                    "AC": self._ac,
                    "dmg": 0,
                    "max_HP": self._hp_max,
                    "HP": self._hp,
                }
            
        elif action_type[0] == "dc":
          st_roll = random.randint(1, 20) + self._modifiers[action["st"]]
          if st_roll < action["dc"]:
            self._hp -= action["dmg_roll"]
            st_result = "failed"
          elif action["half"] == True:
            self._hp -= math.floor(action["dmg_roll"] / 2)
            st_result = "succeed"
          else:
            st_result = "succeed"

          return {
                    "type": "dc",
                    "status": st_result,
                    "half": action["half"],
                    "st": action["st"],
                    "st_roll": st_roll,
                    "dmg": action["dmg_roll"],
                    "max_HP": self._hp_max,
                    "HP": self._hp,
                  }
               
    def check_status(self):
        if self._hp <= 0 and self._status == "conscious":
            self._status = "dead"
            