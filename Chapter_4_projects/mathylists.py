    ##### - Practice Problems from Chapter 4 - page 60 - #####


## 4-4 - One Million:

numbers = []
for  number in range(1, 1000001):  # makes a variable, 'number', to create an element for every number between 1 and a million. 
    numbers.append(number)         # puts the 'number' variable in the 'numbers[]' list.

#print(numbers)   # commented this out to clear up working terminal. #uncomment to see working.
print('\n')

## 4-5 - Summing a Million:
print(min(numbers))
print(max(numbers))  # make sure list actually starts at 1 and ends at 1mil.
print(sum(numbers))  # how fast can python add a million numbers? ..fast.
print('\n')

## 4-6 - Odd numbers:

odd_numbers = []
for number in range(1, 20, 2):  # adds 1, and every second number after (odd)
    odd_numbers.append(number)

print(odd_numbers)
print('\n')

## 4-7 - Threes:

threes = [value+3 for value in range(3, 30, 3)]
for value in threes:    # created forloop to print each element of the list on a single line.
    print(value)

print('\n')

## 4-8 - Cubes:

cubes = [value**3 for value in range(1, 11)]  # this is a list comprehension for cubes. ** = exponent in python. this returns numbers 1 - 10 in the list. 11 is exclusive.
print(cubes)                   