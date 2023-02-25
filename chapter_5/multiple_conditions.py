age_0 = 22
age_1 = 18
"""Using 'and' to Check Multiple Conditions:
To check whether two conditions are both True simultaneously, 
use the keyword 'and' to combine the two conditional tests; 
if each test passes, the overall expression evaluates to True.
If either test fails or if both tests fail, the 
expression evaluates to False."""
print("Is age_0 >= 21 and age_1 >= 21? I predict False.")
print(age_0 >= 21 and age_1 >= 21)

age_1 = 21 # modified
print("\nIs age_0 >= 21 and age_1 >= 21? I predict True.")
print(age_0 >= 21 and age_1 >= 21)


"""Using 'or' to Check Multiple Conditions:
The keyword 'or' allows you to check multiple conditions as well, but it 
passes when either or both of the individual tests pass. An or expression 
fails only when both individual tests fail."""
age_0 = 22
age_1 = 18
print("\nIs age_0 >= 21 or age_1 >= 21? I predict True.")
print(age_0 >= 21 or age_1 >= 21)

age_0 = 19 # modified
print("\nIs age_0 >= 21 or age_1 >= 21? I predict False.")
print(age_0 >= 21 or age_1 >= 21)