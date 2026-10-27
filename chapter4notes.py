# Working with Lists:

magicians = ['alice', 'david', 'merlin']
for magician in magicians:  # the variable name: 'magician' is arbitrary, but this way is common practice. The colon tells program to loop the indented lines that follow.
    print(magician)  # prints each element (name) on a new line \n 
     # ^ print statement must be indented to be included in the forloop.


for magician in magicians:
    print(f'\n{magician.title()}, that was a great trick!') # prints for each element (magician in the list).
    print(f"I can't wait to see your next trick, {magician.title()}!")

print('\nThank-you everyone! That was a great show!')  # not indented, so it is NOT included in the loop. prints once, as normal.


# Numerical Lists:

for value in range(1, 5):  # prints indexes: remember that the second number is exclusive in a range and the first number is inclusive.
    print(value)

print('\n')

for value in range(1, 6): # prints 1 - 5 in terminal 
    print(value)

print('\n')

numbers = list(range(1,6)) # created a list of numbers 1 - 5
print(numbers)

print('\n')
      
even_nums = list(range(2, 11, 2)) # printing even numbers 1 - 10
print(even_nums)

print('\n')



squares = []
for value in range(1, 11): # 'value' is the new variable for each number from 1 to ten, given in this range
    square = value **2  # 'square' is the new variable that is equal to each 'value' to the second power (** mean exponent)
    squares.append(square)  # append the list 'squares' with the new 'square' value (the range to the second power in this example)

print(squares) # output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Shortcut - same result :  # somethimes using a temporary variable is necessary, like in the above example ^ but usually not the case.

cubes = []
for value in range(1, 11):
    cubes.append(value**3)

print(cubes)

print ('\n')


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits)) # minimum in the list of numbers, 0
print(max(digits)) # maximum in the list of numbers, 9
print(sum(digits)) # sum, 45

print('\n')

squares = [value**2 for value in range(1, 11)] # a 'List Comprehension' consolidates many lines of code into a single line of code, producing the same result.
print(squares)


# Working with Part of a List:

players = ['charles', 'martina', 'michael', 'florence', 'eli'] # slicing does not change the original list.
print(players[0:3])  # remember the 3 is exclusive so output will inclued indexed 0 - 2
print(players[:4])  # omit first number in a slice, python starts at beg. of list.
print(players[2:])  # omit last number in slice, python goes to end of list.
# remember a negative input, in a slice for this example, works backwards from the end of a list. 
print(players[-3:]) # what happens here:  list['omit', 'omit', -3, -2, -1]  keeps the last 3 elements only. 

print('\n')


# Looping through a slice:

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())



# Copying a List:

my_foods = ['pizza', 'falafel', 'carrot-cake']
friend_foods = my_foods[:]   # copies exact list to a completely new list. if we had used 'friend_foods = my_foods' it would have just changed the variable/name of the same list. 
print(f'\nMy favorite foods are: \n{my_foods}')
print(f"\nMy friend's favorite foods are: \n{friend_foods}")  

my_foods.append('cannoli')    # add different items to the lists to prove they are separate independent lists. 
friend_foods.append('french-fries')
print(f'\nMy favorite foods are: \n{my_foods}')
print(f"\nMy friend's favorite foods are: \n{friend_foods}\n")


#### Tuples: Lists that cannot change - "immutable" in development terminology  ####

# Defining a Tuple:

dimensions = (200, 50)    # tuples use parenteses instead of square brackets like regular lists.
print(dimensions[0])
print(dimensions[1])
print('\n')

#dimensions[0] = 250      # Output: 'TypeError: 'tuple' object does not support item assignment'  Cannot perform a change to a tuple.
#print(dimensions)

# tuples are defined by the comma, the parenthesis are just for readability. So even with one item in the tuple, you must have a trailing comma. ex: tup = (3,)

for dimension in dimensions:
    print(dimension)     # forloops work the same for tuples as lists.
print('\n')

# Writing over a Tuple:

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
print('\n')

dimensions = (300, 500) 
print("Modified dimensions:")   # you can change a tuple by redefining the variable associated with it. Not able to just change the elements.
for dimension in dimensions:
    print(dimension)
print('\n')

