# So I am scrapping this approach because if there is the same gifter and
    # recipient left last on both lists it will cause a bug. Instead I will just
    # scramble a second list, which should be shorter anyway.



# "Secret Santa" Takes a list of names and assigns each to another person.

from random import randint

# Create a list of all santas and all giftees

santa_list = ["one", "two", "three", "four", "five"]
giftee_list = santa_list.copy()

def select_recipient():

    # Select the first santa in line and remove this santa from the master list
    gifter = santa_list[0]
    santa_list.remove(gifter)

    # make a working list of recipients and remove our gifter if not already gone
    recipient_list = giftee_list.copy()
    if gifter in recipient_list:
        recipient_list.remove(gifter)

    # Display given santa with a randomly selected recipient
    recipient_list_length = len(recipient_list)
    print(recipient_list_length)
    if recipient_list_length <= 0: ##Fix randint bug when list is empty https://stackoverflow.com/questions/18161513/
        recipient_index = 0
    else:
        recipient_list_length -= 1
        print(recipient_list_length)
        recipient_index = randint(0, recipient_list_length)
    recipient_name = recipient_list[recipient_index]
    print(gifter + " is giving to: " + recipient_name)

    # Remove giftee from master list of recipients
    giftee_list.remove(recipient_name)

# Iterate over list until all santas are assigned
for i in range(len(santa_list)):
    print(i + 1.0)
    select_recipient()

