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
                "BARBARIAN",
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


    def use_action(self):
        action_weights = []
        for action in self._class._actions[self._level]:
            action_type = action["type"].split("#")

            max_dmg = sum([dmg_roll["count"] * dmg_roll["dmg_roll"] for dmg_roll in action["dmg_rolls"]])

            if action_type[0] in ["attack", "dc"]:
                action_weights.append(math.exp(max_dmg))
                

        total = sum(action_weights)
        action_weights_norm = []
        for weight in action_weights:
            action_weights_norm.append(weight / total)

        action = random.choices(population=self._class._actions[self._level], weights=action_weights_norm)[0]

        action_type = action["type"].split("#")

        if action_type[0] == "attack":
            attack_stat = action["attack_stat"]
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

            dmg_rolls = [ {"dmg": sum([random.randint(1,dmg_roll["dmg_roll"] + self._modifiers[attack_stat]) for roll in range(dmg_roll["count"])]), "dmg_type": dmg_roll["dmg_type"]} for dmg_roll in action["dmg_rolls"]]

            # dmg_roll = (
            #     random.randint(1, action["dmg_roll"])
            #     + self._modifiers[attack_stat]
            # )
            
            if self._class._name == "Barbarian" and action_type[1] == "physical":
                dmg_rolls[0]["dmg"] += self._class._rage_bonus[self._level]
            
            return {"type": "attack", "attack_roll": attack_roll, "dmg_rolls": dmg_rolls}
        
        elif action_type[0] == "dc":
            dmg_rolls = [ {"dmg": sum([random.randint(1,dmg_roll["dmg_roll"]) for _ in range(dmg_roll["count"])]), "dmg_type": dmg_roll["dmg_type"]} for dmg_roll in action["dmg_rolls"]]

            return {"type": "dc", "st": action["st"], "dc": self._spell_dc, "half": action["half"], "dmg_rolls": dmg_rolls}

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
            return {"type": "attack", "received_attacks": received_attacks}

    def check_status(self):
        if self._hp <= 0 and self._status == "conscious":
            self._status = "death_saves"
        elif self._hp <= 0 and self._status == "death_saves":
            self.check_death_saves()

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