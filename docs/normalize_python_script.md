# Normalize python code
When you publish a python code, you should normalize your code, so everyone can read it and understand it easily.
In this doc, we will learn:
- how the python code naming convention works
- how to use tools such as `black`, "pylint" to keep your code clean(code lint). 
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

## 3. Use Black for 