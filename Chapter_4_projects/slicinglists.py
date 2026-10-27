    ##### - Practice Problems from Chapter 4 - page 65 - #####


## 4-10 - Slices:

players = ['charles', 'martina', 'michael', 'florence', 'eli']  # using a list from the chapter notes
print(f'The first three items in the list are: {players[:3]}')
print(f'The middle three items in the list are: {players[1:4]}')
print(f'The last three items in the list are: {players[2:]}')

## 4-11: My Pizzas, Your Pizzas:

my_pizzas = ['pepperoni', 'sausage-pineapple', 'philly-steakbomb', 'mediterranean']   
friend_pizzas = my_pizzas[:]  # make new list for friends favorite pizzas, from my_pizzas

my_pizzas.append('bbq-chicken')        # add seperate items to prove they are indeed two separate lists.
friend_pizzas.append('three-cheese')

print('\nMy favorite pizzas are:')    # print to prove with a forloop.
for value in my_pizzas:
    print(value)

print('\nMy friends favorite pizzas are:')
for value in friend_pizzas:
    print(value)
