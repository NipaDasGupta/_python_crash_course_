# Python Crash Course - Quick Start Guide

## Getting Started in 5 Minutes

This guide provides immediate examples for the most commonly used APIs in the Python Crash Course repository.

## Essential Imports

```python
# Core classes
from chapter_9.car import Car
from chapter_9.restaurant import Restaurant
from chapter_9.user import User

# Utility functions
from chapter_11.name_function import get_formatted_name
from chapter_8.user_profile import build_profile

# File operations
from chapter_10.word_count import count_word_1
from chapter_11.survey import AnonymousSurvey
```

## 1. Working with Classes

### Car Management (Most Popular)
```python
from chapter_9.car import Car

# Create and use a car
car = Car("toyota", "camry", 2023)
print(car.get_decriptive_name())  # "2023 Toyota Camry"

# Manage odometer
car.update_odometer(1000)
car.increment_odometer(50)
car.read_odometer()  # "This car has 1050 miles on it."
```

### User Management
```python
from chapter_9.user import User

# Create user
user = User("john", "doe", 30, "seattle")
user.describe_user()
user.greet_user()

# Track login attempts
user.increment_login_attempts()
print(f"Attempts: {user.login_attempts}")  # 1
user.reset_login_attempts()
```

### Restaurant Operations
```python
from chapter_9.restaurant import Restaurant

# Create and manage restaurant
restaurant = Restaurant("joe's diner", "american")
restaurant.describe_restaurant()

# Track customers
restaurant.set_number_served(50)
restaurant.increment_number_served(10)
restaurant.read_number_served()  # "The restaurant has served 60 customers."
```

## 2. Essential Functions

### Name Formatting
```python
from chapter_11.name_function import get_formatted_name

# Format names
name1 = get_formatted_name("john", "doe")
name2 = get_formatted_name("jane", "smith", "marie")
print(name1)  # "John Doe"
print(name2)  # "Jane Marie Smith"
```

### User Profiles
```python
from chapter_8.user_profile import build_profile

# Build flexible user profiles
profile = build_profile("alice", "johnson",
                       age=25,
                       city="portland",
                       occupation="developer",
                       hobby="photography")
print(profile)
# {'first_name': 'alice', 'last_name': 'johnson', 'age': 25, 'city': 'portland', 'occupation': 'developer', 'hobby': 'photography'}
```

## 3. File Operations

### Word Counting
```python
from chapter_10.word_count import count_word_1

# Count words in files (handles errors gracefully)
files = ["chapter_10/alice.txt", "chapter_10/programming.txt"]
for filename in files:
    count_word_1(filename)
```

### File Reading
```python
from chapter_10.read_files import read_files

# Safe file reading
try:
    read_files("chapter_10/alice.txt")
except FileNotFoundError:
    print("File not found")
```

## 4. Survey System

### Data Collection
```python
from chapter_11.survey import AnonymousSurvey

# Create and run survey
survey = AnonymousSurvey("What's your favorite programming language?")

# Collect responses
responses = ["Python", "JavaScript", "Java"]
for response in responses:
    survey.store_response(response)

# Display results
survey.show_question()
survey.show_results()
```

## 5. Advanced Examples

### Electric Car with Battery
```python
from chapter_9.electric_car import ElectricCar

# Create electric car
tesla = ElectricCar("tesla", "model 3", 2023)
print(tesla.get_decriptive_name())

# Use battery features
tesla.battery.describe_battery()
tesla.battery.get_range()
tesla.battery.upgrade_battery()
tesla.battery.get_range()  # Shows improved range
```

### Inheritance Example
```python
from chapter_9.icecreamstand import IceCreamStand

# Ice cream shop (inherits from Restaurant)
shop = IceCreamStand("sweet treats", "dessert")
shop.describe_restaurant()  # Inherited method
shop.show_flavors()         # Specific method
```

### Admin User
```python
from chapter_9.admin import Admin

# Create admin with privileges
admin = Admin("bob", "admin", 40, "headquarters")
admin.describe_user()  # Inherited from User
admin.privileges.show_privileges()  # Admin-specific
```

## 6. Testing Your Code

### Basic Testing
```python
import unittest
from chapter_11.name_function import get_formatted_name

class TestNameFunction(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()
```

### Survey Testing
```python
import unittest
from chapter_11.survey import AnonymousSurvey

class TestSurvey(unittest.TestCase):
    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        
    def test_store_single_response(self):
        self.my_survey.store_response('English')
        self.assertIn('English', self.my_survey.responses)
```

## 7. Common Patterns

### Error Handling Pattern
```python
def safe_file_operation(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Sorry, {filename} not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
```

### Class Initialization Pattern
```python
class MyClass:
    def __init__(self, required_param, optional_param=None):
        self.required = required_param
        self.optional = optional_param or "default_value"
        self.counter = 0  # Always initialize all attributes
```

### Function with Flexible Arguments
```python
def flexible_function(required_arg, *args, **kwargs):
    """Handle variable arguments like make_pizza() functions."""
    print(f"Required: {required_arg}")
    for arg in args:
        print(f"Optional: {arg}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

## 8. Best Practices Summary

### Do This ✅
```python
# Good: Clear names and docstrings
def calculate_total_price(items, tax_rate=0.08):
    """Calculate total price including tax."""
    subtotal = sum(item.price for item in items)
    return subtotal * (1 + tax_rate)

# Good: Proper error handling
try:
    result = risky_operation()
except SpecificError as e:
    handle_error(e)
```

### Avoid This ❌
```python
# Bad: Unclear names
def calc(x, y=0.08):
    return x * (1 + y)

# Bad: Bare except
try:
    risky_operation()
except:
    pass  # Silent failures are hard to debug
```

## 9. Quick Reference

### Most Used Classes
- `Car` - Vehicle management with odometer
- `Restaurant` - Business with customer tracking  
- `User` - Account with login attempts
- `AnonymousSurvey` - Data collection system

### Most Used Functions
- `get_formatted_name()` - Name formatting
- `build_profile()` - Flexible user profiles
- `count_word_1()` - File word counting
- `make_pizza()` - Variable arguments example

### File Operations
- Always use `with open()` for file handling
- Handle `FileNotFoundError` explicitly
- Use JSON for data persistence

### Testing
- Use `unittest.TestCase` for test classes
- Use `setUp()` for test initialization
- Test both success and failure cases

## Next Steps

1. **Explore the full API documentation**: See `API_DOCUMENTATION.md` for complete details
2. **Run the examples**: Copy code snippets and try them yourself
3. **Check the tests**: Look at `chapter_11/` for testing examples
4. **Modify and experiment**: Change parameters and see what happens

## Common Issues & Solutions

### Import Errors
```python
# If you get import errors, make sure you're in the right directory
import sys
sys.path.append('/path/to/python-crash-course')
```

### File Not Found
```python
# Use relative paths from the project root
filename = "chapter_10/alice.txt"  # Not just "alice.txt"
```

### Testing Issues
```python
# Run tests from project root
python -m unittest chapter_11.test_name_function
# Not: python chapter_11/test_name_function.py
```

This quick start guide covers the most essential APIs and patterns. For complete documentation, see the full API documentation file.