    ##### - Practice Problems from Chapter 3 - page 42 - #####


### 3-4 - Guest List:

guest_list = ['dahlia', 'kelly', 'megan', 'genevieve']
print(guest_list)

print(f"\nAttention: {guest_list[0].title()}! You are cordially invited to my bougie dinner party!")
print(f"Attention: {guest_list[1].title()}! You are cordially invited to my bougie dinner party!")
print(f"Attention: {guest_list[2].title()}! You are cordially invited to my bougie dinner party!")
print(f"Attention: {guest_list[3].title()}! You are cordially invited to my bougie dinner party!")


### 3-5 - Changing Guest List:

not_coming = guest_list.pop(1)  # I chose to use the pop() method to remove kelly from the guest list without losing the ability to use her value in the following statment.
guest_list.append('Dylan')     # adds element to end of list.
print(f"{not_coming.title()} can't make it unfortunately. 😞")

        # reprint invites:
print(f"\nAttention: {guest_list[0].title()}! You are cordially invited to my bougie dinner party!")
print(f"Attention: {guest_list[1].title()}! You are cordially invited to my bougie dinner party!")
print(f"Attention: {guest_list[2].title()}! You are cordially invited to my bougie dinner party!")
print(f"Attention: {guest_list[3].title()}! You are cordially invited to my bougie dinner party!")


### 3-6 - More Guests:

print('\nAttention all guests: I have acquired a more extravagant and accomadating dinner table.\nThis means we have room for 3 more guests! I will be sending out new/better invitations shortly!')