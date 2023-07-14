# Learning Python
This repository is a collection of scripts used to try features and experiment with Python. It is great for people who are just starting out and want to learn the syntax, and for people who might have used Python before, but that want to expand their knowledge and see what else Python is capable of.

## Language Details
A variable is created when you assign it a value. Variables never need to be declared ahead of time.

Calling a class like a function generates instances of the new type, and the class's methods automatically receive the instance being processed by a given method call (in the `self` argument).

You can access the attributes and methods of a class by using `self`. If you don't use `self` for variables, they will be class variables and will be shared by _all_ instances of the class.

```python
class Dog:
    tricks = []             # Class variable shared by all instances.

    def __init__(self, name):
        self.name = name    # Instance variable unique to each instance.
```

```python
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # Creates a new empty list for each dog.

    def add_trick(self, trick):
        self.tricks.append(trick)
```

## Hierarchy
- Programs are composed of modules.
- Modules contain statements.
- Statements contain expressions.
- Expressions create and process objects.

## Built-in Types
### Lists
Lists are positionally ordered collections of arbitrarily typed object, and they have no fixed size. They provide a very flexible tool for representing arbitrary collections - employees in a company, emails in your inbox, etc.

### Dictionaries
Dictionaries are also known as mappings. A mapping is a collection of objects that stores objects by key instead of by relative position. Mappings map keys to associated values.

### Tuples
Tuples are sequences that cannot be changed. They are used to represent a fixed collection of items (like a specific calendar date).

## Naming Convention
### Modules
Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability.

`file.py`

### Classes
Class names should normally use the CapWords convention. The naming convention for functions may be used instead in cases where the interface is documented and used primarily as a callable.

`class MyClass`

### Exceptions
Since exceptions should be classes, the class naming convention applies here. Use the suffix "Error" on the name if the exception actually is an error.

`CustomError`

### Functions and Variables
Function names should be lowercase, with words separated by underscores as necessary to improve readability.

`def my_function()`

Variable names follow the same convention as function names.

`my_variable`

### Methods
Use the function naming convention: lowercase with words separated by underscores as necessary to improve readability.

`def my_method()`

### Constants
Constants are usually defined on a module level and written in all capital letters with underscores separating words.

`MY_CONSTANT`

## Debugging
You can use `py -i file_name.py` from the terminal/command line to run the program in interactive mode. This command will run the program and once it exits, it will allow you to interact with the program (like assign variables, print statements, etc) regardless of whether or not it ran successfully.