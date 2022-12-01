from animations import *
from enemy_presets import *
import math
import main
import random

# Denotes whether a turn should be used or not during the view inventory phase
turn_used = True

# Returns a list of attacks that are currently off cooldown
def get_availiable_attacks(attacks):
    availiable_attacks = []
    for attack in attacks:
        if (attack["current-cooldown"] <= 0):
            availiable_attacks.append(attack)
    return availiable_attacks

# Prints all attacks that are not currently on cooldown
def display_attacks(avaliable_attacks):
    print("Attacks: ", end="")
    moves = ""
    for attack in avaliable_attacks:
        moves += attack["name"] + ", "
    moves = moves[0: (len(moves) - 2)] + "."
    print(moves)

# Calculates the amount of damage to be dealt after armour has been taken into account
def calc_damage_reduction(damage, armour):
    reduction_percent = 60 * math.log((1/8 * armour) + 1, 10)
    damage = round(damage * (1 - (reduction_percent / 100)), 0) 
    return damage

# Boss functions -------------------------------------

# Creates a new affliction dictionary so the cooldown can be changed idenpendantly from the attacks cooldown
def create_new_affliction(affliction):
    new_affliction = {}
    new_affliction["type"] = affliction["type"]
    new_affliction["damage"] = affliction["damage"]
    new_affliction["turns"] = affliction["turns"]
    return new_affliction

# Reduces the players health by the damage of the requested attack
def deal_damage_to_player(attack, player):
     # Check if the used attack applies any effects
    if (attack["effect"] != None):
        match attack["effect"]["type"]:
            case "Burn":
                player["afflicted-status"] = create_new_affliction(attack["effect"])
                print("You were burnt")
            case "Bleed":
                player["afflicted-status"] = create_new_affliction(attack["effect"])
                print("You started to bleed")
            case "Poison":
                player["afflicted-status"] = create_new_affliction(attack["effect"])
                print("You were poisoned")

    # The player's armour reduces the total damage
    damage = calc_damage_reduction(attack["damage"], player["armour"]["armour-value"] + player["bonus-armour"])
    player["health"] -= damage
    print(f"You took {damage} damage")

    # Check and update player status effects
    player = update_affliction(player)

    return player

# Increase the damage of the attacks that the boss can deal
def increase_boss_damage(boss):
    for attack in boss["attacks"]:
        attack["damage"] *= 2
    return boss

# Reset the cooldown of a given boss attack
def set_boss_attack_cooldown(boss, completed_attack):
    for attack in boss["attacks"]:
        if (attack["name"] == completed_attack["name"]):
            attack["current-cooldown"] = attack["cooldown"]
    return boss

# Decreases the cooldown time for some of the bosses special attacks
def decrease_boss_cooldown_times(boss):
    for attacks in boss["attacks"]:
        attacks["current-cooldown"] -= 1
    return boss

# Displays the bosses current stats as well as its next attack
def display_boss_details(boss):
    availiable_attacks = get_availiable_attacks(boss["attacks"])
    next_attack = availiable_attacks[random.randint(0, len(availiable_attacks) - 1)]

    print("/------------- " + boss["name"] + " -------------\\")
    print(" Health: " + str(boss["health"]))
    print(" Armour: " + str(boss["armour"]))
    print(" Next Attack: " + next_attack["name"])
    print(" Damage: " + str(next_attack["damage"]))

    # Prints the effect of the next attack, if it has one
    if (next_attack["effect"] != None):
        print(" Effect: " + next_attack["effect"]["type"])

    # Prints the current effect on the boss, if one is active
    if (boss["afflicted-status"] != None):
        print(" Status: " + boss["afflicted-status"]["type"])

    h = "-" * len(boss["name"])

    print("\\--------------" + h + "--------------/")

    return next_attack

# Player functions --------------------------------------
    
# Prints the availiable options to the user
def print_user_options():
    while (True):
        print("\nYou can: ")
        print("Choose an attack")
        print("Open your inventory")
        print("Pass the turn")

        user_input = input("Enter: ")
        user_input = main.normalise(user_input)

        for i in user_input:
            if (i == "choose" or i == "attack"):
                return "attack"
            elif (i == "open" or i == "inventory"):
                return "inventory"
            elif (i == "pass" or i == "turn"):
                return "pass"

        print("Enter a valid choice")

# Decrease the current cooldown for all the player's attacks
def decrease_cooldowns(player, amount = 1):
    for attacks in player["weapon"]["attacks"]:
        attacks["current-cooldown"] -= amount
    return player

