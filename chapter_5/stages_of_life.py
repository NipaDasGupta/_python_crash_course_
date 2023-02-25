"""Stages of Life: Write an if-elif-else chain that determines a person’s
stage of life. Set a value for the variable age, and then:
•	 If the person is less than 2 years old, print a message that the person is
a baby.
•	 If the person is at least 2 years old but less than 4, print a message that
the person is a toddler.
•	 If the person is at least 4 years old but less than 13, print a message that
the person is a kid.
•	 If the person is at least 13 years old but less than 20, print a message that
the person is a teenager.
•	 If the person is at least 20 years old but less than 65, print a message that
the person is an adult.
•	 If the person is age 65 or older, print a message that the person is an
elder."""

age = 3

if age < 2:
    stages_of_life = 'baby'
elif age == 2 or age < 4:
    stages_of_life = 'toddler'
elif age == 4 or age < 13:
    stages_of_life = 'kid'
elif age == 13 or age < 20:
    stages_of_life = 'teenager'
elif age == 20 or age < 65:
    stages_of_life = 'adult'
elif age >= 65:
    stages_of_life = 'elder'

print(f'You are a/an {stages_of_life}.')