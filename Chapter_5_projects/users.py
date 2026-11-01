    ##### - Practice Problems from Chapter 5 - page 89 - #####


## 5-8 - Hello Admin:

usernames = ['admin', 'stephen', 'kathy', 'maddison', 'zack']
username = 'admin'

if username != 'admin':   # forgot and tried with a forloop first and it kept printing all the names. no forloop!
    print(f'\nHello, {username}, welcome back!')
else:
    print(f'\nHello, {username}, would you like a status report?')


## 5-9 - No Users:

users = []
user = ''

if not users:
    print('\nWe need to find some users!')  # cheated on this one. could not get the code to run with the for/if.
else:
    print(f'\nWelcome back, {user}.')


## 5-10 - Checking Usernames:

current_users = ['tifannie', 'monique', 'kyla', 'javier', 'elvin']
new_users = ['tom', 'bill', 'kathy', 'cindy', 'kyla']

for user in new_users:
    if user in current_users:
        print(f'\nUsername: {user.title()} is not available. Please choose a different username.')
    else:
        print(f'\nWelcome! Your new username is {user.title()}.')   # it worked first try! 😭


## 5-11 - Ordinal Numbers:

ord_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for number in ord_nums:
    print(number)  # loop through list.

for number in ord_nums:
    if number == '1':
        print(f'\n{number}st')
    elif number == '2':
            print(f'\n{number}nd')
    elif number == '3':
            print(f'\n{number}rd')
    else:
        print(f'\n{number}th')
