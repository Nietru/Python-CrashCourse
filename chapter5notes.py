# Conditional Tests 

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car =='bmw':  # test elements to see if a car title that needs to be all uppercase is ran.
        print(car.upper())  # output will now capitalize all of the letters in BMW when used from list.
    else:
        print(car.title())  # all other cars will only use title() to capitalize the first letter. > Run
print('\n')

# Checking for Equality:

car = 'bmw'  # sets value of car to bmw
print(car == 'bmw')  # tests if car is set to bmw  '==' checks if something is True or False (boolean)
# >>>True

car = 'audi'
print(car == 'bmw')
# >>>False

car = 'Audi'
print(car == 'audi')
# >>>False

car = 'Audi'
print(car.lower() == 'audi')  # lower() will not change the actual formatting of 'Audi' in the list. 
# >>>True


# Checking for inequality:

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':  # != means 'not equal to'
    print('\nHold the anchovies!')

answer =  17         # users answer
if answer != 42:     # correct answer is 42
    print('\nThat is not the correct answer, try again!\n')


# Various mathematical comparisons:

age = 19

print(age < 21)
print(age > 20)
print(age <=21)
print(age !=19)

# Checking multiple conditions: and operator
print('\n')

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21) # check if both ages are atleast 21

age_1 = 21   # change age_1 to be 21
print(age_0 >= 21 and age_1 >=21)  # check if both ages are atleast 21 now.

# Checking multiple conditions: or operator
print('\n')

age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21) # only one or the other must be true. output is true.

age_0 = 18
print(age_0 >= 21 or age_1 >= 21) # now both ages are 18, so neither are true. output is false.

# Checking if values are/are not in a list:
print('\n')

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)  # true
print('pepperoni' in requested_toppings)  # false
print('\n')

banned_users = ['andrew', 'caroline', 'david']
user = 'marle'

if user not in banned_users:
    print(f'{user.title()}, you can post a response.')

