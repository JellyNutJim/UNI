from html.entities import codepoint2name
from map import cities
from player import *
from items import *
from boss_battle import *
from animations import *

game_active = True

def get_player_input():
    player_input = input("Enter: ")
    return player_input

# Removes all punctuation and numbers from a string, while keeping characters and spaces.
def normalise(string):
    normalised_string = ''
    for char in string.lower():
        if (char >= 'a' and char <= 'z') or char == " ":
            normalised_string += char

    seperated_words = seperate_words(normalised_string)
    return seperated_words

# Checks if a string exists within a list
def exists_in(words, word):
    for string in words:
        if (string == word):
            return True
    return False

# Splits up words in a string based on when a space (" ") is found
def seperate_words(user_input):
    new_word = ""
    start_word = False
    words = []
    user_input += " "

    for i in range(len(user_input)):
        if(user_input[i].isalpha() == True and start_word == False):
            new_word += user_input[i]
            start_word = True
        elif (user_input[i].isalpha() == True and start_word == True):
            new_word += user_input[i]
        elif (user_input[i].isalpha() == False and start_word == True):
            words.append(new_word)
            new_word = ""
            start_word = False

    return words

# Combines up to two words
# words > 2
def combine_words(words, items = None):
    new_words = []

    if (items == None):
        global inventory
        global current_place
        global current_city

        new_words = combine_word_process(words, inventory)

        if (len(new_words) < 2 and current_place != None):
            new_words = combine_word_process(words, current_place["items"])

        if (len(new_words) < 2):
            new_words = combine_word_process(words, current_city["places"])

        if (len(new_words) < 2):
            for key in current_city["connections"].keys():
                city_list = []
                city_list.append(current_city["connections"][key])
                new_words = combine_word_process(words, city_list)
                if (len(new_words) == 2):
                    break
    else:
        new_words = combine_word_process(words, items)

    if (new_words == False):
        return False
    return new_words

# Searches a list and compares it too potential items in order to find a match
def combine_word_process(words, items):
        new_words = []
        if (len(words) < 1):
            return False
        new_words.append(words[0])

        for item in items:
            item_split = seperate_words(item["name"].lower())

            word1 = False
            word2 = False
            for i in range (0, len(item_split), + 1):
                if (word1 == False):
                    if (exists_in(words, item_split[i])):
                        word1 = True
                else:
                    if (exists_in(words, item_split[i])):
                        word2 = True

            if (word1 == True and word2 == True):
                new_words.append(item["name"].lower())
                break

        return new_words

# Displays the name and description of a given city
def print_city(city):
    print(f'\nYou are in {city["name"]}.\n\n{city["description"]}\n')

# Displays the name and description of a given place
def print_place(place):
    print(f'\nYou are in {place["name"]}.\n\n{place["description"]}\n')

# Print the places and cities you can travel to
def print_city_destinations(city):
    # Print places
    print("Which of these places do you want to go to?")
    for place in city["places"]:
        print("GO", place["id"].upper(), "to go to", place["name"])

    # Print destinations
    print()
    print("Which of these cities would you like to visit")
    destinations = city["connections"]

    # Prints all cities that connect to the current city excluding itself
    for place in destinations:
        if (place == city["id"]):
            continue
        else:
            print("GO", place.upper(), "to go to", place)

    print("GO BOSS to go to the final boss" )

# Enter the boss fight phase
def start_boss():
    global equipped_armour
    global equipped_weapon
    global inventory
    global game_active
    ready_for_fight = True

    # Check if the player could be in a more advantageous position before continuing
    if (equipped_weapon == None):
        clear()
        print("You must have a weapon before fighting the boss")
        return
    elif (equipped_armour == None):
        clear()
        print("You must have a piece of armour before fighting the boss")
    else:
        if (len(inventory) < 4):
            print("You can still hold more items")
            ready_for_fight = False
        if (ready_for_fight == False):
            print("Do you wish to fight the boss anyway? (y/n)")
        else:
            print("Do you wish to fight the boss (y/n)")
        i = input("Enter: ").lower()
        if (i == "y" or i == "yes"):
            #TEMP
            clear()
            intilialise_boss_battle(100, inventory, equipped_weapon, equipped_armour)
            game_active = False
        else:
            clear()

