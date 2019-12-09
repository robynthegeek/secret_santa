##"Secret Santa" Takes a list of names and assigns each to another person.

from random import randint

name_list = ["Hilary", "Rich", "Roz", "Derek", "Robyn", "Cory", "Monica", "Peter", "Vicky", "Kathryn"]
list_length = len(name_list)
match_index = randint(0, list_length)

print(name_list)
