bard_actions = {
    1: [
        {
            "name": "rapier",
            "type": "attack#physical",
            "target_type": "creature_amount",
            "amount_creatures": 1,
            "attacks": [{
                "attack_stat": "Finesse",
                "dmg_rolls": [{
                    "count": 1,
                    "dmg_roll": 8,
                    "dmg_type": "piercing"
                }]
            }]
        },
        {
            "name": "Vicious Mockery",
            "type": "dc#cantrip",
            "target_type": "creature_amount",
            "amount_creatures": 1,
            "st": "WIS",
            "dmg_rolls": [{
                "count": 1,
                "dmg_roll": 4,
                "dmg_type": "psychic"
            }],
            "half": False
        },
        {
            "name": "Dissonant Whispers 1",
            "type": "dc#spell",
            "target_type": "creature_amount",
            "amount_creatures": 1,
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
        {
            "name": "Thunderwave 1",
            "type": "dc#spell",
            "target_type": "aoe",
            "radius": 15,
            "spell_level": 1,
            "st": "CON",
            "dmg_rolls": [{
                "count": 2,
                "dmg_roll": 8,
                "dmg_type": "thunder"
            }],
            "half": True
            # +1d8 per extra slot lvl
        },
        {
            "name": "Cure Wounds 1",
            "type": "heal#spell",
            "spell_level": 1,
            "count": 1,
            "creatures": 1,
            "heal_dice": 8,
            "heal_bonus": "CHA"
            # +1d8 per extra slot lvl 
        }
    ],
    2: [
        {
            "name": "rapier",
            "type": "attack#physical",
            "target_type": "creature_amount",
            "amount_creatures": 1,
            "attacks": [{
                "attack_stat": "Finesse",
                "dmg_rolls": [{
                    "count": 1,
                    "dmg_roll": 8,
                    "dmg_type": "piercing"
                }]
            }]
        },
        {
            "name": "Vicious Mockery",
            "type": "dc#cantrip",
            "target_type": "creature_amount",
            "amount_creatures": 1,
            "st": "WIS",
            "dmg_rolls": [{
                "count": 1,
                "dmg_roll": 4,
                "dmg_type": "psychic"
            }],
            "half": False
        },
        {
            "name": "Dissonant Whispers 1",
            "type": "dc#spell",
            "target_type": "creature_amount",
            "amount_creatures": 1,
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
        {
            "name": "Thunderwave 1",
            "type": "dc#spell",
            "target_type": "aoe",
            "radius": 15,
            "spell_level": 1,
            "st": "CON",
            "dmg_rolls": [{
                "count": 2,
                "dmg_roll": 8,
                "dmg_type": "thunder"
            }],
            "half": True
            # +1d8 per extra slot lvl
        },
        {
            "name": "Cure Wounds 1",
            "type": "heal#spell",
            "spell_level": 1,
            "count": 1,
            "creatures": 1,
            "heal_dice": 8,
            "heal_bonus": "CHA"
            # +1d8 per extra slot lvl 
        }
    ],
    3: [
        {
            "name": "rapier",
            "type": "attack#physical",
            "target_type": "creature_amount",
            "amount_creatures": 1,
            "attacks": [{
                "attack_stat": "Finesse",
                "dmg_rolls": [{
                    "count": 1,
                    "dmg_roll": 8,
                    "dmg_type": "piercing"
                }]
            }]
        },
        {
            "name": "Vicious Mockery",
            "type": "dc#cantrip",
            "target_type": "creature_amount",
            "amount_creatures": 1,
            "st": "WIS",
            "dmg_rolls": [{
                "count": 1,
                "dmg_roll": 4,
                "dmg_type": "psychic"
            }],
            "half": False
        },
        {
            "name": "Dissonant Whispers 1",
            "type": "dc#spell",
            "target_type": "creature_amount",
            "amount_creatures": 1,
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
        {
            "name": "Dissonant Whispers 2",
            "type": "dc#spell",
            "target_type": "creature_amount",
            "amount_creatures": 1,
            "spell_level": 2,
            "st": "WIS",
            "dmg_rolls": [{
                "count": 4,
                "dmg_roll": 6,
                "dmg_type": "psychic"
            }],
            "half": True
            # +1d6 per extra slot lvl
        },
        {
            "name": "Thunderwave 1",
            "type": "dc#spell",
            "target_type": "aoe",
            "radius": 15,
            "spell_level": 1,
            "st": "CON",
            "dmg_rolls": [{
                "count": 2,
                "dmg_roll": 8,
                "dmg_type": "thunder"
            }],
            "half": True
            # +1d8 per extra slot lvl
        },
        {
            "name": "Thunderwave 2",
            "type": "dc#spell",
            "target_type": "aoe",
            "radius": 15,
            "spell_level": 2,
            "st": "CON",
            "dmg_rolls": [{
                "count": 3,
                "dmg_roll": 8,
                "dmg_type": "thunder"
            }],
            "half": True
            # +1d8 per extra slot lvl
        },
        {
            "name": "Cure Wounds 1",
            "type": "heal#spell",
            "spell_level": 1,
            "count": 1,
            "creatures": 1,
            "heal_dice": 8,
            "heal_bonus": "CHA"
            # +1d8 per extra slot lvl 
        },
        {
            "name": "Cure Wounds 2",
            "type": "heal#spell",
            "spell_level": 2,
            "count": 1,
            "creatures": 2,
            "heal_dice": 8,
            "heal_bonus": "CHA"
            # +1d8 per extra slot lvl 
        },
        {
            "name": "Phantasmal Force 2",
            "type": "dc#spell",
            "target_type": "creature_amount",
            "amount_creatures": 1,
            "spell_level": 2,
            "st": "INT",
            "dmg_rolls": [{
                "count": 1,
                "dmg_roll": 6,
                "dmg_type": "psychic"
            }],
            "half": True
        },
        {
            "name": "Shatter 2",
            "type": "dc#spell",
            "target_type": "creature_amount",
            "amount_creatures": 1,
            "spell_level": 2,
            "st": "CON",
            "dmg_rolls": [{
                "count": 3,
                "dmg_roll": 8,
                "dmg_type": "thunder"
            }],
            "half": True
            # +1d8 per extra slot lvl
        }
    ],
    4: [
        {
            "name": "rapier",
            "type": "attack#physical",
            "target_type": "creature_amount",
            "amount_creatures": 1,
            "attacks": [{
                "attack_stat": "Finesse",
                "dmg_rolls": [{
                    "count": 1,
                    "dmg_roll": 8,
                    "dmg_type": "piercing"
                }]
            }]
        },
        {
            "name": "Vicious Mockery",
            "type": "dc#cantrip",
            "target_type": "creature_amount",
            "amount_creatures": 1,
            "st": "WIS",
            "dmg_rolls": [{
                "count": 1,
                "dmg_roll": 4,
                "dmg_type": "psychic"
            }],
            "half": False
        },
        {
            "name": "Dissonant Whispers 1",
            "type": "dc#spell",
            "target_type": "creature_amount",
            "amount_creatures": 1,
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
        {
            "name": "Dissonant Whispers 2",
            "type": "dc#spell",
            "target_type": "creature_amount",
            "amount_creatures": 1,
            "spell_level": 2,
            "st": "WIS",
            "dmg_rolls": [{
                "count": 4,
                "dmg_roll": 6,
                "dmg_type": "psychic"
            }],
            "half": True
            # +1d6 per extra slot lvl
        },
        {
            "name": "Thunderwave 1",
            "type": "dc#spell",
            "target_type": "aoe",
            "radius": 15,
            "spell_level": 1,
            "st": "CON",
            "dmg_rolls": [{
                "count": 2,
                "dmg_roll": 8,
                "dmg_type": "thunder"
            }],
            "half": True
            # +1d8 per extra slot lvl
        },
        {
            "name": "Thunderwave 2",
            "type": "dc#spell",
            "target_type": "aoe",
            "radius": 15,
            "spell_level": 2,
            "st": "CON",
            "dmg_rolls": [{
                "count": 3,
                "dmg_roll": 8,
                "dmg_type": "thunder"
            }],
            "half": True
            # +1d8 per extra slot lvl
        },
        {
            "name": "Cure Wounds 1",
            "type": "heal#spell",
            "spell_level": 1,
            "count": 1,
            "creatures": 1,
            "heal_dice": 8,
            "heal_bonus": "CHA"
            # +1d8 per extra slot lvl 
        },
        {
            "name": "Cure Wounds 2",
            "type": "heal#spell",
            "spell_level": 2,
            "count": 1,
            "creatures": 2,
            "heal_dice": 8,
            "heal_bonus": "CHA"
            # +1d8 per extra slot lvl 
        },
        {
            "name": "Phantasmal Force 2",
            "type": "dc#spell",
            "target_type": "creature_amount",
            "amount_creatures": 1,
            "spell_level": 2,
            "st": "INT",
            "dmg_rolls": [{
                "count": 1,
                "dmg_roll": 6,
                "dmg_type": "psychic"
            }],
            "half": True
        },
        {
            "name": "Shatter 2",
            "type": "dc#spell",
            "target_type": "creature_amount",
            "amount_creatures": 1,
            "spell_level": 2,
            "st": "CON",
            "dmg_rolls": [{
                "count": 3,
                "dmg_roll": 8,
                "dmg_type": "thunder"
            }],
            "half": True
            # +1d8 per extra slot lvl
        }
    ],
    5: [
        {
            "name": "rapier",
            "type": "attack#physical",
            "target_type": "creature_amount",
            "amount_creatures": 1,
            "attacks": [{
                "attack_stat": "Finesse",
                "dmg_rolls": [{
                    "count": 1,
                    "dmg_roll": 8,
                    "dmg_type": "piercing"
                }]
            }]
        },
        {
            "name": "Vicious Mockery",
            "type": "dc#cantrip",
            "target_type": "creature_amount",
            "amount_creatures": 1,
            "st": "WIS",
            "dmg_rolls": [{
                "count": 1,
                "dmg_roll": 4,
                "dmg_type": "psychic"
            }],
            "half": False
        },
        {
            "name": "Dissonant Whispers 1",
            "type": "dc#spell",
            "target_type": "creature_amount",
            "amount_creatures": 1,
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
        {
            "name": "Dissonant Whispers 2",
            "type": "dc#spell",
            "target_type": "creature_amount",
            "amount_creatures": 1,
            "spell_level": 2,
            "st": "WIS",
            "dmg_rolls": [{
                "count": 4,
                "dmg_roll": 6,
                "dmg_type": "psychic"
            }],
            "half": True
            # +1d6 per extra slot lvl
        },
        {
            "name": "Dissonant Whispers 3",
            "type": "dc#spell",
            "target_type": "creature_amount",
            "amount_creatures": 1,
            "spell_level": 3,
            "st": "WIS",
            "dmg_rolls": [{
                "count": 5,
                "dmg_roll": 6,
                "dmg_type": "psychic"
            }],
            "half": True
            # +1d6 per extra slot lvl
        },
        {
            "name": "Thunderwave 1",
            "type": "dc#spell",
            "target_type": "aoe",
            "radius": 15,
            "spell_level": 1,
            "st": "CON",
            "dmg_rolls": [{
                "count": 2,
                "dmg_roll": 8,
                "dmg_type": "thunder"
            }],
            "half": True
            # +1d8 per extra slot lvl
        },
        {
            "name": "Thunderwave 2",
            "type": "dc#spell",
            "target_type": "aoe",
            "radius": 15,
            "spell_level": 2,
            "st": "CON",
            "dmg_rolls": [{
                "count": 3,
                "dmg_roll": 8,
                "dmg_type": "thunder"
            }],
            "half": True
            # +1d8 per extra slot lvl
        },
        {
            "name": "Thunderwave 3",
            "type": "dc#spell",
            "target_type": "aoe",
            "radius": 15,
            "spell_level": 3,
            "st": "CON",
            "dmg_rolls": [{
                "count": 4,
                "dmg_roll": 8,
                "dmg_type": "thunder"
            }],
            "half": True
            # +1d8 per extra slot lvl
        },
        {
            "name": "Cure Wounds 1",
            "type": "heal#spell",
            "spell_level": 1,
            "count": 1,
            "creatures": 1,
            "heal_dice": 8,
            "heal_bonus": "CHA"
            # +1d8 per extra slot lvl 
        },
        {
            "name": "Cure Wounds 2",
            "type": "heal#spell",
            "spell_level": 2,
            "count": 1,
            "creatures": 2,
            "heal_dice": 8,
            "heal_bonus": "CHA"
            # +1d8 per extra slot lvl 
        },
        {
            "name": "Cure Wounds 3",
            "type": "heal#spell",
            "spell_level": 3,
            "count": 1,
            "creatures": 3,
            "heal_dice": 8,
            "heal_bonus": "CHA"
            # +1d8 per extra slot lvl 
        },
        {
            "name": "Phantasmal Force 2",
            "type": "dc#spell",
            "target_type": "creature_amount",
            "amount_creatures": 1,
            "spell_level": 2,
            "st": "INT",
            "dmg_rolls": [{
                "count": 1,
                "dmg_roll": 6,
                "dmg_type": "psychic"
            }],
            "half": True
        },
        {
            "name": "Phantasmal Force 3",
            "type": "dc#spell",
            "target_type": "creature_amount",
            "amount_creatures": 1,
            "spell_level": 3,
            "st": "INT",
            "dmg_rolls": [{
                "count": 1,
                "dmg_roll": 6,
                "dmg_type": "psychic"
            }],
            "half": True
        },
        {
            "name": "Shatter 2",
            "type": "dc#spell",
            "target_type": "creature_amount",
            "amount_creatures": 1,
            "spell_level": 2,
            "st": "CON",
            "dmg_rolls": [{
                "count": 3,
                "dmg_roll": 8,
                "dmg_type": "thunder"
            }],
            "half": True
            # +1d8 per extra slot lvl
        },
        {
            "name": "Shatter 3",
            "type": "dc#spell",
            "target_type": "creature_amount",
            "amount_creatures": 1,
            "spell_level": 3,
            "st": "CON",
            "dmg_rolls": [{
                "count": 4,
                "dmg_roll": 8,
                "dmg_type": "thunder"
            }],
            "half": True
            # +1d8 per extra slot lvl
        }
    ],
}