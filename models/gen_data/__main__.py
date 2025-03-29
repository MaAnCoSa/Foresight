from PC import PC
from Monster import Monster
from Party import Party
from MonsterGroup import MonsterGroup
from Combat import Combat
import json

def __main__():
    print("GEN_DATA!!!")

    longsword_action = {
      "type": "attack",
      "attack_stat": "STR",
      "dmg_roll": 10
    }

    with open("../data/raw/monsters.json", "r") as file:
        monsters_data = json.load(file)

    # pc = PC()
    # for i in range(10):
    #     print(pc.use_action(longsword_action))

    
    party = Party([PC(), PC(), PC()])#, PC()])

    print(party._pcs[0]._class, party._pcs[0]._initiative)
    print(party._pcs[1]._class, party._pcs[1]._initiative)
    print(party._pcs[2]._class, party._pcs[2]._initiative)
    #print(party._pcs[3]._class, party._pcs[3]._initiative)


    monster_data1 = monsters_data["0.25"][6]
    monster_data2 = monsters_data["0.25"][5]
    #monster_data3 = monsters_data["0.25"][2]

    monster1 = Monster(monster_data1)
    monster2 = Monster(monster_data2)
    #monster3 = Monster(monster_data3)

    monsterGroup = MonsterGroup([monster1, monster2])

    combat = Combat(party, monsterGroup)

    for turn in combat._turn_order:
        if turn["combatant"]._type == "player":
            print(turn, turn["combatant"]._type, turn["combatant"]._class)
        else:
            print(turn, turn["combatant"]._type, turn["combatant"]._name)


    combat.combat()

__main__()