#Lists:

bicycles = ['trek', 'cannondale', 'speacialized', 'redline', 'diamondback']  # list is in square brackets. stays in order, and can be altered.
print(bicycles)

print(bicycles[0])  # first "index" in a list starts at 0. if there are five elements in a list, the fifth one is found at index 4.
print(bicycles[4])
print(bicycles[-1])  # likewise, -1 will print the very last element in a list.

message = f"my first bicycle was a {bicycles[1].title()}."  # f is shorthand python built-in meaning "format". and .title() capitalizes the word.
print(message)


# modifying lists:
bicycles[2] = 'schwinn'  #replaces index 2 (the third element)
print(bicycles)

bicycles.append('huffy')  # append adds it to the end of the list.
print(bicycles)

del bicycles[1]  # deletes an element from list.
print(bicycles, '\n')

bicycles.pop()   # pop method removes element from a list as well, but you can still access and use that element.
print(bicycles,'\n')

popped_bicycle = bicycles.pop()
print(popped_bicycle)

bike_selected = bicycles.pop(1)
print(f"I would like to purchase the {bike_selected.title()}.")

bicycles.insert(0, 'bmx')  # insert method adds element in specific location of list.
print(bicycles)

# remember that when you use pop() method, it is no longer stored in your list. 

#if you dont know the position of the element in a (longer) list, but you want to remove it, you can use the element value:
bicycles.remove('bmx')
print(bicycles)

# removing an element with its assigned name value, with an explaination:
too_expensive = 'redline'
bicycles.remove(too_expensive)
print(bicycles)
print(f"\nA {too_expensive.title()} is too expensive for me.\n")


# Organizing a List:

cars = ['bmw', 'toyota', 'subaru', 'audi']
cars.sort()  # sorts alphabetically.
print(cars)

cars.sort(reverse=True)  # reverse alphabetical.
print(cars)

cars = ['bmw', 'toyota', 'subaru', 'audi']  # make the list unorganized again.
print("\n Here is the original list:")
print(cars)

print('\n Here is the temporarily sorted list:')
print(sorted(cars))  # temporarily sorts without changing original list.

print('\n Here is the original list, again:')
print(cars)

# the reverse() method does not put the list in reverse-alphabetical order. it only reverses the original list:
cars.reverse()
print('\n Here is the list in reverse order:')
print(cars)

print(len(cars)) # len function - gives you the length (in elements) of any list. (starts with number 1, not 0)