# Reduces the players health by the damage of the requested attack
def deal_damage_to_boss(attack, boss, player):
    
    # Check if the used attack applies any effects
    if (attack["effect"] != None):
        match attack["effect"]["type"]:
            case "Burn":
                boss["afflicted-status"] = create_new_affliction(attack["effect"])
                print("You afflicted the boss with burn")
            case "Bleed":
                boss["afflicted-status"] = create_new_affliction(attack["effect"])
                print("You afflicted the boss with bleed")
            case "Poison":
                boss["afflicted-status"] = create_new_affliction(attack["effect"])
                print("You afflicted the boss with poison")

    # The player's armour reduces the total damage
    damage = calc_damage_reduction(attack["damage"] + player["bonus-damage"], boss["armour"])
    boss["health"] -= damage
    print(f"You dealt {damage} damage")

    # Check and update boss status effects
    boss = update_affliction(boss)

    return boss    

# Does not take into account status afflictions or bonus damage
def deal_turn_damage_to_boss(attack, boss):
    damage = calc_damage_reduction(attack["damage"], boss["armour"])
    boss["health"] -= damage
    return boss    

# Applies turn based status damage to the player
def deal_turn_damage_to_player(attack, player, custom_armour_value = None):
    damage = 0
    if (custom_armour_value == None):
        damage = calc_damage_reduction(attack["damage"], player["armour"]["armour-value"])
    else:
        damage = calc_damage_reduction(attack["damage"], custom_armour_value)

    player["health"] -= damage
    return player  

# Print an attacks name, description and effect (if there are any)
def view_attack(attack):
    h = "-" * math.ceil((len(attack["description"]) / 2))
    if (attack["effect"] != None):
        if (len(attack["effect"]["description"]) > len(attack["description"]) ):
            h = "-" * math.ceil((len(attack["effect"]["description"]) / 3))

    print(f"/{h} " + attack["name"] + f" {h}\\")
    print(" " + attack["description"])
    print(" Damage: " + str(attack["damage"]))
    if (attack["effect"] != None): 
        print(" Effect: " + attack["effect"]["name"] + ".\n " + attack["effect"]["description"])
    

    p = "-" * len(attack["name"])
    print(f"\\{h}-" + p + f"{h}-/")

# Allows the user to select which of the availaible attacks they would like to use
def get_user_attack_choice(attacks):
    user_input = (input("Enter: "))
    if (user_input.lower() == "back" ):
        return "back"

    user_input = main.normalise(user_input)
    user_input = main.combine_words(user_input, attacks)

    if (user_input == False):
        print("Please enter a valid attack")
        return get_user_attack_choice(attacks)
        
    chosen_attack = ""
    valid_attack = False
    # Check if the user_input is a valid attack
    for word in user_input:
        for attack in attacks:
            if (word.lower() == attack["name"].lower()):
                chosen_attack = attack
                valid_attack = True

    if (user_input[0] == "view" and valid_attack == True):
        print()
        view_attack(chosen_attack)
        return get_user_attack_choice(attacks)

    if (valid_attack == True):
        return chosen_attack
    else:
        print("Please enter a valid attack")
        return get_user_attack_choice(attacks)


# Returns an attack dictionary or keyword
def get_attack(attacks):
    print()
    print("Which attack would you like to use? (type BACK to go back type VIEW <attack> to view your attack)")
    display_attacks(attacks)
    choice = get_user_attack_choice(attacks)
    if (choice == "back"):
        return choice
    
    for attack in attacks:
        if (choice["name"].lower() == attack["name"].lower()):
            attack["current-cooldown"] = attack["cooldown"]
    return choice

# Equips the given armour to the player
def switch_armour(player, item):
    print("Would you like to switch to this armour? (yes/no)")
    i = input("Enter: ").lower()
    if (i == "y" or i == "yes"):
        if (player["armour"] != None): # If a piece of armour is already active, return to the inventory
            player["inventory"].append(player["armour"])
        player["armour"] = item
        player["inventory"].remove(item)
        print()
        print("You equipped " + item["name"])
    return player

# Equips the given weapon to the player
def switch_weapon(player, item):
    print("Would you like to switch to this weapon? (yes/no)")
    i = input("Enter: ").lower()
    if (i == "y" or i == "yes"):
        if (player["weapon"] != None): # If a piece of armour is already active, return to the inventory
            player["inventory"].append(player["weapon"])
        player["weapon"] = item
        player["inventory"].remove(item)
        print()
        print("You equipped " + item["name"])
    return player

