# Dictionaries - A collection of key-value pairs. Can store an almost limitless amount of information. wrapped in braces {...}

alien_0 = {'color': 'green', 'points': 5}  # 'color' and 'points' are Keys. 'green' and '5' are their corresponding values. 
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']   # to call a key-value pair, use square brackets and the 'key' name, like so.
print(f"\nYou just earned {new_points} points!\n")

print(alien_0, '\n')    # adding new key-value pairs to a dictionary:
alien_0['x-position'] = 0
alien_0['y-position'] = 25
print(alien_0, '\n')

alien_0 = {}   # it is sometimes beneficial to start with an empty dictionary.
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

print(f'\nThe alien is {alien_0["color"]}.')
alien_0['color'] = 'yellow'   # changing the value of a key in your dictionary. now the alien is yellow.
print(f'\nThe alien is now{alien_0["color"]}.')


# More interesting usage of changing the values in a dictionary:
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"\nOriginal position: {alien_0['x_position']}")

# move the alien to the right (imagining creating simple video game)

# determine how far to move the alien using its current speed:
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3  # speedy gonzales

alien_0['x_position'] = alien_0['x_position'] + x_increment  # the new position is the old position + the associated x_increment.

print(f'New position: {alien_0['x_position']}\n')  # prints 'New position: 2' because our dictionary has 'medium' value for 'speed'


# Removing key-value pairs:   Be away that deleting a key-val pair permanently removes it.

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

# top page 97
