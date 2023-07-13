# Learning Python
This repository is a collection of scripts used to try features and experiment with Python. It is great for people who are just starting out and want to learn the syntax, and for people who might have used Python before, but that want to expand their knowledge and see what else Python is capable of.

## Language Details
A variable is created when you assign it a value. Variables never need to be declared ahead of time.

## Hierarchy
- Programs are composed of modules.
- Modules contain statements.
- Statements contain expressions.
- Expressions create and process objects.

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