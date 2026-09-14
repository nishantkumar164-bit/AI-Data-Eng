# Python OOP — Interview Questions & Answers

This file is for interview revision after completing the concepts.

---

# 1. What is OOP?

**Answer:**

OOP (Object-Oriented Programming) is a programming approach where we organize code around objects that contain data and behavior.

A class defines the structure/behavior, while an object is an instance created from that class.

---

# 2. What is the difference between a class and an object?

**Answer:**

A class is a blueprint; an object is an actual instance of that blueprint.

```python
class Employee:
    pass

employee = Employee()
```

`Employee` is the class and `employee` is the object.

---

# 3. What is `self`?

**Answer:**

`self` refers to the current instance of the class.

```python
class Employee:

    def __init__(self, name):
        self.name = name
```

When:

```python
employee = Employee("Rahul")
```

`self` refers to `employee`.

---

# 4. What is `__init__`?

**Answer:**

`__init__` initializes an object's instance state when the object is created.

```python
class Employee:

    def __init__(self, name):
        self.name = name
```

It is commonly used to initialize instance attributes.

---

# 5. What is an instance method?

**Answer:**

An instance method operates on an instance and receives `self`.

```python
def introduce(self):
    return self.name
```

It is normally called through an object.

---

# 6. Class method vs instance method?

| Instance Method | Class Method |
|---|---|
| Receives `self` | Receives `cls` |
| Works with instance state | Works with class state |
| Called on an object | Can be called on class |
| No decorator required | Uses `@classmethod` |

---

# 7. What is a static method?

**Answer:**

A static method is a method placed inside a class namespace that does not automatically receive `self` or `cls`.

```python
@staticmethod
def add(a, b):
    return a + b
```

It is useful when the operation logically belongs to the class but does not need instance/class state.

---

# 8. What is encapsulation?

**Answer:**

Encapsulation is about keeping internal state and implementation controlled behind an interface.

Python commonly uses `_name` to communicate that an attribute is intended for internal use.

Important:

> `_name` does not create strict private access control.

---

# 9. Is `_balance` private in Python?

**Answer:**

No, not strictly.

```python
account._balance = 10000
```

is technically allowed.

The single underscore is a convention communicating:

> "This is intended for internal use."

---

# 10. What is abstraction?

**Answer:**

Abstraction exposes required behavior while hiding implementation details.

Python can implement formal abstraction using `ABC` and `@abstractmethod`.

```python
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

The abstract class defines the required contract.

---

# 11. Why define an abstract method if the parent doesn't implement it?

**Answer:**

Because the parent class can define a contract.

For example:

```python
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

This communicates:

> Every concrete payment type must provide `pay()`.

The parent defines **what capability is required**, while subclasses define **how it works**.

---

# 12. What is inheritance?

**Answer:**

Inheritance allows a child class to derive behavior and structure from a parent class.

It normally represents an **IS-A** relationship.

```python
class Dog(Animal):
    pass
```

A dog is an animal.

---

# 13. What is method overriding?

**Answer:**

When a child class provides its own implementation of a method inherited from the parent.

```python
class Animal:
    def speak(self):
        print("Sound")


class Dog(Animal):
    def speak(self):
        print("Woof")
```

`Dog` overrides `speak()`.

---

# 14. What is polymorphism?

**Answer:**

Polymorphism allows the same interface/operation to work with different object types while each object provides its own behavior.

```python
for animal in animals:
    animal.speak()
```

A `Dog` and a `Cat` can both provide `speak()` differently.

---

# 15. What is the difference between inheritance and composition?

**Answer:**

Use the relationship test:

```text
IS-A  → Inheritance
HAS-A → Composition
```

Example:

```text
Dog IS-A Animal
Car HAS-A Engine
```

Composition means one object contains/uses another object.

---

# 16. Why is composition often preferred over inheritance?

**Answer:**

Composition can reduce strong coupling between classes and makes it easier to replace components.

For example:

```python
class Car:
    def __init__(self, engine):
        self.engine = engine
```

A car can receive different engine implementations without becoming a subclass of an engine.

However, this does not mean composition should always replace inheritance. Use inheritance when the IS-A relationship genuinely exists.

---

# 17. What are dunder methods?

**Answer:**

Dunder methods are special methods whose names use double underscores.

Examples:

```text
__str__
__repr__
__len__
__eq__
__iter__
__call__
```

They allow custom objects to integrate with Python's built-in syntax and protocols.

---

# 18. What does `__str__` do?

**Answer:**

It defines a human-readable string representation of an object.

```python
print(obj)
```

typically invokes:

```python
obj.__str__()
```

---

# 19. What is the difference between `__str__` and `__repr__`?

**Answer:**

```text
__str__  → human-friendly
__repr__ → developer/debug-friendly
```

Example:

```python
def __str__(self):
    return "Rahul - 50000 INR"

def __repr__(self):
    return "Employee('Rahul', 50000)"
```

---

# 20. What happens when an object is inside a list?

For example:

```python
employees = [employee]
print(employees)
```

Python generally uses the object's `__repr__` representation when representing the object inside the collection.

This is why defining a useful `__repr__` is valuable for debugging.

---

# 21. What does `__len__` do?

**Answer:**

It defines how `len(obj)` behaves.

```python
len(obj)
```

conceptually invokes:

```python
obj.__len__()
```

---

# 22. What does `__eq__` do?

**Answer:**

It defines equality behavior for `==`.

```python
obj1 == obj2
```

conceptually invokes:

```python
obj1.__eq__(obj2)
```

Inside the method:

```text
self  → obj1
other → obj2
```

---

# 23. What does `__iter__` do?

**Answer:**

