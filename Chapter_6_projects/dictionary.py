    ##### - Practice Problems from Chapter 6 - page 99 - #####


## 6-1 - Person:

person_1 = {
    'first_name': 'john',
    'last_name': 'adoneous',
    'age': 44,
    'city': 'peabody',
}
print(person_1)


## 6-1 - Favorite Numbers:

favorite_nums = {
    'tifannie': 1,
    'dahlia': 13,
    'genevieve': 67,
    'edwardo': 4,
    'stephen': 32,
}

for person, number in favorite_nums.items():  # had to look it up, for the items() part. 
    print(person.title(),'=', number)  # prints with spacing... interesting.


## 6-3 - Glossary:

glossary = {
    'dictionary': 'A collection of key-pair values.',
    'list': 'A collection of items in a particular order.',
    'variable': 'A storage word for a specific value.',
    'else-block': 'A catch-all statement that matches any condition not matched by a specific if or elif test.',
    'boolean': 'A test that results in True or False exclusively.',
}

for word, definition in glossary.items():  # had to look it up, for the items() part. 
    print(('\n'),word.title(),':', definition)  # put '\n' in parentesis for it to work correctly.
