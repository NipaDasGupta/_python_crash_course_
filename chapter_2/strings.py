# """create a variable called message and define it to "hello there!"
#    it will display the variable, message"""
message = """hello there!"""
print(message)

name = 'ada lovelace'
print(name.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"

print(f"{first_name} {last_name}")

# alternative way
print("{} {}".format(first_name,last_name))

print(f"Hello, {first_name.title()} {last_name.title()}!")

# to add a tab in your text: \t
# to add a newline in a string: \n

print("\nPython\nC\n\tJava\n\t\tPHP")


favorite_language = ' python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())