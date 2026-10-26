    ##### - Practice Problems from Chapter 3 - page 46 - #####


## 3-9 - Dinner Guests:

guest_list = ['kelly', 'megan', 'dahlia', 'genevieve']
print(guest_list)

print(f'\nThe number of guests invited to dinner is: {len(guest_list)}.')  # putting an altered list in a string and producing the length of the list.


## 3-10 - Every Function:

location = ['peru', 'scotland', 'kyoto', 'italy', 'balkins']
print(f'\n Here is an unsorted list: \n{location}\n')


print(location)
print(f'Here is the same list in reversed order (temporarily) within a string:\n{location[::-1]}\n')  # could not get reverse() method to work within the string. gave up lol

print (f'Original list: {location}\n')

location.sort()
print(f'Alphabetical permanent: {location}\n')

location.sort(reverse=True)
print(f'Reverse alphabetical permanent: {location}\n')

# might not be every function, but book has vague instructions and moving on!