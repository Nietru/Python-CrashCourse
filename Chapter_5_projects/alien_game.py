    ##### - Practice Problems from Chapter 5 - page 84 - #####


## 5-3 - Alien Colors #1: if-statement

alien_color_0 = 'green'
alien_color_1 = 'yellow'
alien_color_2 = 'red'

alien_shot = 'green'

if alien_shot is alien_color_0:
    print("\nYou killed a green alien! You just won 5 points!")  # one that works

alien_shot = 'red'

if alien_shot is alien_color_0:
    print("\nYou killed a green alien! You just won 5 points!")  # one that does not work


## 5-5 - Alien Colors #3: if-elif-else chain

alien_shot = 'red'

if alien_shot is alien_color_0:
    print("\nYou killed a green alien! You just won 5 points!") 
elif alien_shot is alien_color_1:
    print("\nYou killed a yellow alien! You just won 10 points!") 
else:
    print("\nYou killed a red alien! You just won 20 points!")  # output


## 5-6 - Stages of Life:

age_1 = 20

if age_1 < 2:
    print("\nYou are a baby.")
elif age_1 < 4: 
    print("\nYou are a toddler.")    # note: tried to use 'and' operator and it would not let me.
elif age_1 <=12:
    print("\nYou are a child.")
elif age_1 < 18:
    print("\nYou are a teenager.")
elif age_1 <=21:
    print("\nYou are a young adult.")
elif age_1 <=55:
    print("\nYou are an adult.")
elif age_1 > 55:
    print("\nYou are a senior citizen.")

