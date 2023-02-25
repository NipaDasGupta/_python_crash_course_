from matplotlib.style import available


course_name = 'machine learning'

print("Is course_name == 'Machine Learning'? I predict False.") 
print(course_name == 'Machine Learning')

print("\nIs course_name != 'deep learning'? I predict True.") 
print(course_name != 'deep learning')

print("\nIs course_name.title() == 'Machine Learning'? I predict True.") 
print(course_name.title() == 'Machine Learning')

name = 'Ada Lovalace'
print("\nIs name == 'ada lovalace'? I predict False.") 
print(name == 'ada lovalace')

print("\nIs name.lower() == 'ada lovalace'? I predict True.") 
print(name.lower() == 'ada lovalace')

requested_toppings = 7
print("\nIs requested_toppings == 5? I predict False.") 
print(requested_toppings == 5)

print("\nIs requested_toppings != 5? I predict True.") 
print(requested_toppings != 5)

print("\nIs requested_toppings < 5? I predict False.") 
print(requested_toppings < 5)

print("\nIs requested_toppings <= 5? I predict False.") 
print(requested_toppings <= 5)

print("\nIs requested_toppings > 5? I predict True.") 
print(requested_toppings > 5)

print("\nIs requested_toppings >= 5? I predict True.") 
print(requested_toppings >= 5)

available_toppings = 5
print("\nIs requested_toppings >= 5 and available_toppings >= 5? I predict True.") 
print(requested_toppings >= 5 and available_toppings >= 5)

print("\nIs requested_toppings <= 5 or available_toppings <= 5? I predict True.") 
print(requested_toppings <= 5 or available_toppings <= 5)
