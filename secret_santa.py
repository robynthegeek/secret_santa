##"Secret Santa" Takes a list of names and assigns each to another person.

from random import randint

##Create a list of all santas
santa_list = ["Hilary", "Rich", "Roz", "Derek", "Robyn", "Cory", "Monica", "Peter", "Vicky", "Kathryn"]
gifter = santa_list[0]

##Remove our gifter from the list of recipients
santa_list.remove(gifter)
recipient_list = santa_list
print(recipient_list)

##Select a random recipient
recipient_index = randint(0, (len(recipient_list)-1))
recipient_name = recipient_list[recipient_index]
##Display gifter and recipient
print(gifter + " is giving to: " + recipient_name)

recipient_list.pop(recipient_index)
print(recipient_list)

##print(recipient_list)
