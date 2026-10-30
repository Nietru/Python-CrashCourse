    ##### - Practice Problems from Chapter 5 - page 78 - #####


## 5-1 - Conditional Tests:

car = 'subaru'
print('Is car == subaru? I predict True.')
print(car == 'subaru')
print('\n')


age_0 = 16
age_1 = 22

print('I predict False: Both people are NOT 18:')    # using and operator.
if age_0 >= 18 and age_1 >= 18:
    print('Both people are atleast 18 years old. You may enter!')
else:
    print('Both people are NOT 18 years old. You may not enter, sorry!\n')


print('I predict True: Atleast one person is old enough to buy rated R movie tickets:')  # using or operator.
if age_0 or age_1 >=21:
    print('True: Atleast one of these friends is old enough to purchase rated R movie tickets.\n')
else:
    print('False: neither of these people are over age 18. They cannot purchase rated R movie tickets.\n')


## 5-2 - More Conditional Tests:

car = 'AUDI'
print(car == 'Audi')   # false because of capitalization.
print(car.lower() == "audi")  # true with lower()


existing_users = ['Tifannie', 'Dahlia', 'Genevieve', 'Sarah']
user = 'Tifannie'

if user in existing_users:
    print('\nThis username already exists. Please choose a different username.')
else:
    print('This username is available (: Please proceed to the next step.)')

pizza_toppings = ['pepperoni', 'pineapple', 'bacon']
requested_topping = 'anchovy'

if requested_topping not in pizza_toppings:
    print('\nSpecial order coming through!')
else:
    print('\nMake the usual!')