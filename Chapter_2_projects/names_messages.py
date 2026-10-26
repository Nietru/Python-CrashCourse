    ##### - Practice Problems from Chapter 2 - page 25 - #####

### 2-3 - Personal Message:

first_name = "Tifannie"
last_name = "Truman"

person = (f"{first_name} {last_name}")

message = "I hope you feel better.   " # whitespace in beginning, remove.

print(f"{person}, {message}".rstrip())


### 2-4 - Namecases:

print (person.title())
print(person.upper())
print(person.lower())


### 2-6 - Famous Quote 2:

author = "Timothy Levitch"
quote = "On really romantic evenings of self, I go salsa dancing with my confusion."

print(f'{author} once said: "{quote}"')


### 2-7 - Stripping Names:

name_first = "   Thomas     "
name_last = "  Larocque   "

print(f"{name_first} {name_last}")
print(f"{name_first.rstrip()} {name_last.rstrip()}")
print(f"{name_first.lstrip()} {name_last.lstrip()}")
print(f"{name_first.strip()} {name_last.strip()}")
