import random

player = {"name": "Bingus", "health": 999, "mana": 998, "alive": True, "experiance": 2540, "inventory": ["sword", "staff", "toast"]}



def print_player(player):
    for stat in player:
        print(f"{stat} is {player[stat]}")

def compute_experiance(damage):
    xp_gain = random.randrange(0, damage * 2)
    return xp_gain

def take_damage(damage, player):
    player["health"] -= damage
    player["experiance"] += compute_experiance(damage)
    if (player["health"] <= 0):
        player["health"] = 0
        player["alive"] = False
    return player

print_player(player)
take_damage(2000, player)
print()
print_player(player)


'''
player = {}
print(player)

player["name"] = "Sheldor The Conqueror"
player["health"] = 79
player["ammo"] = 100
print(player)
print(player["ammo"])

del player["ammo"]
print(player)



player = {"name": "Bingus", "health": 999, "mana": 998, "alive": True, "inventory": {"sword", "staff", "toast"}}

print(player)
print((player["inventory"]))



#Add sword
player["inventory"].append("Mask of Fabric")
print(player)

for item in player["inventory"]:
    if (item == "Mask of Fabric"):
        print(True)
        break

length = len(player["inventory"])

print(f"Amount of items: {length}")


#print stats

for stat in player:
    print(f"{stat} is {player[stat]}")



'''