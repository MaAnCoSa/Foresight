from PC import PC
from Monster import Monster
from Party import Party
from MonsterGroup import MonsterGroup
from Combat import Combat
import json
import pandas as pd
from Combats_Dataset import Combats_Dataset
import random
import itertools

def __main__(verbose = 0):
    if verbose >= 1:
        print("GEN_DATA!!!\n")

    with open("../data/external/monsters.json", "r") as file:
        monsters_data = json.load(file)

    with open("../data/external/spells.json", "r") as file:
        spells_data = json.load(file)

    results = []

    combats_dataset = Combats_Dataset()

    crs = [0.125, 0.25, 0.5] + [i+1 for i in range(1, 30)]

    # cr = 10
    # pc_lvl = 5
    # num_pcs = 3
    # i = 0

    monster_exceptions = [
        "Rug of Smothering",
        "Hydra",
        "Vampire, Mist Form"
    ]

    for _ in range(80000):
        # Choosing random monsters
        num_monsters = random.randint(1,7)
        monsters_to_use = []

        # TODO: After considering more PC lvls, we can consider bigger CR for monsters.
        base_cr_idx = random.randint(0, 5) #len(crs)-1)
        min_cr_idx = base_cr_idx - 3
        if min_cr_idx < 0:
            min_cr_idx = 0
        max_cr_idx = base_cr_idx + 3
        if max_cr_idx > 12:
            max_cr_idx = 12
        
        cr_range = range(min_cr_idx, max_cr_idx)

        i = 0
        while i < num_monsters:
            monster_cr_idx = random.choice(cr_range)
            monster_cr = crs[monster_cr_idx]
            possible_monsters = monsters_data[str(monster_cr)]
            if len(possible_monsters) == 0:
                continue
            monster = possible_monsters[random.randint(0,len(possible_monsters)-1)]

            if monster["name"] not in monster_exceptions:
                monsters_to_use.append(monster)
                i += 1
            
        # Choosing random lvl for PCs
        pc_lvl = random.randint(1, 5)

        # Choosing random number of PCs
        num_pcs = random.randint(1,7)

        # Choosing random classes for those PCs
        clases = []
        for _ in range(num_pcs):
            clases.append(random.choice(
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
            ))

        # We repeat the encounter 10 times to consider variations
        for _ in range(10):
            # We create the PCs
            pcs = []
            for pc in range(num_pcs):
                pcs.append(PC(pc_lvl, clases[pc]))

            # We create the Monsters
            monsters = []
            for monster in monsters_to_use:
                monsters.append(Monster(monster, spells_data))

            # We create the Party and the Monster Group
            party = Party(pcs)
            monsterGroup = MonsterGroup(monsters)

            # We print the Party and Monster Group information (if asked to)
            if verbose >= 1:
                print("Party:")
                for pc in party._pcs:
                    print("\t",pc._class, pc._initiative)
                print("")
                print("Monster Group:")
                for monster in monsterGroup._monsters:
                    print("\t",monster._name, monster._initiative)
                print("")

            # We create the combat object
            combat = Combat(party, monsterGroup)

            # We print the turn order (if asked to)
            if verbose >= 1:
                print("Turns:")
                for turn in combat._turn_order:
                    if turn["combatant"]._type == "player":
                        print("\t", turn, turn["combatant"]._type, turn["combatant"]._class)
                    else:
                        print("\t", turn, turn["combatant"]._type, turn["combatant"]._name)
                print("")
            
            # We run the combat
            winner = combat.combat(verbose)

            # We calculate the conscuousness and health ratios
            total_players = len(party._pcs)
            not_conscious_players = sum([1 if pc._status != "conscious" else 0 for pc in party._pcs])
            not_conscious_players_ratio = not_conscious_players / total_players

            total_party_hp = sum([pc._hp_max for pc in party._pcs])
            remaining_party_hp = sum([pc._hp for pc in party._pcs])
            party_hp_ratio = remaining_party_hp / total_party_hp

            total_monsters_hp = sum([monster._hp_max for monster in monsterGroup._monsters])
            remaining_monsters_hp = sum([monster._hp for monster in monsterGroup._monsters])
            monsters_hp_ratio = remaining_monsters_hp / total_monsters_hp

            if winner == "party" and party_hp_ratio == 1.0:
                difficulty = 0          # Trivial
            elif winner == "party" and party_hp_ratio >= 0.75:
                difficulty = 1          # Very Easy
            elif winner == "party" and party_hp_ratio >= 0.5:
                difficulty = 2          # Easy
            elif winner == "party" and party_hp_ratio >= 0.25:
                difficulty = 3          # Medium
            elif winner == "party" and party_hp_ratio >= 0:
                difficulty = 4          # Hard
            elif winner == "monsters" and monsters_hp_ratio < 0.25:
                difficulty = 5          # Deadly
            elif winner == "monsters" and monsters_hp_ratio < 0.5:
                difficulty = 6
            elif winner == "monsters" and monsters_hp_ratio < 0.75:
                difficulty = 7
            elif winner == "monsters" and monsters_hp_ratio < 1.0:
                difficulty = 8
            elif winner == "monsters" and monsters_hp_ratio == 1.0:
                difficulty = 9

            # We label the combat's difficulty by its result:
            # if not_conscious_players_ratio == 1:
            #     difficulty = 9          # Definitively Deadly
            # elif not_conscious_players_ratio > (2/3):
            #     difficulty = 8          # Extremely Deadly
            # elif not_conscious_players_ratio > (1/3):
            #     difficulty = 7          # Very Deadly
            # elif not_conscious_players_ratio > 0:
            #     difficulty = 6          # Deadly
            # elif party_hp_ratio < 0.2:
            #     difficulty = 5          # Hard
            # elif party_hp_ratio < 0.4:
            #     difficulty = 4          # Medium
            # elif party_hp_ratio < 0.6:
            #     difficulty = 3          # Easy
            # elif party_hp_ratio < 0.8:
            #     difficulty = 2          # Very Easy
            # elif party_hp_ratio < 1:
            #     difficulty = 1          # Extremely Easy
            # else:
            #     difficulty = 0          # Trivial

            # We create the combat's information to append to our list of results.
            combats_dataset.add_combat_result({
                "pc1_class": party._pcs[0]._class._name,
                "pc1_level": party._pcs[0]._level,
                "pc1_hp_max": party._pcs[0]._hp_max,
                "pc1_ac": party._pcs[0]._ac,
                "pc1_STR": party._pcs[0]._modifiers["STR"],
                "pc1_DEX": party._pcs[0]._modifiers["DEX"],
                "pc1_CON": party._pcs[0]._modifiers["CON"],
                "pc1_INT": party._pcs[0]._modifiers["INT"],
                "pc1_WIS": party._pcs[0]._modifiers["WIS"],
                "pc1_CHA": party._pcs[0]._modifiers["CHA"],

                "pc2_class": party._pcs[1]._class._name if len(party._pcs) > 1 else "-",
                "pc2_level": party._pcs[1]._level if len(party._pcs) > 1 else 0,
                "pc2_hp_max": party._pcs[1]._hp_max if len(party._pcs) > 1 else 0,
                "pc2_ac": party._pcs[1]._ac if len(party._pcs) > 1 else 0,
                "pc2_STR": party._pcs[1]._modifiers["STR"] if len(party._pcs) > 1 else 0,
                "pc2_DEX": party._pcs[1]._modifiers["DEX"] if len(party._pcs) > 1 else 0,
                "pc2_CON": party._pcs[1]._modifiers["CON"] if len(party._pcs) > 1 else 0,
                "pc2_INT": party._pcs[1]._modifiers["INT"] if len(party._pcs) > 1 else 0,
                "pc2_WIS": party._pcs[1]._modifiers["WIS"] if len(party._pcs) > 1 else 0,
                "pc2_CHA": party._pcs[1]._modifiers["CHA"] if len(party._pcs) > 1 else 0,

                "pc3_class": party._pcs[2]._class._name if len(party._pcs) > 2 else "-",
                "pc3_level": party._pcs[2]._level if len(party._pcs) > 2 else 0,
                "pc3_hp_max": party._pcs[2]._hp_max if len(party._pcs) > 2 else 0,
                "pc3_ac": party._pcs[2]._ac if len(party._pcs) > 2 else 0,
                "pc3_STR": party._pcs[2]._modifiers["STR"] if len(party._pcs) > 2 else 0,
                "pc3_DEX": party._pcs[2]._modifiers["DEX"] if len(party._pcs) > 2 else 0,
                "pc3_CON": party._pcs[2]._modifiers["CON"] if len(party._pcs) > 2 else 0,
                "pc3_INT": party._pcs[2]._modifiers["INT"] if len(party._pcs) > 2 else 0,
                "pc3_WIS": party._pcs[2]._modifiers["WIS"] if len(party._pcs) > 2 else 0,
                "pc3_CHA": party._pcs[2]._modifiers["CHA"] if len(party._pcs) > 2 else 0,

                "pc4_class": party._pcs[3]._class._name if len(party._pcs) > 3 else "-",
                "pc4_level": party._pcs[3]._level if len(party._pcs) > 3 else 0,
                "pc4_hp_max": party._pcs[3]._hp_max if len(party._pcs) > 3 else 0,
                "pc4_ac": party._pcs[3]._ac if len(party._pcs) > 3 else 0,
                "pc4_STR": party._pcs[3]._modifiers["STR"] if len(party._pcs) > 3 else 0,
                "pc4_DEX": party._pcs[3]._modifiers["DEX"] if len(party._pcs) > 3 else 0,
                "pc4_CON": party._pcs[3]._modifiers["CON"] if len(party._pcs) > 3 else 0,
                "pc4_INT": party._pcs[3]._modifiers["INT"] if len(party._pcs) > 3 else 0,
                "pc4_WIS": party._pcs[3]._modifiers["WIS"] if len(party._pcs) > 3 else 0,
                "pc4_CHA": party._pcs[3]._modifiers["CHA"] if len(party._pcs) > 3 else 0,

                "pc5_class": party._pcs[4]._class._name if len(party._pcs) > 4 else "-",
                "pc5_level": party._pcs[4]._level if len(party._pcs) > 4 else 0,
                "pc5_hp_max": party._pcs[4]._hp_max if len(party._pcs) > 4 else 0,
                "pc5_ac": party._pcs[4]._ac if len(party._pcs) > 4 else 0,
                "pc5_STR": party._pcs[4]._modifiers["STR"] if len(party._pcs) > 4 else 0,
                "pc5_DEX": party._pcs[4]._modifiers["DEX"] if len(party._pcs) > 4 else 0,
                "pc5_CON": party._pcs[4]._modifiers["CON"] if len(party._pcs) > 4 else 0,
                "pc5_INT": party._pcs[4]._modifiers["INT"] if len(party._pcs) > 4 else 0,
                "pc5_WIS": party._pcs[4]._modifiers["WIS"] if len(party._pcs) > 4 else 0,
                "pc5_CHA": party._pcs[4]._modifiers["CHA"] if len(party._pcs) > 4 else 0,
                
                "pc6_class": party._pcs[5]._class._name if len(party._pcs) > 5 else "-",
                "pc6_level": party._pcs[5]._level if len(party._pcs) > 5 else 0,
                "pc6_hp_max": party._pcs[5]._hp_max if len(party._pcs) > 5 else 0,
                "pc6_ac": party._pcs[5]._ac if len(party._pcs) > 5 else 0,
                "pc6_STR": party._pcs[5]._modifiers["STR"] if len(party._pcs) > 5 else 0,
                "pc6_DEX": party._pcs[5]._modifiers["DEX"] if len(party._pcs) > 5 else 0,
                "pc6_CON": party._pcs[5]._modifiers["CON"] if len(party._pcs) > 5 else 0,
                "pc6_INT": party._pcs[5]._modifiers["INT"] if len(party._pcs) > 5 else 0,
                "pc6_WIS": party._pcs[5]._modifiers["WIS"] if len(party._pcs) > 5 else 0,
                "pc6_CHA": party._pcs[5]._modifiers["CHA"] if len(party._pcs) > 5 else 0,

                "pc7_class": party._pcs[6]._class._name if len(party._pcs) > 6 else "-",
                "pc7_level": party._pcs[6]._level if len(party._pcs) > 6 else 0,
                "pc7_hp_max": party._pcs[6]._hp_max if len(party._pcs) > 6 else 0,
                "pc7_ac": party._pcs[6]._ac if len(party._pcs) > 6 else 0,
                "pc7_STR": party._pcs[6]._modifiers["STR"] if len(party._pcs) > 6 else 0,
                "pc7_DEX": party._pcs[6]._modifiers["DEX"] if len(party._pcs) > 6 else 0,
                "pc7_CON": party._pcs[6]._modifiers["CON"] if len(party._pcs) > 6 else 0,
                "pc7_INT": party._pcs[6]._modifiers["INT"] if len(party._pcs) > 6 else 0,
                "pc7_WIS": party._pcs[6]._modifiers["WIS"] if len(party._pcs) > 6 else 0,
                "pc7_CHA": party._pcs[6]._modifiers["CHA"] if len(party._pcs) > 6 else 0,

                "monster1_name": monsterGroup._monsters[0]._name,
                "monster1_cr": monsterGroup._monsters[0]._challenge_rating,
                "monster1_hp_max": monsterGroup._monsters[0]._hp_max,
                "monster1_ac": monsterGroup._monsters[0]._ac,
                "monster1_STR": monsterGroup._monsters[0]._modifiers["STR"],
                "monster1_DEX": monsterGroup._monsters[0]._modifiers["DEX"],
                "monster1_CON": monsterGroup._monsters[0]._modifiers["CON"],
                "monster1_INT": monsterGroup._monsters[0]._modifiers["INT"],
                "monster1_WIS": monsterGroup._monsters[0]._modifiers["WIS"],
                "monster1_CHA": monsterGroup._monsters[0]._modifiers["CHA"],

                "monster2_name": monsterGroup._monsters[1]._name if len(monsterGroup._monsters) > 1 else "-",
                "monster2_cr": monsterGroup._monsters[1]._challenge_rating if len(monsterGroup._monsters) > 1 else 0,
                "monster2_hp_max": monsterGroup._monsters[1]._hp_max if len(monsterGroup._monsters) > 1 else 0,
                "monster2_ac": monsterGroup._monsters[1]._ac if len(monsterGroup._monsters) > 1 else 0,
                "monster2_STR": monsterGroup._monsters[1]._modifiers["STR"] if len(monsterGroup._monsters) > 1 else 0,
                "monster2_DEX": monsterGroup._monsters[1]._modifiers["DEX"] if len(monsterGroup._monsters) > 1 else 0,
                "monster2_CON": monsterGroup._monsters[1]._modifiers["CON"] if len(monsterGroup._monsters) > 1 else 0,
                "monster2_INT": monsterGroup._monsters[1]._modifiers["INT"] if len(monsterGroup._monsters) > 1 else 0,
                "monster2_WIS": monsterGroup._monsters[1]._modifiers["WIS"] if len(monsterGroup._monsters) > 1 else 0,
                "monster2_CHA": monsterGroup._monsters[1]._modifiers["CHA"] if len(monsterGroup._monsters) > 1 else 0,

                "monster3_name": monsterGroup._monsters[2]._name if len(monsterGroup._monsters) > 2 else "-",
                "monster3_cr": monsterGroup._monsters[2]._challenge_rating if len(monsterGroup._monsters) > 2 else 0,
                "monster3_hp_max": monsterGroup._monsters[2]._hp_max if len(monsterGroup._monsters) > 2 else 0,
                "monster3_ac": monsterGroup._monsters[2]._ac if len(monsterGroup._monsters) > 2 else 0,
                "monster3_STR": monsterGroup._monsters[2]._modifiers["STR"] if len(monsterGroup._monsters) > 2 else 0,
                "monster3_DEX": monsterGroup._monsters[2]._modifiers["DEX"] if len(monsterGroup._monsters) > 2 else 0,
                "monster3_CON": monsterGroup._monsters[2]._modifiers["CON"] if len(monsterGroup._monsters) > 2 else 0,
                "monster3_INT": monsterGroup._monsters[2]._modifiers["INT"] if len(monsterGroup._monsters) > 2 else 0,
                "monster3_WIS": monsterGroup._monsters[2]._modifiers["WIS"] if len(monsterGroup._monsters) > 2 else 0,
                "monster3_CHA": monsterGroup._monsters[2]._modifiers["CHA"] if len(monsterGroup._monsters) > 2 else 0,

                "monster4_name": monsterGroup._monsters[3]._name if len(monsterGroup._monsters) > 3 else "-",
                "monster4_cr": monsterGroup._monsters[3]._challenge_rating if len(monsterGroup._monsters) > 3 else 0,
                "monster4_hp_max": monsterGroup._monsters[3]._hp_max if len(monsterGroup._monsters) > 3 else 0,
                "monster4_ac": monsterGroup._monsters[3]._ac if len(monsterGroup._monsters) > 3 else 0,
                "monster4_STR": monsterGroup._monsters[3]._modifiers["STR"] if len(monsterGroup._monsters) > 3 else 0,
                "monster4_DEX": monsterGroup._monsters[3]._modifiers["DEX"] if len(monsterGroup._monsters) > 3 else 0,
                "monster4_CON": monsterGroup._monsters[3]._modifiers["CON"] if len(monsterGroup._monsters) > 3 else 0,
                "monster4_INT": monsterGroup._monsters[3]._modifiers["INT"] if len(monsterGroup._monsters) > 3 else 0,
                "monster4_WIS": monsterGroup._monsters[3]._modifiers["WIS"] if len(monsterGroup._monsters) > 3 else 0,
                "monster4_CHA": monsterGroup._monsters[3]._modifiers["CHA"] if len(monsterGroup._monsters) > 3 else 0,

                "monster5_name": monsterGroup._monsters[4]._name if len(monsterGroup._monsters) > 4 else "-",
                "monster5_cr": monsterGroup._monsters[4]._challenge_rating if len(monsterGroup._monsters) > 4 else 0,
                "monster5_hp_max": monsterGroup._monsters[4]._hp_max if len(monsterGroup._monsters) > 4 else 0,
                "monster5_ac": monsterGroup._monsters[4]._ac if len(monsterGroup._monsters) > 4 else 0,
                "monster5_STR": monsterGroup._monsters[4]._modifiers["STR"] if len(monsterGroup._monsters) > 4 else 0,
                "monster5_DEX": monsterGroup._monsters[4]._modifiers["DEX"] if len(monsterGroup._monsters) > 4 else 0,
                "monster5_CON": monsterGroup._monsters[4]._modifiers["CON"] if len(monsterGroup._monsters) > 4 else 0,
                "monster5_INT": monsterGroup._monsters[4]._modifiers["INT"] if len(monsterGroup._monsters) > 4 else 0,
                "monster5_WIS": monsterGroup._monsters[4]._modifiers["WIS"] if len(monsterGroup._monsters) > 4 else 0,
                "monster5_CHA": monsterGroup._monsters[4]._modifiers["CHA"] if len(monsterGroup._monsters) > 4 else 0,

                "monster6_name": monsterGroup._monsters[5]._name if len(monsterGroup._monsters) > 5 else "-",
                "monster6_cr": monsterGroup._monsters[5]._challenge_rating if len(monsterGroup._monsters) > 5 else 0,
                "monster6_hp_max": monsterGroup._monsters[5]._hp_max if len(monsterGroup._monsters) > 5 else 0,
                "monster6_ac": monsterGroup._monsters[5]._ac if len(monsterGroup._monsters) > 5 else 0,
                "monster6_STR": monsterGroup._monsters[5]._modifiers["STR"] if len(monsterGroup._monsters) > 5 else 0,
                "monster6_DEX": monsterGroup._monsters[5]._modifiers["DEX"] if len(monsterGroup._monsters) > 5 else 0,
                "monster6_CON": monsterGroup._monsters[5]._modifiers["CON"] if len(monsterGroup._monsters) > 5 else 0,
                "monster6_INT": monsterGroup._monsters[5]._modifiers["INT"] if len(monsterGroup._monsters) > 5 else 0,
                "monster6_WIS": monsterGroup._monsters[5]._modifiers["WIS"] if len(monsterGroup._monsters) > 5 else 0,
                "monster6_CHA": monsterGroup._monsters[5]._modifiers["CHA"] if len(monsterGroup._monsters) > 5 else 0,

                "monster7_name": monsterGroup._monsters[6]._name if len(monsterGroup._monsters) > 6 else "-",
                "monster7_cr": monsterGroup._monsters[6]._challenge_rating if len(monsterGroup._monsters) > 6 else 0,
                "monster7_hp_max": monsterGroup._monsters[6]._hp_max if len(monsterGroup._monsters) > 6 else 0,
                "monster7_ac": monsterGroup._monsters[6]._ac if len(monsterGroup._monsters) > 6 else 0,
                "monster7_STR": monsterGroup._monsters[6]._modifiers["STR"] if len(monsterGroup._monsters) > 6 else 0,
                "monster7_DEX": monsterGroup._monsters[6]._modifiers["DEX"] if len(monsterGroup._monsters) > 6 else 0,
                "monster7_CON": monsterGroup._monsters[6]._modifiers["CON"] if len(monsterGroup._monsters) > 6 else 0,
                "monster7_INT": monsterGroup._monsters[6]._modifiers["INT"] if len(monsterGroup._monsters) > 6 else 0,
                "monster7_WIS": monsterGroup._monsters[6]._modifiers["WIS"] if len(monsterGroup._monsters) > 6 else 0,
                "monster7_CHA": monsterGroup._monsters[6]._modifiers["CHA"] if len(monsterGroup._monsters) > 6 else 0,

                "winner": winner,

                "not_conscious_players_ratio": not_conscious_players_ratio,
                "party_hp_ratio": party_hp_ratio,

                "difficulty": difficulty 
            })

    # After running all combats, we create a DataFrame with all the results.
    combats_df = combats_dataset.create_dataframe()
    # print("")
    # print(combats_df)

    # We save the DataFrame as a CSV.
    combats_df.to_csv("../data/raw/combat_results_lvl_5.csv")


__main__(verbose=0)