##"Secret Santa" Takes a list of names and assigns each to another person.

from random import randint

##Create a list of all santas and all giftees

santa_list = ["Hilary", "Rich", "Roz", "Derek", "Robyn", "Cory", "Monica", "Peter", "Vicky", "Kathryn"]
giftee_list = santa_list.copy()

def select_recipient():

    ##Select the next santa and remove our gifter from the master list of santas
    gifter = santa_list[0]
    santa_list.remove(gifter)

    ##make a working list of recipients and remove our gifter if not already gone
    recipient_list = giftee_list.copy()
    if gifter in recipient_list: recipient_list.remove(gifter)
    ##Select a random recipient
    recipient_index = randint(0, (len(recipient_list)-1))
    recipient_name = recipient_list[recipient_index]

    ##Display gifter and recipient
    print(gifter + " is giving to: " + recipient_name)

    ##Remove giftee from master list of recipients
    giftee_list.remove(recipient_name)
    print(santa_list)


for i in range(len(santa_list)):
    select_recipient()