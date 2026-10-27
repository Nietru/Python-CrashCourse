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

# A list Comprehension: consolidates many lines of code into a single line of code, producing the same result.

squares = [value**2 for value in range(1, 11)]
print(squares)