# Move from the current city to another city or a place within that city
def execute_move_city(destination): # Moves player
    global current_city
    global current_place

    if (destination == "boss"):
        start_boss()
        return

    # Move to city
    for city in cities:
        if (city == destination):
            current_city = cities[city]
            travel_animation(plane)
            current_place = None
            return

    # Move to place
    for place in current_city["places"]:
        if (place["name"].lower() == destination or place["id"] == destination):
            print(True)
            travel_animation(bus)
            current_place = place
            return
    clear()
    print("Please enter a valid place")

# Returns the user to the current city form there current place
def execute_move_place():
    global current_place
    travel_animation(bus)
    current_place = None
    print("You returned to the city")

# Attempts to take an item from the place and add it to the player inventory.
def execute_take(item_id):
    global current_place
    global inventory
    global max_inventory_items

    # Checks if the player is already at max items
    if (len(inventory) >= max_inventory_items ):
        clear()
        print("You are at maximum items")
        return
    else:
        for item in current_place["items"]:
            if (item_id == item["name"].lower()):
                inventory.append(item)
                current_place["items"].remove(item)
                clear()
                print("You took " + item["name"])
                return
    clear()
    print("This item is not present")

# Attempts to drop an item from the players inventory, adding it to the current place.
def execute_drop(item_id):
    global current_place
    global inventory
    clear()

    # Checks if the requested item exists within the user's inventory
    for item in inventory:
        if (item_id == item["name"].lower()):
            current_place["items"].append(item)
            inventory.remove(item)
            print("You dropped " + item["name"])
            return
    print("You do not have this item")

# Switches the current weapon to the given input
def switch_weapon(item):
    global equipped_weapon
    global inventory

    if (equipped_weapon != None):
        inventory.append(equipped_weapon)
        equipped_weapon = item
        inventory.remove(item)
    else:
        inventory.remove(item)
        equipped_weapon = item

# Switches the current armour to the given input
def switch_armour(item):
    global equipped_armour
    global inventory

    if (equipped_armour != None):
        inventory.append(equipped_armour)
        equipped_armour = item
        inventory.remove(item)
    else:
        inventory.remove(item)
        equipped_armour = item

# Repeats until the player has decided to take or leave the item
# The user can view an items attacks while doing this
def view_or_equip_attacks(item_to_view):
    print("\nWould you like to view an attack (VIEW <attack>) or Would you like to equip this weapon? (y/n)")
    user_input = get_player_input().lower()
    user_input = normalise(user_input)
    if (len(user_input) > 2):
        user_input = combine_words(user_input, item_to_view["attacks"])
    print()
    if (user_input == False or len(user_input) < 1):
        print("Please enter a valid attack")
        view_or_equip_attacks(item_to_view)
    elif (user_input[0] == "view"):
        if (len(user_input) > 1):
            for attack in item_to_view["attacks"]:
                if (user_input[1].lower() == attack["name"].lower()):
                    view_attack(attack)
                    view_or_equip_attacks(item_to_view)
                    return
        else:
            print("View what?")
            view_or_equip_attacks(item_to_view)

        print("Enter a valid attack")
        view_or_equip_attacks(item_to_view)
        
    elif (user_input[0] == "y" or user_input[0] == "yes"):
        switch_weapon(item_to_view)
        clear()
        print("You equipped the " + item_to_view["name"])
        return
    else:
        clear()
        return

# Attempts to show the player all details about a requested item.
def execute_view(item_id):
    global inventory
    global current_place
    item_to_view = None
    if current_place == None:
        return
    in_inv = False

    # Checks if the requested item is within the current place
    for item in inventory:
        if (item_id == item["name"].lower()):
            item_to_view = item
            in_inv = True
            break

    # Checks if the requested item is within the player's inventory
    for item in current_place["items"]:
        if (item_id == item["name"].lower()):
            item_to_view = item
            break

    # If an item was found, display that information.
    if (item_to_view != None):
        clear()
        h = "-" * math.ceil((len(item_to_view["description"]) / 2))

        print(f"/{h} " + item_to_view["name"] + f" {h}\\")
        print(" " + item_to_view["description"])
        #print("Damage: " + str(item_to_view["damage"]))

        # Prints the appropriate dialog depending on the item type
        match item_to_view["item-type"]:
                case "armour":
                    print(" Grants " + str(item_to_view["armour-value"]) + " armour when equipped")
                case "weapon":
                    print(" Can perform: ", end="")
                    moves = ""
                    for attack in item_to_view["attacks"]:
                        moves += attack["name"] + ", "
                    moves = moves[0: (len(moves) - 2)] + "."
                    print(moves)

                case "h-item":\
                    print(" Heals for: " + str(item_to_view["healing-value"]) + "hp when consumed")
                case "d-item":
                    print(" Grants: " + str(item_to_view["buff-value"]) + " bonus damage when used.")
                case "a-item":
                    print(" Grants: " + str(item_to_view["buff-value"]) + " bonus armour when used.")
                case "useless":
                    print()

        p = "-" * len(item_to_view["name"])
        print(f"\\{h}-" + p + f"{h}-/")

        if (item_to_view["item-type"] == "weapon" and in_inv):
            view_or_equip_attacks(item_to_view)

        elif(item_to_view["item-type"] == "armour" and in_inv):
            print("Would you like to equip this piece of armour? (y/n)")
            i = get_player_input().lower()
            if (i == "y" or i == "yes"):
                switch_armour(item_to_view)
                clear()
                print("You put on the " + item_to_view["name"])
    else:
        # Item not present
        clear()
        print("This is not an item")

