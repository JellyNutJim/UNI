from contextlib import nullcontext
import math
from operator import truediv
from queue import Empty
import random

density = 0.001

def is_Even(num):
    if (num % 2 == 0):
        return True
    else:
        return False

def calc_waist_size(height, mass):
    v = mass / density
    r = math.sqrt(v / (math.pi * height))
    c = 2 * math.pi * r
    return c

def cm_to_inch(cm):
    return cm / 2.54

def find_max(num_1, num_2, num_3):
    biggest_num = num_1
    if (num_2 > biggest_num):
        biggest_num = num_2
    if (num_3 > biggest_num):
        biggest_num = num_3
    return biggest_num

def get_user_input():
    print("Enter:") 
    return input()

def read_numbers():
    new_input = int(get_user_input())
    max_num = new_input
    min_num = new_input
    num_sum = new_input
    num_count = 1

    while (True):
        new_input = get_user_input()

        if (not new_input):
            break
        else:
            num = int(new_input)
            num_sum += num
            num_count += 1

            if (num > max_num):
                max_num = num;
            elif (num < min_num):
                min_num = num
   

    print("Average: " + str((num_sum / num_count)))
    print("Smallest number: " + str(min_num))
    print("Largest number: " + str(max_num))

def read_numbers2():
    new_input = int(get_user_input())
    max_num = new_input
    min_num = new_input
    num_sum = new_input

    new_input = get_user_input()
    while (new_input):
        num = int(new_input)
        num_sum += num
        num_count += 1
        if (num > max_num):
            max_num = num;
        elif (num < min_num):
            min_num = num

        new_input = get_user_input()
   

    print("Average: " + str((num_sum / num_count)))
    print("Smallest number: " + str(min_num))
    print("Largest number: " + str(max_num))

def get_string_deets(user_input):
    number_of_char = 0
    number_of_digit = 0
    number_of_punc = 0;

    for i in range (len(user_input)):
        if (user_input[i].isalpha()):
            number_of_char += 1
        elif (user_input[i].isdigit()):
            number_of_digit += 1
        else:
            number_of_punc += 1 
    
    print(f"Letters: {number_of_char}")
    print(f"Digits: {number_of_digit}")
    print(f"Punctuation: {number_of_punc}")

def create_pattern(size):
    if (size == 0):
        return
    else:
        for i in range(size, 0, -1):
            print (str(i) + " ", end = '')
    print()
    size -= 1;
    create_pattern(size)
    return

def guess_number():
    my_number = random.randrange(1, 11)
    guess = False
    print("Guess my number!")

    while (guess == False):
        print("Number: ", end = "")
        guessed_num = int(input())

        if (guessed_num > my_number):
            print("My number is smaller")
        elif (guessed_num < my_number):
            print("My number is bigger")
        else:
            print("You guessed my number!!")
            break

    return

def flip_word(word):
    word2 = ""
    for i in range (len(word) - 1, -1, -1):
        word2 += word[i]
    return word2

def is_pallindrome(word):
    flipped_word = flip_word(word)
    if (word == flipped_word):
        return True
    else:
        return False

def numerical_sequence(n):
    while (n != 1):
        print(n)
        if (n % 2 == 0):
            n = n/2
        else:
            n = (3 * n) + 1
    print(n)


print("Enter number: ", end = "")
number = int(input())
numerical_sequence(number)





'''
max_num = 0
min_num = 0
num_sum = 0
num_count = 1

print("Enter word")

word = input()

print(is_pallindrome(word))

print("Enter pattern size")

size = int(input())

create_pattern(size)

print("Enter your string:")

user_string = input()

get_string_deets(user_string)


for i in range (99, 0, -1):
    print(f"{str(i)} bottles of beer on the wall, {str(i)} bottles of beer.\nTake one down, pass it around")

print("Please enter three numbers")

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(find_max(num_1, num_2, num_3))

print("Please enter height(cm) and weight(kg)")
height = int(input())
weight = int(input())

print(cm_to_inch(calc_waist_size(height, weight)))

'''


