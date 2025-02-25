# Normalize python code
When you publish a python code, you should normalize your code, so everyone can read it and understand it easily.
In this doc, we will learn:
- how the python code naming convention works
- how to use tools such as `black` to do code lint
- how to use tools such as `isort` to clean imports
- how to document the code
- how to use `type hint` and use tool such as `` to do static check
- 

## 1. Naming convention

The python naming convention is defined in **PEP08**. For more details, you should visit the official page of PEP.

### 1.1 Package

A **package name** should always be in `lowercase letters`, and separate words with `underscores` only if necessary.

```text
my_package   # Good ✅
mypackage    # Good (preferred if short) ✅
MyPackage    # Bad (avoid CamelCase for packages) ❌ 
myPackage    # Bad (mixed case is not recommended) ❌ 
```

### 1.2 Module

A **module name** should always be in `lowercase letters`, and separate words with `underscores` only if it improves readability.

```text
my_module.py   # Good ✅
mymodule.py    # Good (preferred if short) ✅
MyModule.py    # Bad (avoid CamelCase for packages) ❌ 
myModule.py    # Bad (mixed case is not recommended) ❌ 
my-module.py   # Not allowed (hyphens are not allowed) ❌❌
```

### 1.3 Class

A class name should be in CamelCase (PascalCase).

```text
class MyClass:   # Good ✅
    pass

class my_class:  # Bad (use CamelCase) ❌ 
    pass

class my_class:   # Bad (not readable) ❌ 
    pass
```

### 1.4 Function/Method

A **function/method** name should use the `snake_case (lowercase with underscores)`.

```text
def my_function():  # Good ✅
    pass

def MyFunction():   # Bad (looks like a class) ❌ 
    pass

def myFunction():   # Bad (mixed case is not recommended) ❌ 
    pass
```

### 1.5 Variable

Use `snake_case` for variable names.

```text
my_variable = 38   # Good ✅
MyVariable = 38    # Bad (avoid CamelCase for variables) ❌ 
myVariable = 38    # Bad (mixed case is not recommended) ❌ 
```

### 1.6 Constant

```text
MY_CONSTANT = 38  # Good ✅
pi = 3.14        # Bad (constants should be in ALL_CAPS) ❌ 
```

### 1.7 Custom exception 

The custom exception name should be in `CamelCase` and end with `Error`.

```text
class DataProcessingError(Exception):  # Good ✅
    pass

class Data_Error(Exception):  # Bad (no underscores in class names) ❌ 
    pass
```

## 2. Private and Protected Members of Python class 

In a python class, you can define:
- `private` attributes/methods with a single underscore _ .
- `strong private` attributes/methods with a double underscore __ (name mangling) .

```python
class MyClass:
    def __init__(self):
        self.public_var = 42         # Public attribute
        self._protected_var = 99      # Protected attribute (convention)
        self.__private_var = 100      # Private attribute (name mangling)

    def _helper_method(self):         # Protected method
        pass

    def __internal_method(self):      # Private method
        pass

```

> Another class can still access the protected attribute of a class, it's only a naming convention that tells other users
> you should not use it.
> 
> 

## 3. Dunder (Double Underscore) Methods in Python class

`Dunder methods (short for double underscore methods, also known as magic methods)` are special methods in Python 
that begin and end with double underscores (__method__). These methods allow objects to interact with 
built-in Python functions and operators.

| Category               | 	Common Dunder Methods                                                 |
|------------------------|------------------------------------------------------------------------|
| Object Construction	   | __new__, __init__, __del__                                             |
| String Representation	 | __str__, __repr__                                                      |
| Arithmetic Operators   | 	__add__, __sub__, __mul__, __truediv__, __mod__                       |
| Comparison Operators   | 	__eq__, __ne__, __lt__, __le__, __gt__, __ge__                        |
| Container Methods	     | __len__, __getitem__, __setitem__, __delitem__, __iter__, __contains__ |
| Attribute Management	  | __getattr__, __setattr__, __delattr__, __dir__                         |

### 3.1 Object Construction & Initialization

These methods are used to define how objects are created and initialized.

| Method	              | Description                                             |
|----------------------|---------------------------------------------------------|
| __new__(cls, ...)	   | Creates a new instance of a class. Rarely overridden.   |
| __init__(self, ...)	 | Initializes an instance (like a constructor).           |
| __del__(self)	       | Called when an object is deleted (not always reliable). |

```python
class Car:
    def __init__(self, make, model):
        """Constructor: Initializes the car object"""
        self.make = make
        self.model = model

    def __del__(self):
        """Destructor: Called when object is deleted"""
        print(f"{self.make} {self.model} is being deleted!")

# Create an object
car = Car("Toyota", "Corolla")
del car  # Calls __del__()

```

### 3.2 String Representation

These methods define how an object is represented as a string.

| Method	         | Description                                                                     |
|-----------------|---------------------------------------------------------------------------------|
| __str__(self)	  | Returns a user-friendly string representation of an object (used with print()). |
| __repr__(self)	 | Returns an unambiguous representation (used in debugging).                      |

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"{self.make} {self.model}"

    def __repr__(self):
        return f"Car(make={self.make}, model={self.model})"

car = Car("Honda", "Civic")
print(str(car))   # Calls __str__ → "Honda Civic"
print(repr(car))  # Calls __repr__ → "Car(make=Honda, model=Civic)"

```

### 3.3 Arithmetic Operators Overloading

These methods allow objects to use arithmetic operators like `+, -, *, etc`.

| Method	                   | Description                    |
|---------------------------|--------------------------------|
| __add__(self, other)      | 	Implements + (e.g., a + b).   |
| __sub__(self, other)      | 	Implements - (e.g., a - b).   |
| __mul__(self, other)      | 	Implements * (e.g., a * b).   |
| __truediv__(self, other)  | 	Implements / (e.g., a / b).   |
| __floordiv__(self, other) | 	Implements // (e.g., a // b). |
| __mod__(self, other)	     | Implements % (e.g., a % b).    |
| __pow__(self, other)	     | Implements ** (e.g., a ** b).  |

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2  # Calls __add__()
print(v3)  # Output: Vector(6, 8)

```

### 3.4 Comparison Operators Overloading

These methods define how objects behave with comparison operators.

Method	Description
__eq__(self, other)	Implements == (equal to).
__ne__(self, other)	Implements != (not equal to).
__lt__(self, other)	Implements < (less than).
__le__(self, other)	Implements <= (less than or equal to).
__gt__(self, other)	Implements > (greater than).
__ge__(self, other)	Implements >= (greater than or equal to).