# define a string variable and print it out
name = 'Eric'
print(f"Hello {name}, would you like to learn some Python today?")
print()

# define a string varibale and print out in change cases 
# uses three built-in methods: lower(), upper(), title()
# lower() method returns a lower case string variables
# upper() method returns a upper case string variables
# title() method return a captial letter string variables
name = "eric"
print(f"Hello {name.lower()}, would you like to learn some Python today?")
print(f"Hello {name.upper()}, would you like to learn some Python today?")
print(f"Hello {name.title()}, would you like to learn some Python today?")
print()

famous_quote = """Albert Einstein once said, “A person who never made a
mistake never tried anything new.”"""
print(famous_quote)
print()

famous_person = "Albert Einstein"
message = 'once said, “A person who never made a mistake never tried anything new.”'
print(f"{famous_person} {message}")
print()

name = " ada\t\nlovelace "
print(name.lstrip())
print(name.rstrip())
print(name.strip())
print()