# Uses the given health item on the player
def use_health_item(player, item):
    health_to_add = item["healing-value"]
    player["health"] += health_to_add
    player["inventory"].remove(item)
    print("You used the " + item["name"])
    print("Gained " + str(health_to_add) + " health")
    return player

# Uses the given damage buff item on the player
def use_damage_buff_item(player, item):
    buff = item["buff-value"]
    player["bonus-damage"] += buff
    player["inventory"].remove(item)
    print(f"You gained {buff} bonus damage!")
    return player

# Uses the given armour buff item on the player
def use_armour_buff_item(player, item):
    buff = item["buff-value"]
    player["bonus-armour"] += buff
    player["inventory"].remove(item)
    print(f"You gained {buff} bonus armour!")
    return player

# Attempts to use the requested item from the player
def use_item(player, requested_item):
    global turn_used
    turn_used = True
    item_to_use = None

    # Get item from player, as requested item is a string
    for item in player["inventory"]:
        if (item["name"].lower() == requested_item):
            item_to_use = item
            break
        
    if (item_to_use == None):
        print("Please select a valid item")
        turn_used = False
    else:
        # Math the item to the correct type
        match item_to_use["item-type"]:
            case "useless":
                print("This item has no use")
            case "armour":
                clear()
                player = switch_armour(player, item_to_use)
            case "weapon":
                clear()
                player = switch_weapon(player, item_to_use)
            case "h-item":
                clear()
                player = use_health_item(player, item_to_use)
            case "d-item":
                clear()
                player = use_damage_buff_item(player, item_to_use)
            case "a-item":
                clear()
                player = use_armour_buff_item(player, item_to_use)
            case _:
                turn_used = False
    return player

# Prints the requested item to the console
def view_item(player, requested_item):
    item_to_use = None
    for item in player["inventory"]:
        if (item["name"].lower() == requested_item):
            item_to_use = item
            break

    if (item_to_use == None):
        print("Please select a valid item")
    else:
        print("/--------------- " + item_to_use["name"] + " ---------------\\")
        
        print(" " + item_to_use["description"])
        # Prints the correct details based on item type
        match item["item-type"]:
                case "armour":
                    print(" Armour Value: " + item_to_use["armour-value"])
                case "weapon":
                    print(" ", end="") 
                    display_attacks(item_to_use["attacks"])
                case "h-item":
                    print(" Heals for: " + str(item_to_use["healing-value"]) + "hp")
                case "d-item":
                    print(" Grants: " + str(item_to_use["buff-value"]) + " bonus damage")
                case "a-item":
                    print(" Grants: " + str(item_to_use["buff-value"]) + " bonus armour")

        h = "-" * len(item_to_use["name"])
        print("\\----------------" + h + "----------------/")

# Prints the players inventory to the console and gives them to option to use or view an item, or return to the previous menu
def display_inventory(player):
    global turn_used
    turn_used = True

    if (len(player["inventory"]) > 0):
        print("\nType USE <item> to use an item. Type VIEW <item> to view an item. Type BACK to go back")
        main.print_player_items(player["inventory"])
        
        valid_selection = False
        while (valid_selection == False):
            user_input = main.normalise(input("Enter: "))
            if (len(user_input) < 1):
                print("Enter a valid item")
                turn_used = False
                break

            if (len(user_input) > 2):
                user_input = main.combine_words(user_input, player["inventory"])

            if(user_input[0] == "use"):
                player = use_item(player, user_input[1])
                break
            elif(user_input[0] == "view"):
                view_item(player, user_input[1])
                return "viewed"
            elif(user_input[0] == "back"):
                return "back"
            else:
                print("Do what?")
    else:
        print("You have no items")
        turn_used = False
    return player

# Apply the currently afflicted status effects to the player
def apply_status_to_player(player):
    match player["afflicted-status"]["type"]:
        case "Burn":
            # Deals normal damage
            player = deal_turn_damage_to_player(player["afflicted-status"], player)
            print("You were burnt for " + str(calc_damage_reduction(player["afflicted-status"]["damage"], player["armour"]["armour-value"])) + " damage.")
        case "Poison": 
            # Ignores armour
            player = deal_turn_damage_to_player(player["afflicted-status"], player)
            print("You suffered " + str(calc_damage_reduction(player["afflicted-status"]["damage"], 0)) + " damage from being poisoned.")
        case "Bleed":
            # Armour matters twice as much
            player = deal_turn_damage_to_player(player["afflicted-status"], player)
            print("You suffered " + str(calc_damage_reduction(player["afflicted-status"]["damage"], (player["armour"]["armour-value"]) * 2)) + " damage from bleeding.")
    
    return player

