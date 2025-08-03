# Welcome to Python Crash Course repository! 🎉

This repository contains chapter-wise coding scripts in python that will help you learn the basics and beyond of this powerful and versatile programming language. Whether you are a beginner or an experienced coder, you will find something useful and interesting in this repository. You will learn how to use python for data analysis, web development, game design, automation, and more. You will also learn how to write clean, efficient, and elegant code that follows the best practices and standards of python.

## 📚 Documentation

Comprehensive documentation is available for all public APIs, functions, and components:

- **[API Documentation](API_DOCUMENTATION.md)** - Complete reference for all functions, classes, and APIs with detailed examples
- **[Quick Start Guide](QUICK_START_GUIDE.md)** - Get started in 5 minutes with the most commonly used components
- **[Module Reference](MODULE_REFERENCE.md)** - Organized by chapter with interaction patterns and cross-module integration

## 🚀 Getting Started

### Quick Setup
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

### Essential Examples
```python
# Work with classes
from chapter_9.car import Car
car = Car("toyota", "camry", 2023)
print(car.get_decriptive_name())  # "2023 Toyota Camry"

# Format names
from chapter_11.name_function import get_formatted_name
name = get_formatted_name("john", "doe")
print(name)  # "John Doe"

# Process files safely
from chapter_10.word_count import count_word_1
count_word_1("chapter_10/alice.txt")
```

## 📖 Learning Path

To get started, simply clone or download this repository and open the scripts in your favorite code editor or IDE. You can also run them in your terminal or command prompt. Each script has comments and explanations that will guide you through the logic and syntax of python. You can modify them as you wish and experiment with different inputs and outputs.

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
├── chapter_9/          # Classes and OOP
├── chapter_10/         # Files and exceptions
└── chapter_11/         # Testing your code
```

### Key Components
- **Classes**: `Car`, `Restaurant`, `User`, `ElectricCar`, `AnonymousSurvey`
- **Functions**: Name formatting, file processing, user profiles, pizza orders
- **File Operations**: Safe reading, word counting, JSON persistence
- **Testing**: Unit tests with unittest framework

## 🔧 Prerequisites
- Python 3.6 or higher
- No external dependencies (uses only standard library)

I hope you enjoy this repository and find it helpful for your python journey. Happy coding! 😊