It provides an iterator for the object so it can participate in iteration.

```python
for item in obj:
    ...
```

uses the object's iteration protocol, including `__iter__`.

Example:

```python
def __iter__(self):
    return iter(self.items)
```

---

# 24. What does `__call__` do?

**Answer:**

It makes an instance callable.

```python
obj(10)
```

conceptually invokes:

```python
obj.__call__(10)
```

This allows a custom object to behave syntactically like a function.

---

# 25. How is `__call__` related to closures?

**Answer:**

Both can create callable things that retain state.

A closure can retain variables from its enclosing scope.

A callable object can retain state in instance attributes.

Example:

```python
class Multiplier:

    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor
```

The object carries `factor` as state.

---

# 26. What is `@property`?

**Answer:**

`@property` allows a method to be accessed using attribute syntax.

Instead of:

```python
account.get_balance()
```

we can expose:

```python
account.balance
```

while still controlling how the value is retrieved.

---

# 27. What is a getter?

**Answer:**

A getter provides controlled read access to internal state.

```python
@property
def balance(self):
    return self._balance
```

Then:

```python
account.balance
```

invokes the getter.

---

# 28. What is a setter?

**Answer:**

A setter provides controlled write/update access.

```python
@balance.setter
def balance(self, amount):
    if amount >= 0:
        self._balance = amount
```

Then:

```python
account.balance = 10000
```

invokes the setter.

---

# 29. Why use properties instead of public attributes?

**Answer:**

Properties allow validation and controlled access without forcing callers to use explicit getter/setter methods.

For example:

```python
account.balance = -100
```

can be rejected by the setter.

The public interface remains:

```python
account.balance
```

while internal storage can remain:

```python
self._balance
```

---

# 30. Is `@property` the same as abstraction?

**Answer:**

They can support abstraction and encapsulation, but they are not the same concept.

- `@property` is a Python mechanism for attribute-style access.
- Encapsulation is about controlling internal state/implementation.
- Abstraction is about exposing essential behavior while hiding implementation details.

Properties are commonly used as part of an encapsulated interface.

---

# 31. Explain this code

```python
@property
def balance(self):
    return self._balance
```

**Answer:**

It creates a property named `balance`.

When the caller writes:

```python
account.balance
```

Python invokes the getter method and returns `_balance`.

---

# 32. Explain this code

```python
@balance.setter
def balance(self, amount):
    self._balance = amount
```

**Answer:**

It attaches a setter to the existing `balance` property.

When:

```python
account.balance = 5000
```

is executed, Python invokes the setter and passes `5000` as `amount`.

---

# 33. Why must the setter use the same property name?

Correct:

```python
@property
def balance(self):
    ...


@balance.setter
def balance(self, amount):
    ...
```

The setter attaches itself to the existing `balance` property.

This gives one public interface:

```python
account.balance
account.balance = 5000
```

---

# 34. What is the difference between a setter and a deposit method?

**Answer:**

A setter generally means:

> Set the value to this value.

```python
account.balance = 10000
```

A deposit method represents a domain operation:

> Add this amount to the existing balance.

```python
account.deposit(1000)
```

So:

```python
self._balance = amount
```

and:

```python
self._balance += amount
```

represent different semantics.

---

# 35. Explain the following mapping

```text
print(obj)       → __str__
repr(obj)        → __repr__
len(obj)         → __len__
obj1 == obj2     → __eq__
for x in obj     → __iter__
obj()            → __call__
```

**Answer:**

These are Python operations that can invoke corresponding special methods on custom objects.

The benefit is that custom classes can behave naturally with Python's built-in syntax.

---

# 36. Scenario Question

You have:

```text
Car
Engine
```

Should `Car` inherit from `Engine`?

**Answer:**

No.

The relationship is:

```text
Car HAS-A Engine
```

so composition is more appropriate.

---

# 37. Scenario Question

You have:

```text
Animal
Dog
Cat
```

Should `Dog` inherit from `Animal`?

**Answer:**

Yes, assuming the model genuinely represents:

```text
Dog IS-A Animal
```

Inheritance is appropriate.

---

# 38. Scenario Question

You need different payment implementations:

```text
CreditCard
UPI
Cash
```

They all must implement:

```python
pay(amount)
```

What OOP concepts could be appropriate?

**Answer:**

Abstraction can define the `Payment` contract, inheritance can provide the relationship to the abstract base class, and polymorphism allows the caller to use different payment objects through the same `pay()` interface.

---

# 39. Coding Interview Question

Design:

```text
Payment
 ├── CreditCardPayment
 ├── UPIPayment
 └── CashPayment
```

Requirements:

- Parent defines `pay()`.
- Child classes implement it.
- A function should accept any payment object.
- The function should call `pay()` without checking the concrete class.

What concept does this demonstrate?

**Expected answer:**

Abstraction + polymorphism.

---

# 40. Final Interview Mental Model

If asked to explain the OOP concepts quickly:

```text
Class/Object
→ Structure and instances

Encapsulation
→ Control internal state

Abstraction
→ Hide implementation, expose required contract

Inheritance
→ IS-A relationship

Polymorphism
→ Same interface, different behavior

Composition
→ HAS-A relationship

Dunder methods
→ Integrate custom objects with Python syntax

Properties
→ Controlled attribute-style read/write access
```

---

# Interview Rule

Do not answer only with definitions.

A strong answer should follow:

```text
Concept
  ↓
Problem it solves
  ↓
Python mechanism
  ↓
Small example
  ↓
When to use it
```

For example:

> "I use composition when the relationship is HAS-A rather than IS-A. For example, a Car has an Engine, so I would inject an Engine into Car rather than inherit Car from Engine. This keeps the components more flexible."
