fighter_str_actions = {
    1: [
        {
          "name": "unarmed_strike",
          "type": "attack#physical",
          "target_type": "creature_amount",
          "amount_creatures": 1,
          "attacks": [{
            "attack_stat": "STR",
            "dmg_rolls": [{
                "count": 1,
                "dmg_roll": 1,
                "dmg_type": "bludgeoning"
            }]
          }]
        },
        {
          "name": "Longsword",
          "type": "attack#physical",
          "target_type": "creature_amount",
          "amount_creatures": 1,
          "attacks": [{
            "attack_stat": "STR",
            "dmg_rolls": [{
                "count": 1,
                "dmg_roll": 10,
                "dmg_type": "slashing"
            }]
          }]
        }
    ]
}