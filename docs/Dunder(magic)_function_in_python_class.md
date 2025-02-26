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

| Method	             | Description                                |
|---------------------|--------------------------------------------|
| __eq__(self, other) | 	Implements == (equal to).                 |
| __ne__(self, other) | Implements != (not equal to).              |
| __lt__(self, other) | 	Implements < (less than).                 |
| __le__(self, other) | 	Implements <= (less than or equal to).    |
| __gt__(self, other) | 	Implements > (greater than).              |
| __ge__(self, other) | 	Implements >= (greater than or equal to). |

```python
class Box:
    def __init__(self, volume):
        self.volume = volume

    def __lt__(self, other):
        return self.volume < other.volume

box1 = Box(10)
box2 = Box(20)
print(box1 < box2)  # Calls __lt__ → True

```

### 3.5 Container & Iterable Protocols

These methods allow objects to act like containers (lists, sets, etc.).

| Method	                        | Description                                |
|--------------------------------|--------------------------------------------|
| __len__(self)	                 | Returns length using len(obj).             |
| __getitem__(self, key)         | 	Implements obj[key].                      |
| __setitem__(self, key, value)	 | Implements obj[key] = value.               |
| __delitem__(self, key)	        | Implements del obj[key].                   |
| __iter__(self)	                | Returns an iterator for looping.           |
| __contains__(self, item)	      | Implements in keyword (e.g., item in obj). |


```python
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def __setitem__(self, key, value):
        self.items[key] = value

    def __getitem__(self, key):
        return self.items.get(key, "Item not found")

    def __len__(self):
        return len(self.items)

cart = ShoppingCart()
cart["Apple"] = 3  # Calls __setitem__
print(cart["Apple"])  # Calls __getitem__ → 3
print(len(cart))  # Calls __len__ → 1

```

### 3.6 Attribute Access & Management

These methods control how attributes are accessed, set, or deleted.

| Method	                         | Description                            |
|---------------------------------|----------------------------------------|
| __getattr__(self, name)	        | Called when an attribute is not found. |
| __setattr__(self, name, value)	 | Called when setting an attribute.      |
| __delattr__(self, name)	        | Called when deleting an attribute.     |
| __dir__(self)	                  | Returns a list of attributes.          |

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
        return f"'{attr}' attribute not found"

p = Person("Alice")
print(p.age)  # Calls __getattr__ → "'age' attribute not found"

```