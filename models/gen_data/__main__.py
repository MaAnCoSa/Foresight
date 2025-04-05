from PC import PC
from Monster import Monster
from Party import Party
from MonsterGroup import MonsterGroup
from Combat import Combat
import json

def __main__(verbose = 0):
    if verbose >= 1:
        print("GEN_DATA!!!\n")

    with open("../data/raw/monsters.json", "r") as file:
        monsters_data = json.load(file)

    with open("../data/raw/spells.json", "r") as file:
        spells_data = json.load(file)

    results = []

    cr = 7
    amount_of_monsters = len(monsters_data[str(cr)])
    monster_exceptions = [
        "Rug of Smothering",
        "Hydra",
        "Vampire, Mist Form"
    ]
    for i in range(amount_of_monsters):
        if monsters_data[str(cr)][i]["name"] not in monster_exceptions:
            party = Party([PC(2), PC(2), PC(2), PC(2)])

            if verbose >= 1:
                print("Party:")
                print("\t",party._pcs[0]._class, party._pcs[0]._initiative)
                print("\t",party._pcs[1]._class, party._pcs[1]._initiative)
                print("\t",party._pcs[2]._class, party._pcs[2]._initiative)
                print("\t",party._pcs[3]._class, party._pcs[3]._initiative)
                print("")


            monster_data1 = monsters_data[str(cr)][i]
            #monster_data2 = monsters_data["0.25"][6]
            #monster_data3 = monsters_data["0.25"][2]

            monster1 = Monster(monster_data1, spells_data)
            #monster2 = Monster(monster_data2, spells_data)
            #monster3 = Monster(monster_data3, spells_data)

            monsterGroup = MonsterGroup([monster1])

            if verbose >= 1:
                print("Monster Group:")
                print("\t",monsterGroup._monsters[0]._name, monsterGroup._monsters[0]._initiative)
                #print("\t",monsterGroup._monsters[0]._name, monsterGroup._monsters[0]._initiative)
                #print("\t",monsterGroup._monsters[0]._name, monsterGroup._monsters[0]._initiative)
                #print("\t",monsterGroup._monsters[0]._name, monsterGroup._monsters[0]._initiative)
                print("")

            combat = Combat(party, monsterGroup)

            if verbose >= 1:
                print("Turns:")
                for turn in combat._turn_order:
                    if turn["combatant"]._type == "player":
                        print("\t", turn, turn["combatant"]._type, turn["combatant"]._class)
                    else:
                        print("\t", turn, turn["combatant"]._type, turn["combatant"]._name)
                print("")

            combat.combat(verbose)

            classes = []
            statuses = []
            hps = []
            for pc in party._pcs:
                classes.append(pc._class._name)
                statuses.append(pc._status)
                hps.append(pc._hp)

            names = []
            mon_statuses = []
            mon_hp = []
            for monster in monsterGroup._monsters:
                names.append(monster._name)
                mon_statuses.append(monster._status)
                mon_hp.append(monster._hp)

            results.append({
                "combat": i+1,
                "party": classes,
                "party_status": statuses,
                "party_hp": hps,
                "monster_group": names,
                "monster_status": mon_statuses,
                "monster_hp": mon_hp
            })
    
    print("\nCOMBATS:")
    for result in results:
        print(result)

__main__(verbose=2)