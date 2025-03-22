from PC import PC
from Party import Party
from MonsterGroup import MonsterGroup
from Combat import Combat


def __main__():
    print("GEN_DATA!!!")

    longsword_action = {
      "type": "attack",
      "attack_stat": "STR",
      "dmg_roll": 10
    }

    pc = PC()
    for i in range(10):
        print(pc.use_action(longsword_action))

    
    party = Party([PC(), PC(), PC(), PC()])

    print(party._pcs[0]._class, party._pcs[0]._initiative)
    print(party._pcs[1]._class, party._pcs[1]._initiative)
    print(party._pcs[2]._class, party._pcs[2]._initiative)
    print(party._pcs[3]._class, party._pcs[3]._initiative)

    monster = PC()
    monster._type = "monster"
    monsterGroup = MonsterGroup([monster])

    combat = Combat(party, monsterGroup)

    for turn in combat._turn_order:
        print(turn, turn["combatant"]._type, turn["combatant"]._class)

    combat.combat()

__main__()