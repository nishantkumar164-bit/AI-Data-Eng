# Python OOP — Module 5 Assignments

## How to use this file

Solve the problems **without looking at the solution first**.

Recommended workflow:

1. Read the requirement.
2. Design the classes.
3. Code it yourself.
4. Test edge cases.
5. Explain your design in plain English.
6. Only then compare with your notes/examples.

---

# Level 1 — Fundamentals

## Assignment 1: Student Class

Create a `Student` class.

Requirements:

- `name`
- `age`
- `marks`
- Method `is_passed()`
- A student passes when marks >= 40.
- Add a `__str__` method.

Example:

```python
student = Student("Nishant", 25, 72)

print(student)
print(student.is_passed())
```

Expected idea:

```text
Student: Nishant, Marks: 72
True
```

---

## Assignment 2: Employee

Create an `Employee` class with:

- `name`
- `salary`
- `department`

Methods:

- `display_details()`
- `give_raise(amount)`

Rules:

- Raise must be greater than zero.
- Salary should increase after a valid raise.

---

# Level 2 — Class and Static Methods

## Assignment 3: Employee Company

Create an `Employee` class with a class attribute:

```python
company = "ABC"
```

Add a class method:

```python
change_company(cls, new_company)
```

Verify that changing the company through the class method changes the class-level value.

Then explain:

- Why is this a class method?
- Why would an instance method be less appropriate here?

---

## Assignment 4: Alternative Constructor

Create a `Product` class:

```text
name
price
category
```

Add a class method:

```python
from_string(cls, data)
```

Input:

```text
"Laptop,50000,Electronics"
```

Expected:

```python
product = Product.from_string("Laptop,50000,Electronics")
```

---

## Assignment 5: Static Validation

Create a `User` class.

Add a static method:

```python
is_valid_email(email)
```

It should return `True` if the email contains `@` and `.`.

The method should not depend on:

- `self`
- `cls`

---

# Level 3 — Encapsulation

## Assignment 6: Bank Account

Create:

```python
class BankAccount:
```

Attributes:

- `owner`
- `_balance`

Methods:

- `deposit(amount)`
- `withdraw(amount)`
- `get_balance()`

Rules:

- Deposit must be greater than zero.
- Withdrawal must be greater than zero.
- Withdrawal cannot exceed balance.
- Invalid operations should not change balance.

Test:

```text
Starting balance: 5000
Deposit: 2000
Withdraw: 1000
Withdraw: 10000
```

Explain why `_balance` is not truly private in Python.

---

## Assignment 7: Investigate `_balance`

Create:

```python
account = BankAccount("Nishant", 5000)
```

Try:

```python
account._balance = -10000
```

Observe what happens.

Then answer:

1. Does `_balance` actually prevent external modification?
2. What does `_` communicate to developers?
3. Why might properties be better for controlled access?

---

# Level 4 — Abstraction

## Assignment 8: Payment System

Create an abstract class:

```python
Payment
```

with an abstract method:

```python
pay(amount)
```

Create at least three implementations:

- `CreditCardPayment`
- `UPIPayment`
- `CashPayment`

Each class should implement `pay()` differently.

Then write:

```python
payments = [...]
```

and loop over them.

Explain why the parent class has `pay()` even though it doesn't implement the actual payment process.

---

# Level 5 — Inheritance and Polymorphism

## Assignment 9: Animal Hierarchy

Create:

```text
Animal
 ├── Dog
 ├── Cat
 └── Cow
```

Parent:

```python
eat()
```

Each child:

```python
speak()
```

Override `speak()` in each subclass.

Then:

```python
animals = [Dog(), Cat(), Cow()]
```

Loop through them and call:

```python
animal.speak()
```

Explain why this is polymorphism.

---

## Assignment 10: Employee Hierarchy

Create:

```text
Employee
 ├── Developer
 └── Manager
```

Parent:

- `name`
- `salary`

Method:

```python
work()
```

Override `work()` in both subclasses.

Then demonstrate polymorphism with a list of employees.

---

# Level 6 — Composition

## Assignment 11: Car and Engine

Create:

```text
Engine
Car
```

`Engine` should have:

```python
start()
```

`Car` should receive an engine through its constructor.

```python
car = Car(engine)
```

The car should delegate starting to the engine.

Then explain:

> Why is composition more appropriate than making `Car` inherit from `Engine`?

---

## Assignment 12: Computer

Create:

```text
CPU
RAM
Computer
```

A computer HAS-A CPU and HAS-A RAM.

Example:

```python
computer = Computer(cpu, ram)
```

Add a method:

