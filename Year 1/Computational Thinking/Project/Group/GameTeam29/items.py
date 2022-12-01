from attacks import *

# Example/Testing items -----------------------------------------

# Example armour
basic_armour = {"name": "Basic Armour",
                  "item-type": "armour",
                  "description": "A basic piece armour",
                  "armour-value": 10}

# Example weapon
basic_sword = {"name": "Basic Sword",
                "item-type": "weapon",
                "description": "A basic sword",
                "attacks": [quick_slash, poison_strike, critical_slice, torch_throw]}

# Example healing item
health_item_template = {"name": "Healing Item",
                 "item-type": "h-item",
                 "description": "A basic health recovery item",
                 "healing-value": 10}

# Example defensive buff item
defence_buff_item = {"name": "Defence boost",
                 "item-type": "a-item",
                 "description": "A basic single use defence buff item",
                 "buff-value": 5}

# Example damage buff item
damage_buff_item = {"name": "Damage Boost",
                 "item-type": "d-item",
                 "description": "A basic single use damage buff item",
                 "buff-value": 5}

# Example useless item
paper = {"name": "Paper",
                "item-type": "useless",
                "description": "A piece of paper"}

# cardiff items -------------------------------------------

knife = {"name": "Knife",
                "description": "This knife is a prop used in the performance 'Lady Killers' in the Millennium Centre.",
                "item-type": "weapon",
                "attacks": [quick_slash, heavy_slash]}

rock = {"name": "Rock",
                "description": "This rock is located on the coastline of cardiff bay.",
                "item-type": "weapon",
                "attacks": [bonk]}

umbrella = {"name": "Umbrella",
                "description": "This umbrella is a daily essential used by most people in cardiff.",
                "item-type": "useless"}

ball = {"name": "Rugby ball",
                "description": "This rugby ball can be used when playing games of rugby. ",
                "item-type": "weapon",
                "attacks": [bounce]}

pint = {"name": "Pint",
                "description": "A pint is the usual drink to have while watching a rugby match.",
                "item-type": "a-item",
                "buff-value": 5}

# kyiv items    ------------------------------------------

balloon = {"name": "Latex Balloon",
                "description": "A soggy balloon under Zelenskyy's bed. I wonder what it was used for.",
                "item-type": "armour",
                "armour-value": 1}

boxers = {"name": "Boxers",
                "description": "A pair of dirty calvins. Smells a bit too.",
                "item-type": "armour",
                "armour-value": 8}

candle = {"name": "Candle",
                "description": "I think these are used to remember the dead, nice of them to give me one for free!",
                "item-type": "weapon",
                "attacks": [candle_hit, candle_throw]}

wine = {"name": "Glass of wine",
                "description": "A classic bev, looks a bit like blood.",
                "item-type": "h-item",
                "healing-value": 10}

# Melbourne Items ----
bat = {"name": "Cricket Bat",
                "description": "A wooden stick, could do some damage.",
                "item-type": "weapon",
                "attacks": [weak_strike, heavy_strike]}

helmet = {"name": "Cricket Helmet",
                "description": "A helment, could be good protection for a face",
                "item-type": "armour",
                "armour-value": 10}

watering = {"name": "Watering Can",
                "description": "It's just a watering can, pretty useless",
                "item-type": "useless" }

shears = {"name": "A Pair of Shears",
                "description": "Big scissors, might deal some damage",
                "item-type": "weapon",
                "attacks": [quick_slash, heavy_slash]}

# New York Items ---------------
apple = {"name": "Apple",
         "description": "A big apple",
         "item-type": "h-item",
         "healing-value": 5}

stick = {"name": "Stick",
         "description": "A fallen tree branch that could be used as a weapon",
         "item-type": "weapon",
         "attacks": [weak_hit]}

torch = {"name": "Torch",
         "description": "A torch reminiscent of the one the statue is holding",
         "item-type": "weapon",
         "attacks": [torch_hit, torch_throw]}

cocktail = {"name": "Manhattan Cocktail",
            "description": "A glass of New York city's signature cocktail",
            "item-type": "h-item",
            "healing-value": 10}

cap = {"name": "Baseball cap",
       "description": "A New York Yankees baseball cap",
       "item-type": "armour",
       "armour-value": 6}


# Rio Items -----------------------------

medal = {"name": "Gold Medal",
         "description": "This probably shouldn't still be here, but hey, it looks pretty cool.\n You feel slightly stronger wearing it.",
         "item-type": "a-item",
         "buff-value": 7 }

fencing_lame = {"name": "Fencing Lame",
                "description": "A decent quality lame, looks pretty durable",
                "item-type": "armour",
                "armour-value": 15}

rusty_fencing_sabre = {"name": "Fencing Sabre",
                       "description": "An incredibly rusty fencing sabre. Probably wont do much damage, but might poison your oponent",
                       "item-type": "weapon",
                       "attacks": [poke, forceful_jab] }

binoculars = {"name": "Binoculars",
              "description": "Some generic cheap tourism binoculars.",
              "item-type": "d-item",
              "buff-value": 7 }

bottle_of_water = {"name": "Bottled Water",
                   "description": "An unbranded bottle of water.",
                   "item-type": "h-item",
                   "healing-value": 15}

a_map = {"name": "Map",
       "description": "A map of the mountain",
       "item-type": "useless" }


# Paris Items -----------------------------

croissant = {"name": "Croissant",
             "item-type": "weapon",
             "description": "A flaky pastry that is the pride of France",
             "attacks": [croissant_smash, croissant_throw]}

beret = {"name": "Beret",
         "item-type": "armour",
         "description": "A small hat for small heads",
         "armour-value": 1}

red_wine = {"name": "Bottle of red wine",
            "item-type": "d-item",
            "description": "A red liquid used to increase your strength and sex drive",
            "buff-value": 7}

white_wine = {"name": "Bottle of white wine",
              "item-type": "a-item",
              "description": "A white liquid which makes make you more durable.",
              "buff-value": "5"}


eiffel_tower_model = {"name": "Model of the Eiffel Tower",
                      "item-type": "useless",
                      "description": "A little statue of the French's favourite thing"}

# Tokyo Items -----------------------------
sushi = {"name": "Sushi",
         "description": "A Japanese classic. You can try using chopsticks but you'll probably fail.",
         "item-type": "h-item",
         "healing-value": 10}

hot_spring = {"name": "Hot spring water",
              "description": "Warm water from a beautiful hot spring, but you aren't sure if it is clean.",
              "item-type": "a-item",
              "buff-value": 5}

katana = {"name": "Katana",
          "description": "A long, single-edged sword used by Japanese samurai. Don't try to hold it from the other end.",
          "item-type": "weapon",
          "attacks": [slice_attack, critical_slice]}

body_pillow = {"name": "Anime body pillow",
               "description": "You can use it to repel people.",
               "item-type": "useless"}

karuta = {"name": "Karuta",
          "description": "A type of Japanese armour worn by samurai warriors and their retainers during the feudal era of Japan.",
          "item-type": "armour",
          "armour-value": 15}
