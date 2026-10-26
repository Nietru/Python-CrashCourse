first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

message = (f"Hello, {full_name.title()}!") # the "f" replaces ".format()" and allows for inline variable substitution
print(message)