# Apply the currently afflicted status effects to the boss
def apply_status_to_boss(boss):
    match boss["afflicted-status"]["type"]:
        case "Burn":
            # Deals normal damage
            boss = deal_turn_damage_to_boss(boss["afflicted-status"], boss)
            print("You burnt the boss for " + str(calc_damage_reduction(boss["afflicted-status"]["damage"], boss["armour"])) + " damage.")
        case "Poison": 
            # Ignores armour
            boss = deal_turn_damage_to_boss(boss["afflicted-status"], boss)
            print("You poisoned the boss for " + str(calc_damage_reduction(boss["afflicted-status"]["damage"], 0)) + " damage.")
        case "Bleed":
            # Armour matters twice as much
            boss = deal_turn_damage_to_boss(boss["afflicted-status"], boss)
            print("You bled the boss for " + str(calc_damage_reduction(boss["afflicted-status"]["damage"], boss["armour"] * 2)) + " damage.")
    return boss

# Causes the current affliction (if there is one) to be applied to the character (either boss or player)
def update_affliction(character):
    if (character["afflicted-status"] != None and character["afflicted-status"]["turns"] > 1):
        match character["afflicted-status"]["type"]:
            case "Burn":
                if (character["name"] == "Player"):
                    character = apply_status_to_player(character)
                else:
                    character = apply_status_to_boss(character)
            case "Bleed":
                if (character["name"] == "Player"):
                    character = apply_status_to_player(character)
                else:
                    character = apply_status_to_boss(character)
            case "Poison":
                if (character["name"] == "Player"):
                    character = apply_status_to_player(character)
                else:
                    character = apply_status_to_boss(character)

        character["afflicted-status"]["turns"] -= 1

    else:
        character["afflicted-status"] = None

    return character

# Defines the player and boss variables as well as printing the boss intro
def intilialise_boss_battle(player_health, player_inventory, player_weapon, player_armour):
    # Select random boss preset
    boss = bosses[random.randrange(0, len(bosses))]

    print("You find yourself in a strange unrecognisable place with a tall figure looming over you...")
    print("It's a " + boss["name"])
    print(boss["description"])
    print()
    print("In order to win this fight you must use all the items you've gathered up till this point to the best of their ability")
    print("Good luck")


    player = {
        "name": "Player",
        "health": player_health,
        "inventory": player_inventory,
        "weapon": player_weapon,
        "armour": player_armour,
        "bonus-damage": 0,
        "bonus-armour": 0,
        "afflicted-status": None
    }

    boss_loop(boss, player)
    pass

# The main looping function that the bass battle occurs in
def boss_loop(boss, player):
    global turn_used
    turn = 1
    intial_boss_health = boss["health"]
    while (True):
        print(f"\n--------------------------- Turn {turn} ---------------------------\n")
        next_boss_attack = display_boss_details(boss) # Gets next boss attack
        print("Player health remaining: " + str(player["health"]))
        choice_selected = False

        # Players turn
        while (choice_selected == False):
            initial_choice = print_user_options()

            match initial_choice:
                case "attack":
                    av_attacks = get_availiable_attacks(player["weapon"]["attacks"])
                    choice = get_attack(av_attacks)
                    if (choice == "back"):
                        continue
                    else:
                        clear()
                        print()
                        boss = deal_damage_to_boss(choice, boss, player)
                        choice_selected = True

                case "inventory":
                    option = display_inventory(player)
                    if (option == "viewed" or option =="back"):
                        continue
                    else:
                        player = option
                    if (turn_used != False):
                        choice_selected = True
                case "pass":
                    clear()
                    player = decrease_cooldowns(player)
                    choice_selected = True

        print()
        # Check win conditions
        if (boss["health"] < 1):
            print("You Win!")
            break

        # Bosses turn

        # If boss health falls below 30%, difficulty increases
        # Doubles the damage of all attacks
        if (boss["health"] <= 0.2 * intial_boss_health):
            boss = increase_boss_damage(boss) 
            print("The boss grew stronger!")

        player = deal_damage_to_player(next_boss_attack, player)
        boss = set_boss_attack_cooldown(boss, next_boss_attack)
        
        # Check fail conditions
        if (player["health"] < 1):
            print("You lose!")
            break

        # Iterate all cooldowns for both the boss and player
        player = decrease_cooldowns(player)
        boss = decrease_boss_cooldown_times(boss)
        
        turn += 1
    
    return True
