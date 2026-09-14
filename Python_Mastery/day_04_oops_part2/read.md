# Python OOP — Module 5

A mastery-first revision and practice module covering the Python OOP concepts studied in Day 4.

## Topics Covered

1. Classes and Objects
2. `__init__` and Instance Attributes
3. Instance Methods
4. Class Methods
5. Static Methods
6. Encapsulation
7. Abstraction
8. Inheritance
9. Polymorphism
10. Composition
11. Dunder Methods
    - `__str__`
    - `__repr__`
    - `__len__`
    - `__eq__`
    - `__iter__`
    - `__call__`
12. Properties
    - `@property`
    - Getters
    - Setters

> SOLID principles are intentionally excluded from this revision pack because they are the next section of Module 5 and have not yet been studied.

---

## 1. Classes and Objects

A class is a blueprint for creating objects.

```python
class Employee:
    pass

employee = Employee()
```

- `Employee` is the class.
- `employee` is an object/instance of `Employee`.

### Mental model

```text
Class
  ↓
Blueprint

Object
  ↓
Actual instance created from the blueprint
```

---

## 2. `__init__` and Instance Attributes

`__init__` initializes an object when it is created.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
```

```python
employee = Employee("Rahul", 50000)
```

`self.name` and `self.salary` are instance attributes.

Each object can have its own values.

---

## 3. Instance Methods

Instance methods operate on a particular object and receive `self`.

```python
class Employee:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name}"
```

```python
employee = Employee("Rahul")
print(employee.introduce())
```

Mental model:

```text
object.method()
      ↓
self = that object
```

---

## 4. Class Methods

A class method receives the class as `cls`.

Use `@classmethod`.

```python
class Employee:
    company = "ABC"

    @classmethod
    def change_company(cls, name):
        cls.company = name
```

```python
Employee.change_company("XYZ")
```

Typical uses:
- Operations involving class-level state.
- Alternative constructors/factory-style constructors.

Example:

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, data):
        name, salary = data.split(",")
        return cls(name, int(salary))
```

---

## 5. Static Methods

A static method does not automatically receive `self` or `cls`.

Use `@staticmethod`.

```python
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b
```

```python
print(Calculator.add(10, 20))
```

Use a static method when the operation logically belongs to the class but does not need instance or class state.

---

# Encapsulation

Encapsulation means keeping an object's internal state/implementation controlled behind a public interface.

Python commonly uses naming conventions:

```python
self._balance
```

A single underscore means:

> This attribute is intended for internal use.

It is **not** a strict access restriction.

This is valid Python:

```python
account._balance = 5000
```

The underscore communicates intent rather than enforcing privacy.

---

## Example: Bank Account

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def get_balance(self):
        return self._balance
```

The class controls how balance changes through its methods.

---

# Abstraction

Abstraction means exposing the required behavior while hiding implementation details.

Python can use the `abc` module.

```python
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

A subclass must provide the required behavior:

```python
class CreditCardPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using credit card")
```

The abstract method defines a contract:

```text
Payment
   ↓
must provide pay()
```

The parent class can define what capability is required without defining the exact implementation for every child.

---

# Inheritance

Inheritance represents an **IS-A** relationship.

```python
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Woof")
```

A `Dog` is an `Animal`.

```text
Animal
  ↑
 Dog
```

The child can reuse inherited behavior and add or override behavior.

---

# Polymorphism

Polymorphism means the same interface/operation can work with different object types.

Example:

```python
class Dog:
    def speak(self):
        print("Woof")


class Cat:
    def speak(self):
        print("Meow")


def make_speak(animal):
    animal.speak()
```

```python
make_speak(Dog())
make_speak(Cat())
```

The caller does not need to know the concrete type. It only relies on the `speak()` behavior.

Mental model:

```text
same operation
      ↓
different objects
      ↓
different behavior
```

---

# Composition

Composition represents a **HAS-A** relationship.

```python
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()
```

A car has an engine.

```text
Car
 |
 +-- Engine
```

Compare:

```text
Dog IS-A Animal       → inheritance
Car HAS-A Engine      → composition
```

Composition can make designs more flexible because a component can be supplied/replaced without making it a parent class.

---

# Dunder Methods

"Dunder" means double underscore.

Dunder methods allow custom objects to participate naturally in Python's built-in operations.

## `__str__`

Human-readable representation.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.name} earns {self.salary} INR"
```

```python
print(employee)
```

Conceptually:

```text
print(obj)
   ↓
obj.__str__()
```

---

## `__repr__`

Developer/debug representation.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"Employee({self.name!r}, {self.salary!r})"
```

```python
repr(employee)
```

`__repr__` is also commonly visible when objects appear inside collections.

Mental model:

```text
__str__  → human-friendly
__repr__ → developer/debug-friendly
```

---

## `__len__`

Defines behavior for `len(obj)`.

```python
class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)
```

```python
len(team)
```

Conceptually:

```text
len(team)
   ↓
team.__len__()
```

---

## `__eq__`

Defines equality behavior for `==`.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.price == other.price
        )
```

```python
p1 == p2
```

Conceptually:

```text
p1 == p2
   ↓
p1.__eq__(p2)

self  → p1
other → p2
```

---

## `__iter__`

Allows a custom object to provide an iterator and work in a `for` loop.

```python
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __iter__(self):
        return iter(self.songs)
```

```python
for song in playlist:
    print(song)
```

Conceptually:

```text
for x in obj
    ↓
iter(obj)
    ↓
obj.__iter__()
```

`__iter__` provides the iterator; it does not necessarily perform all iteration itself.

---

## `__call__`

Makes an object callable like a function.

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor
```

```python
triple = Multiplier(3)
print(triple(10))
```

Conceptually:

```text
triple(10)
    ↓
triple.__call__(10)
```

This is similar to a function carrying state, which connects naturally to closures.

---

# Properties

Properties provide controlled attribute-style access to internal state.

## Getter

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance
```

Now:

```python
account.balance
```

calls the getter.

Mental model:

```text
account.balance
       ↓
@property getter
       ↓
self._balance
```

---

## Setter

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Balance cannot be negative")
```

Now:

```python
account.balance = 10000
```

calls the setter.

The setter can validate before changing internal state.

```text
account.balance = 10000
          ↓
     balance.setter
          ↓
      validation
          ↓
    _balance changes
```

### Getter vs Setter

```text
Getter → controlled read access
Setter → controlled write/update access
```

Properties are useful because the outside interface can remain:

```python
account.balance
```

while the internal implementation remains:

```python
account._balance
```

---

# Quick OOP Mental Map

```text
CLASS
  ↓
creates OBJECTS

ENCAPSULATION
  ↓
controls internal state

ABSTRACTION
  ↓
exposes required behavior/contracts

INHERITANCE
  ↓
IS-A

POLYMORPHISM
  ↓
same interface, different behavior

COMPOSITION
  ↓
HAS-A

DUNDER METHODS
  ↓
customize Python operations

PROPERTIES
  ↓
controlled attribute access
```

---

# Recommended Revision Order

When revising, do not memorize definitions only.

For every concept ask:

1. What problem does it solve?
2. What is the mental model?
3. What Python syntax implements it?
4. What happens internally?
5. When would I use it?
6. Can I explain it without looking at notes?
