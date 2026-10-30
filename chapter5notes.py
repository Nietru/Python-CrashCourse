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

# The if-elif-else Chain:

age = 12

if age < 4:
    print('\nYour admission cost = $0')
elif age < 18:
    print('\nYour admission cost = $5.00')  # program only runs elif if the if portion failed, and so on.
else:
    print('\nYour admission cost = $8.00')

# A more concise way of running this program ^ is:

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print(f"Your admission cost = ${price}.00.\n")   # saves time if you need to make changes later on. Change one print stmt instead of 3.

age = 67

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age > 64:  # added a senior discount
    price = 8    
elif age <= 64:  # normal adult full-price. else-block omitted: python does not require an 'else' block.
    price = 10

print(f"Your admission cost = ${price}.00.\n")

# The if-elif-else chain is good for checking ONE condition. If you need to check for more than one, a series of if-statements is the way to go.

requested_toppings = ['mushrooms', 'extra-cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")           # does not print because it is not in the list (customer's pizza order)
if 'extra-cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nPizza is completed!")  # if-elif-else chain would NOT work because the code would stop running after 'mushrooms' - condition would be "met".


# Using if-statements with Lists:

  # if-statements are versatile and you can do interesting work with them when combining lists.

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"\nAdding {requested_topping}")
print("\nPizza Completed!")  # A simple for loop: prints single statement for each item/element in the list.


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']  # adding an if statement for missing ingredient from list:
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("\nSorry, we are out of green peppers right now.")
    else:
        print(f"\nAdding {requested_topping}")
print("\nPizza Completed!") 

# page 86 (bottom)
