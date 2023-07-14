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

The keyword `global` lets you change names that live outside of the current scope. It tells Python that a function plans to change one or more global names (names that live in the closing module's scope, aka namespace).

```python
X = 88          # Global X

def func():
    global X
    X = 99      # Variable outside def

func()
print(X)        # Prints 99
```

Even if a variable is not declared at the namespace level, it can be declared as a global variable inside a function with the keyword `global`. By default however, names assigned in functions are local variables.

```python
y, z = 1, 2         # Global variables in module

def all_global():
    global x        # Another global variable in module
    x = y + z
```

Factory functions (or closures), are used by programs that need to generate event handlers on the fly in response to conditions at runtime. For example, a GUI must define actions according to user inputs that cannot be anticipated when the GUI is built. In such cases, we need a function that creates and returns another function, with information that may vary per function made.

```python
def maker(N):
    def action(X):
        return X ** N       # The function 'action' retains N from enclosing scope
    return action

f = maker(2)                # Passes 2 to argument N
f(3)                        # Passes 3 to X. N remembers 2 so 3^2 = 9. Returns 9
f(4)                        # Returns 16 because 4^2 = 16
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

```python
file.py
```

### Classes
Class names should normally use the CapWords convention. The naming convention for functions may be used instead in cases where the interface is documented and used primarily as a callable.

```python
class MyClass
```

### Exceptions
Since exceptions should be classes, the class naming convention applies here. Use the suffix "Error" on the name if the exception actually is an error.

```python
CustomError
```

### Functions and Variables
Function names should be lowercase, with words separated by underscores as necessary to improve readability.

```python
def my_function()
```

Variable names follow the same convention as function names.

```python
my_variable
```

### Methods
Use the function naming convention: lowercase with words separated by underscores as necessary to improve readability.

```python
def my_method()
```

### Constants
Constants are usually defined on a module level and written in all capital letters with underscores separating words.

```python
MY_CONSTANT
```

## Debugging
You can use `py -i file_name.py` from the terminal/command line to run the program in interactive mode. This command will run the program and once it exits, it will allow you to interact with the program (like assign variables, print statements, etc) regardless of whether or not it ran successfully.