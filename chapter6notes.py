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

# page 95 - top