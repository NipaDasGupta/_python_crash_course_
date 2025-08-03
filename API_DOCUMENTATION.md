# Python Crash Course - Comprehensive API Documentation

## Table of Contents

1. [Overview](#overview)
2. [Functions API](#functions-api)
3. [Classes API](#classes-api)
4. [File Operations](#file-operations)
5. [Testing Utilities](#testing-utilities)
6. [Usage Examples](#usage-examples)
7. [Best Practices](#best-practices)

## Overview

This repository contains educational Python scripts organized by chapters, covering fundamental to advanced Python concepts. All public APIs are designed for learning purposes and demonstrate best practices in Python programming.

### Repository Structure
```
├── chapter_1/          # Basic Python syntax
├── chapter_2/          # Variables and simple data types
├── chapter_3/          # Lists
├── chapter_4/          # Working with lists
├── chapter_5/          # If statements
├── chapter_6/          # Dictionaries
├── chapter_7/          # User input and while loops
├── chapter_8/          # Functions
├── chapter_9/          # Classes
├── chapter_10/         # Files and exceptions
└── chapter_11/         # Testing your code
```

## Functions API

### Chapter 8: Functions

#### String Formatting Functions

##### `get_formatted_name(first, last, middle="")`
**Location**: `chapter_11/name_function.py`

Generates a neatly formatted full name from individual name components.

**Parameters:**
- `first` (str): First name
- `last` (str): Last name  
- `middle` (str, optional): Middle name. Defaults to empty string.

**Returns:**
- `str`: Properly capitalized full name

**Example:**
```python
from chapter_11.name_function import get_formatted_name

# Basic usage
name = get_formatted_name("john", "doe")
print(name)  # Output: "John Doe"

# With middle name
name = get_formatted_name("john", "doe", "smith")
print(name)  # Output: "John Smith Doe"
```

##### `get_formatted_string(city, country, population=None)`
**Location**: `chapter_11/city_function.py`

Formats city and country information with optional population data.

**Parameters:**
- `city` (str): City name
- `country` (str): Country name
- `population` (int, optional): Population count

**Returns:**
- `str`: Formatted city-country string

**Example:**
```python
from chapter_11.city_function import get_formatted_string

# Without population
location = get_formatted_string("paris", "france")
print(location)  # Output: "Paris, France"

# With population
location = get_formatted_string("paris", "france", 2161000)
print(location)  # Output: "Paris, France - Population: 2161000"
```

#### User Interface Functions

##### `greet_users(names)`
**Location**: `chapter_8/greet_users.py`

Greets multiple users by name.

**Parameters:**
- `names` (list): List of user names

**Example:**
```python
from chapter_8.greet_users import greet_users

users = ["alice", "bob", "charlie"]
greet_users(users)
# Output:
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!
```

##### `describe_city(city, country='iceland')`
**Location**: `chapter_8/cities.py`

Describes a city and its country with a default country option.

**Parameters:**
- `city` (str): City name
- `country` (str, optional): Country name. Defaults to 'iceland'.

**Example:**
```python
from chapter_8.cities import describe_city

describe_city("reykjavik")  # Uses default country
describe_city("paris", "france")  # Custom country
```

#### Product Configuration Functions

##### `make_shirt(size='large', text_of_a_message="I love Python")`
**Location**: `chapter_8/t-shirt.py`

Creates a custom t-shirt configuration.

**Parameters:**
- `size` (str, optional): Shirt size. Defaults to 'large'.
- `text_of_a_message` (str, optional): Message text. Defaults to "I love Python".

**Example:**
```python
from chapter_8.t_shirt import make_shirt

# Default shirt
make_shirt()

# Custom size and message
make_shirt("medium", "Python Developer")

# Using keyword arguments
make_shirt(text_of_a_message="Code is Poetry", size="small")
```

##### `make_pizza(*toppings)` and variations
**Location**: `chapter_8/pizza.py`

Creates pizza orders with variable toppings.

**Parameters:**
- `*toppings`: Variable number of topping strings

**Example:**
```python
from chapter_8.pizza import make_pizza, make_pizza2

# Basic pizza
make_pizza("pepperoni", "mushrooms")

# Pizza with size specification
make_pizza2("large", "pepperoni", "extra cheese", "olives")
```

#### Data Processing Functions

##### `build_profile(first, last, **user_info)`
**Location**: `chapter_8/user_profile.py`

Builds a user profile dictionary with flexible additional information.

**Parameters:**
- `first` (str): First name
- `last` (str): Last name
- `**user_info`: Arbitrary keyword arguments for additional profile data

**Returns:**
- `dict`: User profile dictionary

**Example:**
```python
from chapter_8.user_profile import build_profile

profile = build_profile("john", "doe", 
                       age=30, 
                       city="new york", 
                       occupation="developer")
print(profile)
# Output: {'first_name': 'john', 'last_name': 'doe', 'age': 30, 'city': 'new york', 'occupation': 'developer'}
```

##### `make_album(artist_name, album_title, number_of_songs=None)`
**Location**: `chapter_8/city_names.py`

Creates an album information dictionary.

**Parameters:**
- `artist_name` (str): Artist name
- `album_title` (str): Album title
- `number_of_songs` (int, optional): Number of songs in album

**Returns:**
- `dict`: Album information dictionary

**Example:**
```python
from chapter_8.city_names import make_album

# Album without song count
album = make_album("the beatles", "abbey road")

# Album with song count
album = make_album("pink floyd", "dark side of the moon", 10)
```

### Chapter 10: File Operations

##### `read_files(filename)`
**Location**: `chapter_10/read_files.py`

Safely reads and displays file contents.

**Parameters:**
- `filename` (str): Path to file to read

**Example:**
```python
from chapter_10.read_files import read_files

read_files("chapter_10/alice.txt")
```

##### `count_word_1(filename)`
**Location**: `chapter_10/word_count.py`

Counts words in a file with silent error handling.

**Parameters:**
- `filename` (str): Path to file to analyze

**Example:**
```python
from chapter_10.word_count import count_word_1

count_word_1("chapter_10/alice.txt")
# Output: "The file chapter_10/alice.txt has about 29594 words."
```

##### `count_line(filename)`
**Location**: `chapter_10/count_lines.py`

Counts lines in a text file.

**Parameters:**
- `filename` (str): Path to file to count

**Example:**
```python
from chapter_10.count_lines import count_line

count_line("chapter_10/programming.txt")
```

### Chapter 10: Data Persistence

##### `get_stored_username()`, `get_new_username()`, `greet_user()`
**Location**: `chapter_10/remember_me.py`

User session management functions using JSON storage.

**Functions:**
- `get_stored_username()`: Retrieves stored username from JSON file
- `get_new_username()`: Prompts for and stores new username
- `greet_user()`: Main function that greets user with stored or new username

**Example:**
```python
from chapter_10.remember_me import greet_user

greet_user()  # Handles entire user greeting workflow
```

##### `get_stored_number()`, `get_new_number()`, `tell_favorite_number()`
**Location**: `chapter_10/favorite_number.py`

Favorite number management with JSON persistence.

**Example:**
```python
from chapter_10.favorite_number import tell_favorite_number

tell_favorite_number()  # Complete favorite number workflow
```

### Chapter 9: Lottery System

##### `pull_in(generate_ticket)`, `read_ticket(wining_ticket)`, `check_ticket(generated_ticket, wining_ticket)`, `win_lottery()`
**Location**: `chapter_9/lottery.py`

Complete lottery ticket system with generation and checking functionality.

**Example:**
```python
from chapter_9.lottery import win_lottery

win_lottery()  # Runs complete lottery simulation
```

## Classes API

### Chapter 9: Object-Oriented Programming

#### Core Classes

##### `Car`
**Location**: `chapter_9/car.py`

A comprehensive car representation with odometer functionality.

**Attributes:**
- `make` (str): Car manufacturer
- `model` (str): Car model
- `year` (int): Manufacturing year
- `odometer_reading` (int): Current mileage (default: 0)

**Methods:**

###### `__init__(self, make, model, year)`
Initialize a new car instance.

###### `get_decriptive_name(self)`
Returns formatted descriptive name.

**Returns:** `str` - Formatted car description

###### `read_odometer(self)`
Prints current odometer reading.

###### `update_odometer(self, mileage)`
Updates odometer reading with validation.

**Parameters:**
- `mileage` (int): New mileage value

###### `increment_odometer(self, miles)`
Adds miles to current odometer reading.

**Parameters:**
- `miles` (int): Miles to add

**Example:**
```python
from chapter_9.car import Car

# Create a car
my_car = Car("tesla", "model 3", 2023)

# Use car methods
print(my_car.get_decriptive_name())  # "2023 Tesla Model 3"
my_car.read_odometer()  # "This car has 0 miles on it."

# Update mileage
my_car.update_odometer(1500)
my_car.increment_odometer(100)
my_car.read_odometer()  # "This car has 1600 miles on it."
```

##### `Restaurant`
**Location**: `chapter_9/restaurant.py`

Restaurant management system with customer tracking.

**Attributes:**
- `restaurant_name` (str): Restaurant name
- `cuisine_type` (str): Type of cuisine served
- `number_served` (int): Customers served (default: 0)

**Methods:**

###### `__init__(self, restaurant_name, cusinine_type)`
Initialize restaurant instance.

###### `describe_restaurant(self)`
Prints restaurant information.

###### `open_restaurant(self)`
Displays restaurant open status.

###### `read_number_served(self)`
Prints number of customers served.

###### `set_number_served(self, customers_served)`
Sets customer count with validation.

###### `increment_number_served(self, served)`
Adds to customer count.

**Example:**
```python
from chapter_9.restaurant import Restaurant

# Create restaurant
my_restaurant = Restaurant("mario's", "italian")

# Use restaurant methods
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

# Track customers
my_restaurant.set_number_served(100)
my_restaurant.increment_number_served(25)
my_restaurant.read_number_served()  # "The restaurant has served 125 customers."
```

##### `User`
**Location**: `chapter_9/user.py`

User account management with login tracking.

**Attributes:**
- `first_name` (str): User's first name
- `last_name` (str): User's last name
- `age` (int): User's age
- `location` (str): User's location
- `login_attempts` (int): Login attempt counter (default: 0)

**Methods:**

###### `__init__(self, first_name, last_name, age, location)`
Initialize user instance.

###### `describe_user(self)`
Prints user information summary.

###### `greet_user(self)`
Prints personalized greeting.

###### `increment_login_attempts(self)`
Increments login attempt counter.

###### `reset_login_attempts(self)`
Resets login attempts to zero.

**Example:**
```python
from chapter_9.user import User

# Create user
user = User("alice", "johnson", 28, "seattle")

# Use user methods
user.describe_user()
user.greet_user()

# Track login attempts
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")  # 2
user.reset_login_attempts()
print(f"Login attempts: {user.login_attempts}")  # 0
```

#### Inheritance Examples

##### `ElectricCar(Car)`
**Location**: `chapter_9/electric_car.py`

Electric vehicle class inheriting from Car with battery management.

**Additional Attributes:**
- `battery` (Battery): Battery instance for power management

**Methods:**

###### `__init__(self, make, model, year)`
Initialize electric car with battery.

###### `fill_gas_tank(self)`
Override method - electric cars don't use gas.

**Example:**
```python
from chapter_9.electric_car import ElectricCar

# Create electric car
my_tesla = ElectricCar("tesla", "model s", 2023)

# Use inherited methods
print(my_tesla.get_decriptive_name())

# Use electric-specific methods
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.fill_gas_tank()  # "This car does not need a gas tank!"
```

##### `Battery`
**Location**: `chapter_9/electric_car.py`

Battery management for electric vehicles.

**Attributes:**
- `battery_size` (int): Battery capacity in kWh (default: 75)

**Methods:**

###### `__init__(self, battery_size=75)`
Initialize battery with size.

###### `describe_battery(self)`
Prints battery specifications.

###### `get_range(self)`
Calculates and displays driving range.

###### `upgrade_battery(self)`
Upgrades battery to 100 kWh.

##### `IceCreamStand(Restaurant)`
**Location**: `chapter_9/icecreamstand.py`

Ice cream shop inheriting from Restaurant.

**Additional Attributes:**
- `flavors` (list): Available ice cream flavors

**Methods:**

###### `__init__(self, restaurant_name, cusinine_type)`
Initialize ice cream stand.

###### `show_flavors(self)`
Display available flavors.

**Example:**
```python
from chapter_9.icecreamstand import IceCreamStand

# Create ice cream stand
ice_cream_shop = IceCreamStand("sweet treats", "dessert")

# Use inherited methods
ice_cream_shop.describe_restaurant()

# Use ice cream specific methods
ice_cream_shop.show_flavors()
```

##### `Admin(User)`
**Location**: `chapter_9/admin.py`

Administrative user with privileges management.

**Additional Attributes:**
- `privileges` (Privileges): Privileges management instance

**Example:**
```python
from chapter_9.admin import Admin

# Create admin user
admin = Admin("john", "admin", 35, "headquarters")

# Use inherited methods
admin.describe_user()

# Use admin-specific methods
admin.privileges.show_privileges()
```

##### `Privileges`
**Location**: `chapter_9/admin.py`

Privileges management for admin users.

**Attributes:**
- `privileges` (list): List of admin privileges

**Methods:**

###### `show_privileges(self)`
Display admin privileges.

#### Utility Classes

##### `Dog`
**Location**: `chapter_9/dog.py`

Simple dog representation for basic OOP concepts.

**Attributes:**
- `name` (str): Dog's name
- `age` (int): Dog's age

**Methods:**

###### `__init__(self, name, age)`
Initialize dog instance.

###### `sit(self)`
Make dog sit.

###### `roll_over(self)`
Make dog roll over.

**Example:**
```python
from chapter_9.dog import Dog

# Create dog
my_dog = Dog("buddy", 3)

# Use dog methods
my_dog.sit()        # "Buddy is now sitting."
my_dog.roll_over()  # "Buddy rolled over!"
```

##### `Die`
**Location**: `chapter_9/dice.py`

Configurable dice for games and simulations.

**Attributes:**
- `sides` (int): Number of sides (default: 6)

**Methods:**

###### `__init__(self, sides=6)`
Initialize die with specified sides.

###### `roll_die(self)`
Roll the die and return result.

**Returns:** `int` - Random number between 1 and sides

**Example:**
```python
from chapter_9.dice import Die

# Create different dice
d6 = Die()          # 6-sided die
d10 = Die(10)       # 10-sided die
d20 = Die(20)       # 20-sided die

# Roll dice
print(f"D6 roll: {d6.roll_die()}")
print(f"D10 roll: {d10.roll_die()}")
print(f"D20 roll: {d20.roll_die()}")
```

## File Operations

### Text File Processing

The repository includes several utilities for file operations:

#### Reading Files
```python
# Safe file reading with error handling
from chapter_10.file_reader import read_file

try:
    content = read_file("data.txt")
    print(content)
except FileNotFoundError:
    print("File not found")
```

#### Writing Files
```python
# Writing to files
filename = "output.txt"
with open(filename, 'w') as file:
    file.write("Hello, World!")
```

#### JSON Operations
```python
import json

# Save data to JSON
data = {"name": "Alice", "age": 30}
with open("user_data.json", 'w') as file:
    json.dump(data, file)

# Load data from JSON
with open("user_data.json", 'r') as file:
    loaded_data = json.load(file)
```

## Testing Utilities

### Chapter 11: Unit Testing

#### Test Classes

##### `NamesTestCase(unittest.TestCase)`
**Location**: `chapter_11/test_name_function.py`

Tests for name formatting functions.

**Test Methods:**
- `test_first_last_name()`: Tests basic name formatting
- `test_first_last_middle_name()`: Tests name formatting with middle name

##### `CityTestCase(unittest.TestCase)`
**Location**: `chapter_11/test_cities.py`

Tests for city formatting functions.

##### `TestEmployee(unittest.TestCase)`
**Location**: `chapter_11/test_employee.py`

Tests for employee management functionality.

##### `TestAnonymousSurvey(unittest.TestCase)`
**Location**: `chapter_11/test_survey.py`

Tests for survey functionality with setup methods.

**Test Methods:**
- `setUp()`: Initialize test survey
- `test_store_single_response()`: Test single response storage
- `test_store_three_responses()`: Test multiple response storage

#### Survey System

##### `AnonymousSurvey`
**Location**: `chapter_11/survey.py`

Anonymous survey collection system.

**Attributes:**
- `question` (str): Survey question
- `responses` (list): Collected responses

**Methods:**

###### `__init__(self, question)`
Initialize survey with question.

###### `show_question(self)`
Display survey question.

###### `store_response(self, new_response)`
Store a survey response.

###### `show_results(self)`
Display all collected responses.

**Example:**
```python
from chapter_11.survey import AnonymousSurvey

# Create survey
survey = AnonymousSurvey("What's your favorite programming language?")

# Collect responses
survey.show_question()
survey.store_response("Python")
survey.store_response("JavaScript")
survey.store_response("Go")

# Show results
survey.show_results()
```

##### `Employee`
**Location**: `chapter_11/employee.py`

Employee management with salary operations.

**Attributes:**
- `first_name` (str): Employee first name
- `last_name` (str): Employee last name
- `annual_salary` (int): Annual salary

**Methods:**

###### `__init__(self, first_name, last_name, annual_salary)`
Initialize employee.

###### `give_raise(self, amount=5000)`
Give salary raise with default amount.

**Example:**
```python
from chapter_11.employee import Employee

# Create employee
emp = Employee("john", "doe", 50000)

# Give raise
emp.give_raise()  # Default $5000 raise
print(emp.annual_salary)  # 55000

# Custom raise amount
emp.give_raise(10000)
print(emp.annual_salary)  # 65000
```

## Usage Examples

### Complete Workflow Examples

#### 1. Car Management System
```python
from chapter_9.car import Car
from chapter_9.electric_car import ElectricCar

# Create regular car
my_car = Car("honda", "civic", 2022)
print(my_car.get_decriptive_name())
my_car.update_odometer(15000)
my_car.increment_odometer(500)
my_car.read_odometer()

# Create electric car
my_electric = ElectricCar("tesla", "model 3", 2023)
print(my_electric.get_decriptive_name())
my_electric.battery.describe_battery()
my_electric.battery.get_range()
my_electric.battery.upgrade_battery()
my_electric.battery.get_range()
```

#### 2. Restaurant Management
```python
from chapter_9.restaurant import Restaurant
from chapter_9.icecreamstand import IceCreamStand

# Regular restaurant
restaurant = Restaurant("luigi's", "italian")
restaurant.describe_restaurant()
restaurant.set_number_served(150)
restaurant.increment_number_served(25)
restaurant.read_number_served()

# Ice cream stand
ice_cream = IceCreamStand("cool treats", "dessert")
ice_cream.describe_restaurant()
ice_cream.show_flavors()
```

#### 3. User Management with Admin
```python
from chapter_9.user import User
from chapter_9.admin import Admin

# Regular user
user = User("alice", "smith", 25, "portland")
user.describe_user()
user.increment_login_attempts()

# Admin user
admin = Admin("bob", "jones", 40, "seattle")
admin.describe_user()
admin.privileges.show_privileges()
```

#### 4. File Processing Workflow
```python
from chapter_10.word_count import count_word_1
from chapter_10.read_files import read_files

# Process multiple files
files = [
    "chapter_10/alice.txt",
    "chapter_10/little_women.txt",
    "chapter_10/moby_dick.txt"
]

for filename in files:
    print(f"\nProcessing {filename}:")
    count_word_1(filename)
```

#### 5. Survey Data Collection
```python
from chapter_11.survey import AnonymousSurvey

# Create and run survey
language_survey = AnonymousSurvey("What's your favorite programming language?")

# Simulate responses
responses = ["Python", "JavaScript", "Java", "C++", "Go"]
for response in responses:
    language_survey.store_response(response)

# Display results
language_survey.show_question()
language_survey.show_results()
```

#### 6. Testing Workflow
```python
import unittest
from chapter_11.test_name_function import NamesTestCase
from chapter_11.test_survey import TestAnonymousSurvey

# Run specific test
if __name__ == '__main__':
    # Run all tests
    unittest.main()
    
    # Or run specific test class
    suite = unittest.TestLoader().loadTestsFromTestCase(NamesTestCase)
    unittest.TextTestRunner().run(suite)
```

## Best Practices

### 1. Function Design
- Use descriptive function names
- Include docstrings for all functions
- Provide default parameter values where appropriate
- Handle edge cases gracefully

### 2. Class Design
- Use clear class and method names
- Initialize all attributes in `__init__`
- Provide meaningful string representations
- Use inheritance appropriately

### 3. Error Handling
- Use try-except blocks for file operations
- Provide meaningful error messages
- Fail gracefully when possible
- Log errors appropriately

### 4. Testing
- Write tests for all public methods
- Use setUp methods for test initialization
- Test both success and failure cases
- Use descriptive test method names

### 5. Documentation
- Include module-level docstrings
- Document all parameters and return values
- Provide usage examples
- Keep documentation up to date

## Installation and Setup

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses only standard library)

### Running the Code
```bash
# Clone the repository
git clone <repository-url>
cd python-crash-course

# Run individual scripts
python chapter_9/car.py
python chapter_11/test_name_function.py

# Run tests
python -m unittest chapter_11.test_name_function
python -m unittest discover chapter_11
```

### Project Structure
```
python-crash-course/
├── chapter_1/           # Basic Python concepts
├── chapter_2/           # Variables and data types
├── chapter_3/           # Lists
├── chapter_4/           # Working with lists
├── chapter_5/           # Conditional statements
├── chapter_6/           # Dictionaries
├── chapter_7/           # User input and loops
├── chapter_8/           # Functions
├── chapter_9/           # Classes and OOP
├── chapter_10/          # Files and exceptions
├── chapter_11/          # Testing
└── README.md
```

This documentation covers all public APIs, functions, and classes in the Python Crash Course repository. Each component includes detailed parameter descriptions, return values, and practical usage examples to help developers understand and effectively use the codebase.