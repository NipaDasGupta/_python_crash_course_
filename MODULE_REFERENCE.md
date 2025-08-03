# Python Crash Course - Module Reference Guide

## Overview

This reference guide organizes all public APIs by module/chapter and demonstrates how components interact with each other.

## Chapter 1: Hello World
**Focus**: Basic Python syntax and output

### Key Scripts
- `hello_world.py` - Basic print statements

**Learning Concepts**: Python syntax, print function, basic program structure

---

## Chapter 2: Variables and Simple Data Types
**Focus**: String manipulation, numbers, and basic data types

### Key Scripts
- `strings.py` - String methods and formatting
- `numbers.py` - Numeric operations
- `name_cases.py` - String case manipulation

### Notable Functions
```python
# String formatting examples from various scripts
name = "ada lovelace"
print(name.title())    # Ada Lovelace
print(name.upper())    # ADA LOVELACE
print(name.lower())    # ada lovelace
```

**Learning Concepts**: Variables, string methods, f-strings, numeric operations

---

## Chapter 3: Introducing Lists
**Focus**: List creation, manipulation, and basic operations

### Key Scripts
- `lists.py` - Comprehensive list operations
- `tutorial_1.py`, `tutorial_2.py`, `tutorial_3.py` - Progressive list examples

### Core List Operations
```python
# From lists.py patterns
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')        # Add to end
motorcycles.insert(0, 'kawasaki')   # Insert at position
motorcycles.remove('yamaha')        # Remove by value
popped = motorcycles.pop()          # Remove and return last
```

**Learning Concepts**: List methods, indexing, slicing, list modification

---

## Chapter 4: Working with Lists
**Focus**: Loops, list comprehensions, and advanced list operations

### Key Scripts
- `magicians.py` - For loops with lists
- `numerical_lists.py` - Numeric list operations
- `slices.py` - List slicing techniques
- `buffets.py` - Tuple operations

### Essential Patterns
```python
# Loop patterns from magicians.py
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

# Numerical operations from numerical_lists.py
numbers = list(range(1, 6))
squares = [value**2 for value in range(1, 11)]
```

**Learning Concepts**: For loops, range(), list comprehensions, tuples

---

## Chapter 5: If Statements
**Focus**: Conditional logic and boolean operations

### Key Scripts
- `cars.py` - Conditional formatting
- `alien_color.py` - Multi-condition examples
- `conditional_test.py` - Boolean operations
- `stages_of_life.py` - Age-based conditions

### Conditional Patterns
```python
# From cars.py
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Boolean operations from conditional_test.py
age = 22
print(age == 22)        # True
print(age != 22)        # False
print(age >= 21)        # True
```

**Learning Concepts**: if/elif/else, boolean operators, conditional expressions

---

## Chapter 6: Dictionaries
**Focus**: Key-value data structures and nested data

### Key Scripts
- `alien.py` - Basic dictionary operations
- `fav_languages.py` - Complex dictionary structures
- `many_users.py` - Lists of dictionaries
- `glossary.py` - Dictionary as reference tool

### Dictionary Patterns
```python
# From alien.py
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])     # Access value
alien_0['x_position'] = 0   # Add new key-value pair

# From fav_languages.py - nested structures
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
```

**Learning Concepts**: Dictionary methods, nested dictionaries, dictionary iteration

---

## Chapter 7: User Input and While Loops
**Focus**: Interactive programs and loop control

### Key Scripts
- `parrot.py` - Input validation loops
- `confirmed_users.py` - List processing with while loops
- `movie_tickets.py` - Age-based pricing
- `dream_vacation.py` - Survey collection

### Interactive Patterns
```python
# From parrot.py - input validation
message = input("Tell me something, and I will repeat it back to you: ")
while message != 'quit':
    print(message)
    message = input()

# From confirmed_users.py - list processing
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    confirmed_users.append(current_user)
```

**Learning Concepts**: input(), while loops, break/continue, user interaction

---

## Chapter 8: Functions
**Focus**: Code organization and reusability

### Key Modules and Functions

#### String Processing Functions
```python
# chapter_8/formatted_name.py
def get_formatted_value(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
```

#### Variable Arguments Functions
```python
# chapter_8/pizza.py
def make_pizza(*toppings):
    """Make a pizza with any number of toppings."""
    print("Making a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

def make_pizza2(size, *toppings):
    """Make a pizza with size and toppings."""
    print(f"Making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
```

#### Profile Building Functions
```python
# chapter_8/user_profile.py
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
```

### Function Categories
- **String Formatters**: `get_formatted_value()`, `get_city_names()`
- **User Interface**: `greet_users()`, `describe_city()`
- **Product Configurators**: `make_shirt()`, `make_pizza()`
- **Data Builders**: `build_profile()`, `make_album()`

**Learning Concepts**: Function definition, parameters, return values, *args, **kwargs

---

## Chapter 9: Classes
**Focus**: Object-oriented programming and inheritance

### Core Classes

#### `Car` Class Family
```python
# chapter_9/car.py - Base class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

# chapter_9/electric_car.py - Inheritance
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
```