# Executes the players command after it has been normalised
def execute_command(command):
    global current_place

    if (0 == len(command)):
        clear()
        print("Please enter a valid command")
        return
    elif current_place == None and command[0] != "go":
        clear()
        print("Please enter a valid command")
        return
    elif(command[0] == "return"): # Returns the player to the current city
        execute_move_place()
    elif(len(command) > 2):
        command = combine_words(command)

    # Checks the first word in the command list in order to determine what
    # action the player is trying to do.
    if (command[0] == "go"):
        if (len(command) > 1):
            # Check if the player is moving from a city or a place
            if (current_place == None):
                execute_move_city(command[1])
            else:
                execute_move_place(command[1])

    elif(command[0] == "take"):
        if (len(command) > 1 ):
            execute_take(command[1])
        else:
            clear()
            print("Take what?")

    elif(command[0] == "drop"):
        if (len(command) > 1 ):
            execute_drop(command[1])
        else:
            clear()
            print("Drop what?")

    elif(command[0] == "view"):
        if (len(command) > 1 ):
            execute_view(command[1])
        else:
            clear()
            print("View what?")

    else:
        clear()
        print("Action not valid!")

#function must take a list of items as argument.
def list_of_items(items):
    csl = ""

    for item in items:
        if csl == "":
            csl += item["name"]
        else:
            csl += ", " + item["name"]

    return csl #returns a comma seperated list of values

# Takes the current place, and prints all items within that place
def print_place_items(place):
    items_in_place = place["items"]

    if items_in_place != []:
        print("Items present:", list_of_items(items_in_place) + ".")
    else:
        print("There are no items present.")

# Takes the player's inventory, and prints all items within it
def print_player_items(items):
    if items != []:
        print("Inventory:", list_of_items(items) + ".")
        #print("")
    else:
        print("You have no items.")

 # main gameplay loop running core game functions in the explore phase.
def main():
    global current_place
    global current_city
    global inventory
    global equipped_weapon
    global equipped_armour
    global game_active

    # Print intro
    print("""Around the World in 15 Minutes

             On this quest you must travel round to different cities across the globe and add items that you find to your inventory.
             You must however choose wisely as you can only carry a maximum of 4 items within your inventory.
             You must use these items to defeat the final boss at the end.
             Only the correct combination of items can defeat the boss.
             Your starting position is at Abacws in Cardiff.
             """)

    while game_active:
        # If current_place is none then we are in city
        if (current_place == None):
            print_city(current_city)
            print_city_destinations(current_city)
            player_command = get_player_input()
            command = normalise(player_command)
            execute_command(command)

        else: # We are in a place
            print_place(current_place)
            print("Type RETURN to return to the city")
            print("To take an item type TAKE <item>, to drop type DROP <item>, to view type VIEW <item>")
            print("You must take an item in order to view its properties.")
            print("When viewing an item you must equip yourself with it in order to use it against the boss.")
            print()
            print_place_items(current_place)
            print_player_items(inventory)
            player_command = get_player_input()
            command = normalise(player_command)
            execute_command(command)

if __name__ == "__main__":
    main()
    # --------------------- Code for testing boss phase
    #inventory = [health_item_template, rock, boxers]
    #equipped_weapon = basic_sword
    #equipped_armour = basic_armour
    #intilialise_boss_battle(100, inventory, equipped_weapon, equipped_armour)