```python
show_specs()
```

---

# Level 7 — Dunder Methods

## Assignment 13: `__str__`

Create a `Book` class:

- `title`
- `author`
- `price`

Implement `__str__`.

Expected style:

```text
Clean Code by Robert Martin - 1200 INR
```

---

## Assignment 14: `__repr__`

Extend the `Book` class with `__repr__`.

Make the representation useful for debugging.

Then compare:

```python
print(book)
print(repr(book))
```

Explain the difference.

---

## Assignment 15: `__len__`

Create a `ShoppingCart`.

It contains a list of items.

Make this work:

```python
len(cart)
```

The result should be the number of items.

---

## Assignment 16: `__eq__`

Create a `Product` class.

Two products should be equal if:

- their name is equal
- their price is equal

Test:

```python
p1 == p2
p1 == p3
```

Also test comparison with a different object type and think about why `NotImplemented` can be useful.

---

## Assignment 17: `__iter__`

Create a `Playlist`.

It should contain songs.

Make this work:

```python
for song in playlist:
    print(song)
```

Do not expose the internal list directly in the loop.

Use `__iter__`.

---

## Assignment 18: `__call__`

Create a class:

```python
Power
```

Constructor:

```python
Power(exponent)
```

Make this work:

```python
square = Power(2)
cube = Power(3)

print(square(5))
print(cube(5))
```

Expected:

```text
25
125
```

Explain what Python calls internally when `square(5)` executes.

---

# Level 8 — Properties

## Assignment 19: Bank Account Property

Refactor your `BankAccount` to use:

```python
@property
def balance(self):
    ...
```

and:

```python
@balance.setter
def balance(self, amount):
    ...
```

Rules:

- Balance cannot be negative.
- Reading uses `account.balance`.
- Updating uses `account.balance = value`.

Do NOT require the user to call:

```python
get_balance()
```

for normal reading.

---

## Assignment 20: Read-only Property

Create a `Circle`.

Internal attribute:

```python
_radius
```

Properties:

```python
radius
area
```

Requirements:

- `radius` should be readable.
- `radius` should be settable only if it is positive.
- `area` should be calculated automatically.
- Do not create an `area` setter.

---

# Level 9 — Integrated Challenge

## Assignment 21: E-Commerce Order

Build an `Order` system using several OOP concepts.

### `Order`

Attributes:

- customer
- `_amount`

Property:

```python
amount
```

Rules:

- Amount cannot be negative.

Dunder methods:

- `__str__`
- `__repr__`
- `__eq__`

Two orders are equal when customer and amount are equal.

### Payment abstraction

Create:

```text
Payment
 ├── CreditCardPayment
 ├── UPIPayment
 └── CashPayment
```

Use an abstract `pay()` method.

### Composition

`Order` should HAVE-A payment method.

Example:

```python
order = Order("Nishant", 2500, UPIPayment())
```

Then:

```python
order.pay()
```

The order delegates payment to the payment object.

---

# Level 10 — Explain Without Code

For each statement, explain whether it represents inheritance or composition.

1. `Dog IS-A Animal`
2. `Car HAS-A Engine`
3. `Developer IS-A Employee`
4. `Computer HAS-A CPU`
5. `Manager IS-A Employee`
6. `Order HAS-A PaymentMethod`

Then explain why.

---

# Interview Preparation Assignments

## Assignment 22

Explain the difference between:

```text
Encapsulation
Abstraction
```

Give one Python example for each.

---

## Assignment 23

Explain:

```text
Inheritance vs Composition
```

Use:

```text
Car + Engine
```

as your example.

---

## Assignment 24

Explain the difference between:

```text
__str__
__repr__
```

Then explain why a list containing objects often shows their `repr` representation.

---

## Assignment 25

Explain:

```text
@property
getter
setter
```

using `BankAccount`.

---

## Assignment 26

Explain what happens internally for:

```python
print(obj)
len(obj)
obj1 == obj2
for x in obj:
obj()
```

Map each operation to its dunder method.

---

# Final Mastery Challenge

Build a small **Library Management System**.

Use at least:

- Classes
- Objects
- `__init__`
- Instance methods
- Class method
- Static method
- Encapsulation
- Abstraction
- Inheritance
- Polymorphism
- Composition
- `__str__`
- `__repr__`
- `__len__`
- `__eq__`
- `__iter__`
- `__call__`
- `@property`
- Getter
- Setter

Do not force a concept where it does not make sense.

The goal is not:

> "Use every OOP feature."

The goal is:

> "Choose the appropriate OOP feature for the problem and explain why."
