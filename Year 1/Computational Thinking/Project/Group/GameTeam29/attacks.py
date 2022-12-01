# Status effects --------------------------------------------

burn = {
    "name": "Light Burn",
    "type": "Burn",
    "description": "Deals medium burn damage to the oponent for three turns,\n damage is affected by armour",
    "damage": 2,
    "turns": 3
}

heavy_burn = {
    "name": "Heavy Burn",
    "type": "Burn",
    "description": "Deals heavy burn damage to the oponent for three turns,\n damage is affected by armour",
    "damage": 4,
    "turns": 3
}

bleed = {
    "name": "Bleed",
    "type": "Bleed",
    "description": "Deals extreme bleed damage to the oponent for three turns,\n damage is reduced twice as much by armour",
    "damage": 5,
    "turns": 3
}

heavy_bleed = {
    "name": "Heavy Bleed",
    "type": "Bleed",
    "description": "Deals very extreme bleed damage to the oponent for three turns,\n damage is reduced twice as much by armour",
    "damage": 7,
    "turns": 3
}

poison = {
    "name": "Poison",
    "type": "Poison",
    "description": "Deals low poison damage to the oponent for 4 turns,\n damage is not affected by armour",
    "damage": 3,
    "turns": 4
}

# boss attacks -----------------------------------------

kick = {
    "name": "Kick",
    "description": "A normal kick",
    "damage": 8,
    "effect": None,
    "cooldown": 1,
    "current-cooldown": 0
}

fire_slap = {
    "name": "Fire Slap",
    "description": "An attack with a prolonged burning effect",
    "damage": 10,
    "effect": burn,
    "cooldown": 5,
    "current-cooldown": 0
}

weak_punch = {
    "name": "Weak Punch",
    "description": "An attack",
    "damage": 5,
    "effect": None,
    "cooldown": 1,
    "current-cooldown": 0
}

punch = {
    "name": "Punch",
    "description": "An attack",
    "damage": 8,
    "effect": None,
    "cooldown": 1,
    "current-cooldown": 0
}

heavy_punch = {
    "name": "Heavy Punch",
    "description": "An attack",
    "damage": 15,
    "effect": None,
    "cooldown": 3,
    "current-cooldown": 0
}


poison_strike = {
    "name": "Poison Attack",
    "description": "An attack with a prolonged poison effect",
    "damage": 10,
    "effect": poison,
    "cooldown": 5,
    "current-cooldown": 0
}

slice_attack = { 
    "name": "Slice",
    "description": "A slice with your sword",
    "damage": 10,
    "effect": bleed,
    "cooldown": 1,
    "current-cooldown": 0
}

critical_slice = {
    "name": "Critical Slice",
    "description": "An attack with a prolonged bleeding effect",
    "damage": 15,
    "effect": heavy_bleed,
    "cooldown": 5,
    "current-cooldown": 0
}

# weapon attacks -----------------------------------------

# Knife
quick_slash = {
    "name": "Quick Slash",
    #"id": "qslash",
    "description": "A quick slash with your weapon",
    "damage": 10,
    "effect": None,
    "cooldown": 1,
    "current-cooldown": 0
}

heavy_slash = {
    "name": "Heavy Slash",
    #"id": "hslash",
    "description": "A slower, more damaging slash that applies bleed",
    "damage": 17,
    "effect": bleed,
    "cooldown": 3,
    "current-cooldown": 0
}

# Rock
bonk = {
    "name": "Bonk",
    "description": "Rock hit",
    "damage": 5,
    "effect": None,
    "cooldown": 1,
    "current-cooldown": 0
}

# Rubgy Ball
bounce = {
        "name": "Bounce",
        "Description": "Bounce the ball at your opponent",
        "damage": 2,
        "effect": None,
        "cooldown": 1,
        "current-cooldown": 0
}

# Cricket Bat
weak_strike = {
        "name": "Weak Strike",
        "Description": "Hit the oponent with your bat",
        "damage": 10,
        "effect": None,
        "cooldown": 1,
        "current-cooldown": 0
}

heavy_strike = {
        "name": "Heavy Strike",
        "Description": "Hit the oponent with your bat as hard as you can",
        "damage": 18,
        "effect": None,
        "cooldown": 4,
        "current-cooldown": 0
}

# Candle

candle_hit = {
    "name": "Hit",
    "description": "Hit your oponent with the candle",
    "damage": 7,
    "effect": None,
    "cooldown": 1,
    "current-cooldown": 0
}

candle_throw = {
    "name": "Throw",
    "description": "Throw the candle at your oponent",
    "damage": 5,
    "effect": burn,
    "cooldown": 3,
    "current-cooldown": 0
}

# Stick
weak_hit = {
    "name": "Weak Hit",
    "description": "Hit your oponent with the candle",
    "damage": 9,
    "effect": None,
    "cooldown": 1,
    "current-cooldown": 0
}

# Katana

katana_thrust = {
    "name": "Thrust",
    "description": "Thrust your katana into the oponent for a normal bleed effect",
    "damage": 11,
    "effect": bleed,
    "cooldown": 1,
    "current-cooldown": 0
}

katana_Slice = {
    "name": "Thrust",
    "description": "Bring down your katana onto the oponent for immense bleed damage",
    "damage": 5,
    "effect": heavy_bleed,
    "cooldown": 5,
    "current-cooldown": 0
}

# Torch

torch_hit = {
    "name": "Hit",
    "description": "Hit your oponent with the candle",
    "damage": 9,
    "effect": None,
    "cooldown": 1,
    "current-cooldown": 0
}

torch_throw = {
    "name": "Strong Throw",
    "description": "Throw the torch at your oponent",
    "damage": 10,
    "effect": heavy_burn,
    "cooldown": 4,
    "current-cooldown": 0
}

# Sabre

poke = {
    "name": "Poke",
    "description": "Poke your oponent with the sabre",
    "damage": 8,
    "effect": None,
    "cooldown": 1,
    "current-cooldown": 0
}

forceful_jab = {
    "name": "Forceful Jab",
    "description": "Use your full strength to jab your oponent",
    "damage": 10,
    "effect": poison,
    "cooldown": 4,
    "current-cooldown": 0
}

# Croissant
croissant_smash = {
    "name": "Croissant Smash",
    "description": "Smash the croissant into your oponent",
    "damage": 25,
    "effect": None,
    "cooldown": 4,
    "current-cooldown": 0
}

croissant_throw = {
    "name": "Croissant Throw",
    "description": "Throw the croissant at your oponent",
    "damage": 10,
    "effect": None,
    "cooldown": 1,
    "current-cooldown": 0
}
