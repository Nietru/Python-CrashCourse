first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

message = (f"Hello, {full_name.title()}!") # the "f" replaces ".format()" and allows for inline variable substitution
print(message)

# adding whitespace

print("\n\tPython") # \n adds a new line, \t adds a tab space
print("Python")

print("Languages:\nPython\nC\nJavaScript") # \n adds a new line after each language
print("Languages:\n\tPython\n\tC\n\tJavaScript") # \t adds a tab space before each language

fave_language = "  python  " #put spaces before and after the string
print(fave_language) # prints the string with spaces
print(fave_language.rstrip()) # prints the string with trailing whitespace removed
print(fave_language.lstrip()) # prints the string with leading whitespace removed
print(fave_language.strip()) # prints the string with both leading and trailing whitespace removed

# use double quotes in strings first.
message1 = "One of my favorite languages is Python."
print(message1) 

#message2 = 'Python's a great language'       wont run because of the apostrophe cancelling out the single quotes
#print(message2)
