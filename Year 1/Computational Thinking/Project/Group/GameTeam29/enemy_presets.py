from attacks import *

# Boss presets ---------------------------------------------

test_boss = {
    "name": "Boss",
    "attacks": [kick, fire_slap],
    "armour": 10,
    "health": 100,
    "afflicted-status": None
}

rusty_boss = {
    "name": "Poison Boss",
    "description": "Wielding a pair of rusty knuckle dusters, you better watch out this bosses poison effects",
    "attacks": [punch, poison_strike],
    "armour": 15,
    "health": 100,
    "afflicted-status": None
}

fire_boss = {
    "name": "Fire Boss",
    "description": "Wielding a brightly lit flaming torch, you better watch out this bosses burn effects",
    "attacks": [kick, fire_slap],
    "armour": 15,
    "health": 100,
    "afflicted-status": None
}

tank_boss = {
    "name": "Armoured Boss",
    "description": "Extreme armour with lower attack",
    "attacks": [weak_punch, punch],
    "armour": 60,
    "health": 80,
    "afflicted-status": None
}

boxer_boss = {
    "name": "Boxer",
    "description": "A deadly boxer with high armour and consistent damage",
    "attacks": [punch, heavy_punch],
    "armour": 30,
    "health": 100,
    "afflicted-status": None
}

chef_boss = {
    "name": "Chef",
    "description": "Who needs armour when you have knifes?",
    "attacks": [slice_attack, critical_slice],
    "armour": 0,
    "health": 100,
    "afflicted-status": None
}

bosses = [chef_boss, boxer_boss, tank_boss, fire_boss, rusty_boss]