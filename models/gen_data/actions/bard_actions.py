bard_actions = {
    1: [
        {
            "name": "rapier",
            "type": "attack#physical",
            "attack_stat": "Finesse",
            "dmg_rolls": [{
                "count": 1,
                "dmg_roll": 8,
                "dmg_type": "piercing"
            }]
        },
        {
            "name": "Vicious Mockery",
            "type": "dc#cantrip",
            "st": "WIS",
            "dmg_rolls": [{
                "count": 1,
                "dmg_roll": 4,
                "dmg_type": "psychic"
            }],
            "half": False
        },
        {
            "name": "Dissonant Whispers",
            "type": "dc#spell",
            "spell_level": 1,
            "st": "WIS",
            "dmg_rolls": [{
                "count": 3,
                "dmg_roll": 6,
                "dmg_type": "psychic"
            }],
            "half": True
            # +1d6 per extra slot lvl
        },
    ]
}