# "Secret Santa" 2.0 Takes a list of names and assigns each to another person.

import random

# Create a list of all santas
from typing import List
print("Please enter 3 or more names separated by a space, then press enter")


def shuffle_santas(santa_list):
    random.shuffle(santa_list)
    for i in range(len(santa_list) - 1):
        print(santa_list[i] + " is giving to " + santa_list[i+1])
    print(santa_list[i+1] + " is giving to " + santa_list[0])


def add_santas():
    santa_input_list: List[str] = input().split(" ")
    if len(santa_input_list) < 3:
        print("Whoops! Please try three or more names separated by a space.")
        add_santas()
    else:
        shuffle_santas(santa_input_list)

add_santas()



