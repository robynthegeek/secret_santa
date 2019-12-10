# "Secret Santa" 2.0 Takes a list of names and assigns each to another person.

import random

# Create a list of all santas

print("Please enter 3 or more names separated by a space, then press enter")


santa_list = input().split(" ")

if len(santa_list) < 3: print("Whoops! Please try three or more names separated by a space.")

random.shuffle(santa_list)
for i in range(len(santa_list) - 1):
    print(santa_list[i] + " is giving to " + santa_list[i+1])
print(santa_list[i+1] + " is giving to " + santa_list[0])