#### `Restaurant` Class Family
```python
# chapter_9/restaurant.py - Base class
class Restaurant:
    def __init__(self, restaurant_name, cusinine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cusinine_type
        self.number_served = 0

# chapter_9/icecreamstand.py - Inheritance
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cusinine_type):
        super().__init__(restaurant_name, cusinine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']
```

#### `User` Class Family
```python
# chapter_9/user.py - Base class
class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

# chapter_9/admin.py - Inheritance with composition
class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()
```

### Utility Classes
- `Dog` - Basic class concepts
- `Die` - Random number generation
- `Battery` - Composition example

### Class Interaction Patterns
```python
# Inheritance chain
Car -> ElectricCar
Restaurant -> IceCreamStand
User -> Admin

# Composition pattern
ElectricCar contains Battery
Admin contains Privileges
```

**Learning Concepts**: Classes, inheritance, composition, method overriding

---

## Chapter 10: Files and Exceptions
**Focus**: File I/O, error handling, and data persistence

### File Processing Functions

#### Text File Operations
```python
# chapter_10/read_files.py
def read_files(filename):
    """Read and display file contents."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        print(contents)

# chapter_10/word_count.py
def count_word_1(filename):
    """Count words in a file, failing silently on errors."""
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
```

#### JSON Data Persistence
```python
# chapter_10/remember_me.py
def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username
```

### Error Handling Patterns
```python
# Basic pattern
try:
    risky_operation()
except SpecificError:
    handle_error()
else:
    success_code()

# File handling pattern
try:
    with open(filename) as file:
        data = file.read()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
```

**Learning Concepts**: File I/O, exception handling, JSON operations, context managers

---

## Chapter 11: Testing Your Code
**Focus**: Unit testing and test-driven development

### Testing Framework Components

#### Test Classes
```python
# chapter_11/test_name_function.py
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
```

#### Testing Classes with setUp
```python
# chapter_11/test_survey.py
class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""
    
    def setUp(self):
        """Create a survey and a set of responses for use in all test methods."""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
```

### Testable Components
- `name_function.py` + `test_name_function.py`
- `city_function.py` + `test_cities.py`
- `employee.py` + `test_employee.py`
- `survey.py` + `test_survey.py`

**Learning Concepts**: unittest framework, test methods, setUp, assertions

---

## Cross-Module Interactions

### Common Integration Patterns

#### File Processing + Error Handling
```python
from chapter_10.word_count import count_word_1
from chapter_10.read_files import read_files

# Process multiple files safely
files = ["chapter_10/alice.txt", "chapter_10/programming.txt"]
for filename in files:
    count_word_1(filename)  # Handles errors internally
```

#### Class Inheritance + Testing
```python
from chapter_9.car import Car
from chapter_9.electric_car import ElectricCar
import unittest

class TestCars(unittest.TestCase):
    def test_car_creation(self):
        car = Car("honda", "civic", 2020)
        self.assertEqual(car.get_decriptive_name(), "2020 Honda Civic")
    
    def test_electric_car_inheritance(self):
        tesla = ElectricCar("tesla", "model 3", 2023)
        self.assertIsInstance(tesla, Car)  # Inheritance test
```

#### Function + Class Integration
```python
from chapter_8.user_profile import build_profile
from chapter_9.user import User

# Build profile data, then create User object
profile_data = build_profile("john", "doe", age=30, city="seattle")
user = User(profile_data['first_name'], 
           profile_data['last_name'],
           profile_data['age'],
           profile_data['city'])
```

### Data Flow Patterns

#### Input -> Processing -> Output
```python
# Chapter 7: Get user input
# Chapter 8: Process with functions  
# Chapter 10: Save to file
# Chapter 11: Test the pipeline

def survey_pipeline():
    # Input (Chapter 7 patterns)
    responses = collect_user_responses()
    
    # Processing (Chapter 8 patterns)
    processed_data = process_responses(responses)
    
    # Storage (Chapter 10 patterns)
    save_to_json(processed_data, 'survey_results.json')
    
    # Testing (Chapter 11 patterns)
    # Unit tests verify each step
```

## Module Dependencies

### Import Relationships
```
chapter_9/electric_car.py imports chapter_9/car.py
chapter_11/test_*.py imports corresponding modules
chapter_10 modules use json (standard library)
chapter_11 modules use unittest (standard library)
```

### No External Dependencies
All modules use only Python standard library:
- `json` for data persistence
- `unittest` for testing
- `random` for dice/lottery functions
- Built-in functions and methods

## Best Practices by Module

### Chapter 8 (Functions)
- Use descriptive function names
- Include docstrings
- Handle edge cases with default parameters
- Use *args and **kwargs appropriately

### Chapter 9 (Classes)
- Initialize all attributes in `__init__`
- Use inheritance for "is-a" relationships
- Use composition for "has-a" relationships
- Override methods when necessary

### Chapter 10 (Files)
- Always use context managers (`with` statements)
- Handle specific exceptions
- Use appropriate file encodings
- Implement graceful error handling

### Chapter 11 (Testing)
- Test both success and failure cases
- Use setUp for test initialization
- Write descriptive test names
- Test edge cases and boundary conditions

This module reference provides a comprehensive view of how all components work together in the Python Crash Course repository.