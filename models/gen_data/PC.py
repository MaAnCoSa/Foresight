import random
from clases import (
    Bard,
    Barbarian,
    Cleric,
    Druid,
    FighterStr,
    FighterDex,
    Monk,
    Paladin,
    Ranger,
    Rogue,
    Sorcerer,
    Wizard,
)
import math
from prettytable import PrettyTable

proficiency_bonus = {
    1: 2,
    2: 2,
    3: 2,
    4: 2,
    5: 3,
    6: 3,
    7: 3,
    8: 3,
    9: 4,
    10: 4,
    11: 4,
    12: 4,
    13: 5,
    14: 5,
    15: 5,
    16: 5,
    17: 6,
    18: 6,
    19: 6,
    20: 6
}

class PC:
    def __init__(self, level):
        self._type = "player"
        self._level = level
        self._stats = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}
        self._modifiers = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}
        
        self._status = "conscious"
        
        self._prof_bonus = proficiency_bonus[self._level]
        
        cha_class = random.choice(
            [
                # "BARD",
                # "BARBARIAN",
                # "CLERIC",
                # "DRUID",
                "FIGHTER_STR",
                # "FIGHTER_DEX",
                # "MONK",
                # "PALADIN",
                # "RANGER",
                # "ROGUE",
                # "SORCERER",
                # "WIZARD",
            ]
        )
        if cha_class == "BARD":
            self._class = Bard()
            self._remaining_spell_slots = self._class._spell_slots[self._level]
        elif cha_class == "BARBARIAN":
            self._class = Barbarian()
        elif cha_class == "CLERIC":
            self._class = Cleric()
        elif cha_class == "DRUID":
            self._class = Druid()
        elif cha_class == "FIGHTER_STR":
            self._class = FighterStr()
        elif cha_class == "FIGHTER_DEX":
            self._class = FighterDex()
        elif cha_class == "MONK":
            self._class = Monk()
        elif cha_class == "PALADIN":
            self._class = Paladin()
        elif cha_class == "RANGER":
            self._class = Ranger()
        elif cha_class == "ROGUE":
            self._class = Rogue()
        elif cha_class == "SORCERER":
            self._class = Sorcerer()
        elif cha_class == "WIZARD":
            self._class = Wizard()
            
        scores = sorted([random.randint(8, 18) for i in range(6)], reverse=True)
        for i in range(len(scores)):
            stat = self._class._priority_stats[i]
            self._stats[stat] = scores[i]
            self._modifiers[stat] = math.floor((self._stats[stat] - 10) / 2)

        if self._level >= 4:
            self.ability_score_increase()
        if self._level >= 8:
            self.ability_score_increase()
        if self._level >= 12:
            self.ability_score_increase()
        if self._level >= 16:
            self.ability_score_increase()
        if self._level >= 19:
            self.ability_score_increase()

        self._hp_max = int(self._class._hit_die) + int(self._modifiers["CON"])
        self._hp = self._hp_max
        self._ac = 10 + self._modifiers["DEX"]
        self._initiative = self._modifiers["DEX"]

        self._dmg_vulnerabilities = []
        self._dmg_resistances = []

        self._death_saves = {"successes": 0, "failures": 0}

        if self._level != 1:
            self.increase_hp()
        
        
        if self._class._name == "Barbarian":
            self._ac += self._modifiers["CON"] # Unarmored Defense
            if self._level >= 2:
                self._class._reckless_attack = True
            self._turns_since_last_reckless = 0
        if self._class._name == "Bard":
            self._ac += 1 # Leather armor
            self._spell_dc = 8 + self._prof_bonus + self._modifiers["CHA"]
            self._spell_attack_bonus = self._prof_bonus + self._modifiers["CHA"]
            self._since_last_spell = 5
        if self._class._name == "FighterStr":
            self._class._action_surges = 0
            self._use_action_surge = False
            self._turns_since_action_surge = 1
            if self._level >= 2:
                self._class._action_surges = 1

    def set_party(self, party):
        self._party = party

    def ability_score_increase(self):
        for increase in range(2):
            increased = False
            for i in range(6):
                stat = self._class._priority_stats[i]
                if self._stats[stat] < 20:
                    self._stats[stat] += 2
                    self._modifiers[stat] = math.floor((self._stats[stat] - 10) / 2)
                    increased = True
                if increased: break

    def increase_hp(self):
        levels_to_increase = self._level - 1
        for i in range(levels_to_increase):
            self._hp_max += random.randint(1, self._class._hit_die) + self._modifiers["CON"]
            self._hp = self._hp_max

    def use_action(self, verbose=0):
        action_weights = []

        # We first consider options from the different classes.
        if self._class._name == "Barbarian":
            p = 4/(self._turns_since_last_reckless+4) # Probability of using recless attack.
            use_reckless = random.choices(population=[True, False], weights=[1-p, p])
                        
        i = 0
        for action in self._class._actions[self._level]:
            action_type = action["type"].split("#")

            if action_type[1] == "spell":
                #print("SPELL SLOTS:", self._remaining_spell_slots)
                if self._remaining_spell_slots[action["spell_level"] - 1] == 0:
                    action_weights.append(0.0)
                    continue

            if action_type[0] in ["heal"]:
                _, max_status = self._party.check_party_health()

                # If someoneis below half HP, we consider healing.
                if max_status > 1:
                    max_heal = action["heal_dice"] + self._modifiers[action["heal_bonus"]]
                    action_weights.append(math.pow(max_heal, 3)*max_status)
                else:
                    action_weights.append(0.0)
            

            elif action_type[0] == "dc":
                max_dmg = sum([dmg_roll["count"] * dmg_roll["dmg_roll"] for dmg_roll in action["dmg_rolls"]])
                if action_type[1] == "spell":
                    action_weights.append(math.pow(max_dmg, 2) * (self._since_last_spell/10))
                else:
                    action_weights.append(math.pow(max_dmg, 2))

            elif action_type[0] == "attack":
                max_dmg = 0
                for attack in action["attacks"]:
                    max_dmg += sum([dmg_roll["count"] * dmg_roll["dmg_roll"] for dmg_roll in attack["dmg_rolls"]])
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

        total = sum(action_weights)
        action_weights_norm = []
        for weight in action_weights:
            action_weights_norm.append(weight / total)

        action = random.choices(population=self._class._actions[self._level], weights=action_weights_norm)[0]

        if verbose >= 2:
            print("\n\tPossible Actions:")
            t = PrettyTable(['Action', 'Weight', 'Weight Norm'])

            for i in range(len(self._class._actions[self._level])):
                t.add_row([
                    self._class._actions[self._level][i]["name"],
                    action_weights[i],
                    round(action_weights_norm[i], 2)])
            for row in t.get_string().split("\n"):
                print (" "*6,row)
            print("")


        #print(f"CHOSEN ACTION: {action["name"]}")
        
        action_type = action["type"].split("#")

        if action_type[1] == "spell":
            self._since_last_spell = 0
            self._remaining_spell_slots[action["spell_level"] - 1] -= 1
        elif self._class in ["Bard", "cleric", "Druid", "Paladin", "Ranger", "Sorcerer"]:
            self._since_last_spell += 1

        if action_type[0] == "attack":
            attacks = []
            for attack in action["attacks"]:
                attack_stat = attack["attack_stat"]
                if attack_stat == "Finesse":
                    if self._modifiers["STR"] > self._modifiers["DEX"]:
                        attack_stat = "STR"
                    else:
                        attack_stat = "DEX"
                
                if self._class._name == "Barbarian":
                    if use_reckless == True:
                        attack_d20 = max([random.randint(1, 20), random.randint(1, 20)])
                        self._turns_since_last_reckless = 0
                    else:
                        attack_d20 = random.randint(1, 20)
                        self._turns_since_last_reckless += 1
                else:
                    attack_d20 = random.randint(1, 20)


                attack_roll = (
                    attack_d20
                    + self._modifiers[attack_stat]
                    + self._prof_bonus
                )

                dmg_rolls = [ {"dmg": sum([random.randint(1,dmg_roll["dmg_roll"] + self._modifiers[attack_stat]) for roll in range(dmg_roll["count"])]), "dmg_type": dmg_roll["dmg_type"]} for dmg_roll in attack["dmg_rolls"]]

                # dmg_roll = (
                #     random.randint(1, action["dmg_roll"])
                #     + self._modifiers[attack_stat]
                # )
                
                if self._class._name == "Barbarian" and action_type[1] == "physical":
                    dmg_rolls[0]["dmg"] += self._class._rage_bonus[self._level]
            
                attacks.append({"attack_roll": attack_roll, "dmg_rolls": dmg_rolls})
            
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
            dmg_rolls = [ {"dmg": sum([random.randint(1,dmg_roll["dmg_roll"]) for _ in range(dmg_roll["count"])]), "dmg_type": dmg_roll["dmg_type"]} for dmg_roll in action["dmg_rolls"]]

            action_used = {
                "name": action["name"],
                "type": "dc",
                "target_type": action["target_type"],
                "st": action["st"],
                "dc": self._spell_dc,
                "half": action["half"],
                "dmg_rolls": dmg_rolls
            }
            if action["target_type"] == "creature_amount":
                action_used["amount_creatures"] = action["amount_creatures"]
            elif action["target_type"] == "aoe":
                action_used["raduis"] = action["radius"]

            return action_used

        elif action_type[0] == "heal":
            if action["heal_bonus"] != None:
                heal_bonus = self._modifiers[action["heal_bonus"]]
            else:
                heal_bonus = 0

            healed_hp = sum([random.randint(1,action["heal_dice"]) for _ in range(action["count"])]) + heal_bonus
            return {
                "name": action["name"],
                "type": "heal",
                "healed_hp": healed_hp,
                "creatures": action["creatures"]
            }
        
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
                        dmg = 0
                        for dmg_roll in attack["dmg_roll"]:
                            self._hp -= int(dmg_roll["dmg_roll"])
                            dmg += int(dmg_roll["dmg_roll"])
                            self.check_status()
                        if self._hp < self._hp_max * (-1):
                            self._status = "dead"
                        received_attacks.append({
                            "type": "attack",
                            "status": "hit",
                            "AC": self._ac,
                            "dmg": dmg,
                            "max_HP": self._hp_max,
                            "HP": self._hp,
                        })
                else:
                    received_attacks.append({
                        "type": "attack",
                        "status": "miss",
                        "AC": self._ac,
                        "dmg": 0,
                        "max_HP": self._hp_max,
                        "HP": self._hp,
                    })
            
            if self._hp < 0: self._hp = 0
            return {
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

        elif action_type[0] == "heal":
            self._hp += action["healed_hp"]
            if self._hp > self._hp_max:
                self._hp = self._hp_max
            self.check_status()
            return {
                "name": action["name"],
                "type": "heal",
                "healed_hp": action["healed_hp"],
                "max_HP": self._hp_max,
                "HP": self._hp,
            }

    def check_status(self):
        if self._hp <= 0 and self._status == "conscious":
            self._status = "death_saves"
        elif self._hp <= 0 and self._status == "death_saves":
            self.check_death_saves()
        elif self._hp > 0 and self._status != "conscious":
            self._status = "conscious"
            self.reset_death_saves()

    def throw_death_save(self):
        death_save = random.randint(1, 20)
        if death_save >= 11:
            self._death_saves["successes"] += 1
            result = "success"
        else:
            self._death_saves["failures"] += 1
            result = "failure"
        self.check_death_saves()
        return {"death_save": death_save, "result": result}
    
    def reset_death_saves(self):
        self._death_saves = {"successes": 0, "failures": 0}

    def check_death_saves(self):
        if self._death_saves["successes"] >= 3:
            self._death_saves = {
                "successes": 0,
                "failures": 0
            }
            self._status = "unconscious"
            self._hp = 0
            
        if self._death_saves["failures"] >= 3:
            self._status = "dead"