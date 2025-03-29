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

class PC:
    def __init__(self):
        self._type = "player"
        self._level = 1
        self._stats = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}
        self._modifiers = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}
        
        self._status = "conscious"
        
        self._prof_bonus = 2
        
        cha_class = random.choice(
            [
                "BARD",
                # "BARBARIAN",
                # "CLERIC",
                # "DRUID",
                # "FIGHTER_STR",
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
            
        self._hp_max = int(self._class._hit_die) + int(self._modifiers["CON"])
        self._hp = self._hp_max
        self._ac = 10 + self._modifiers["DEX"]
        self._initiative = self._modifiers["DEX"]

        scores = sorted([random.randint(8, 18) for i in range(6)], reverse=True)
        for i in range(len(scores)):
            stat = self._class._priority_stats[i]
            self._stats[stat] = scores[i]
            self._modifiers[stat] = math.floor((self._stats[stat] - 10) / 2)

        self._death_saves = {"successes": 0, "failures": 0}
        
        
        if self._class._name == "Barbarian":
            self._ac += self._modifiers["CON"] # Unarmored Defense
        if self._class._name == "Bard":
            self._ac += 1 # Leather armor
            self._spell_dc = 8 + self._prof_bonus + self._modifiers["CHA"]
            self._spell_attack_bonus = self._prof_bonus + self._modifiers["CHA"]
            self._since_last_spell = 5

    def set_party(self, party):
        self._party = party

    def use_action(self):
        action_weights = []
        consider_healing = False
        i = 0
        for action in self._class._actions[self._level]:
            action_type = action["type"].split("#")

            if action_type[1] == "spell":
                print("SPELL SLOTS:", self._remaining_spell_slots)
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

            print("ACTION:")
            print(action)
            print(action_weights[i])

            i += 1

        total = sum(action_weights)
        action_weights_norm = []
        for weight in action_weights:
            action_weights_norm.append(weight / total)

        action = random.choices(population=self._class._actions[self._level], weights=action_weights_norm)[0]

        print(f"CHOSEN ACTION: {action["name"]}")
        
        action_type = action["type"].split("#")

        if action_type[1] == "spell":
            self._since_last_spell = 1
            self._remaining_spell_slots[action["spell_level"] - 1] -= 1
            if self._class in ["Bard", "cleric", "Druid", "Paladin", "Ranger", "Sorcerer"]:
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

                attack_roll = (
                    random.randint(1, 20)
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

    def receive_action(self, action):
        if action["type"] == "attack":
            received_attacks = []
            for attack in action["attacks"]:
                
                if attack["attack_roll"] >= self._ac:
                    if self._status == "death_saves":
                        self._death_saves["failures"] += 2
                    elif self._status == "conscious":
                        dmg = 0
                        for dmg_roll in attack["dmg_roll"]:
                            self._hp -= dmg_roll["dmg_roll"]
                            dmg += dmg_roll["dmg_roll"]
                            self.check_status()
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
            
            return {
                "name": action["name"],
                "type": "attack",
                "received_attacks": received_attacks
            }

        elif action["type"] == "heal":
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
        if self._death_saves["successes"] == 3:
            self._death_saves = {
                "successes": 0,
                "failures": 0
            }
            self._status = "unconscious"
            self._hp = 0
            
        if self._death_saves["failures"] == 3:
            self._status = "dead"