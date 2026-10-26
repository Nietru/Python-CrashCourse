    ##### - Practice Problems from Chapter 3 - page 42 - #####


### 3-4 - Guest List:

guest_list = ['dahlia', 'kelly', 'megan', 'genevieve']
print(guest_list)

print(f"\nAttention: {guest_list[0].title()}! You are cordially invited to my bougie dinner party!")
print(f"Attention: {guest_list[1].title()}! You are cordially invited to my bougie dinner party!")
print(f"Attention: {guest_list[2].title()}! You are cordially invited to my bougie dinner party!")
print(f"Attention: {guest_list[3].title()}! You are cordially invited to my bougie dinner party!")


### 3-5 - Changing Guest List:

not_coming = guest_list.pop(1)  # I chose to use the pop() method to remove kelly from the guest list without losing the ability to use her value in the following print statment.
guest_list.append('Dylan')     # adds element to end of list.
print(f"{not_coming.title()} can't make it unfortunately. 😞")

        # reprint invites:
print(f"\nAttention: {guest_list[0].title()}! You are cordially invited to my bougie dinner party!")
print(f"Attention: {guest_list[1].title()}! You are cordially invited to my bougie dinner party!")
print(f"Attention: {guest_list[2].title()}! You are cordially invited to my bougie dinner party!")
print(f"Attention: {guest_list[3].title()}! You are cordially invited to my bougie dinner party!")


### 3-6 - More Guests:

print('\nAttention all guests: I have acquired a more extravagant and accomadating dinner table.\nThis means we have room for 3 more guests! I will be sending out new/better invitations shortly!\n')

guest_list.insert(0, 'lariah') # use insert for beginning of list.
guest_list.insert(2, 'caleb')  # use insert for middle of list.
guest_list.append('thomas')  # add someone to end of a list. this is what the append() method is used for.

print(guest_list)

        # reprint invites:
print(f"\nAttention: {guest_list[0].title()}! You are cordially invited to my bougie dinner party!")
print(f"Attention: {guest_list[1].title()}! You are cordially invited to my bougie dinner party!")
print(f"Attention: {guest_list[2].title()}! You are cordially invited to my bougie dinner party!")
print(f"Attention: {guest_list[3].title()}! You are cordially invited to my bougie dinner party!")
print(f"Attention: {guest_list[4].title()}! You are cordially invited to my bougie dinner party!")
print(f"Attention: {guest_list[5].title()}! You are cordially invited to my bougie dinner party!")
print(f"Attention: {guest_list[6].title()}! You are cordially invited to my bougie dinner party!")


### 3-7 - Shrinking Guest List:

print('\nAttention Guests: I am very sorry to announce that my new dinner table will NOT arrive on time. I can only invite 3 people to my amazing snobby dinner! :(')
print(f'\n{guest_list}')

    # alert un-invited guests and remove from list:
popped_guest = guest_list.pop(0)   # removed first element 'lariah'
message = (f'\nBecause of the delay in the arrival of my new dinner table, I will not be able to invite you. I am sorry, {popped_guest.title()}!')
print(message)

popped_guest = guest_list.pop(1)   # removed second element 'caleb'
message = (f'\nBecause of the delay in the arrival of my new dinner table, I will not be able to invite you. I am sorry, {popped_guest.title()}!')
print(message)

popped_guest = guest_list.pop(1)  # removed updated second element, 'megan'
message = (f'\nBecause of the delay in the arrival of my new dinner table, I will not be able to invite you. I am sorry, {popped_guest.title()}!')
print(message)

popped_guest = guest_list.pop(2)  # list updated: this removed third element, 'Dylan'
message = (f'\nBecause of the delay in the arrival of my new dinner table, I will not be able to invite you. I am sorry, {popped_guest.title()}!')
print(message)

print(f'\n{guest_list}')

        # resend invites:
print(f'\nDespite the unfortunate delay in the arrival of my new dinner table, you are still invited to my gorgeous feast, {guest_list[0].title()}!')
print(f'\nDespite the unfortunate delay in the arrival of my new dinner table, you are still invited to my gorgeous feast, {guest_list[1].title()}!')
print(f'\nDespite the unfortunate delay in the arrival of my new dinner table, you are still invited to my gorgeous feast, {guest_list[2].title()}!')

del guest_list[0]  # deletes first element
del guest_list[0]  # deletes next first element
del guest_list[0]


# better way to clear a list is to just use the guestlist.clear() method but that was not in the book. 

print(f'\n{guest_list}')