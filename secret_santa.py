# "Secret Santa" 2.0 Takes a list of names and assigns each to another person.

import random
from typing import List


# Sorts santas randomly and matches each with a recipient
def shuffle_santas(santa_list):
    random.shuffle(santa_list)
    for i in range(len(santa_list) - 1):
        print(santa_list[i] + " is giving to " + santa_list[i+1])
    print(santa_list[i+1] + " is giving to " + santa_list[0])


# Accepts user input list and checks for minimum length, passes list to shuffle_santas
def add_santas():
    santa_input_list: List[str] = input().split(" ")
    clean_input_list = list(filter(None, santa_input_list))
    if len(clean_input_list) < 3:
        print("Whoops! Please try three or more names separated by a space.")
        add_santas()
    else:
        shuffle_santas(clean_input_list)


# Request user input of list of names
print("Secret Santa Sorter 2.0; Sorting Santas Since 2019")
print("Please enter 3 or more names separated by spaces, then press enter")

add_santas()



