import time
import os

def clear():
    os.system("cls")

bus =[
"_________________________________",
"|   | |  | |  | |  | |  | | |   |",
"|   |_|  |_|  |_|  |_|  |_| |___|",
"|_______________________________|",
"  |_|     |_|       |_|     |_|"
]

plane = [
"|\\",
"| \_____________________________",
"|   |_|  |_|  |_| ______ |_|  |_\\",
"|_______________________________/"
]

def travel_animation(vehicle):
    counter = 0
    while counter < 60:
        clear()
        for line in vehicle:
            print(counter * ' ' + line)
        time.sleep(.01)
        counter += 2
    clear()
