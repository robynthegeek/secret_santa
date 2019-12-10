# "Secret Santa" 2.0 Takes a list of names and assigns each to another person.

from random import shuffle

# Create a list of all santas
santa_list = ["one", "two", "three", "four", "five"]

shuffle(santa_list)
for i in range(len(santa_list) - 1):
    print(santa_list[i] + " is giving to " + santa_list[i+1])
print(santa_list[i+1] + " is giving to " + santa_list[0])