# Python OOP --- Day 4 Assignments

These assignments cover everything we discussed today.

## How to use this file

For each problem:

1.  Predict the behavior first.
2.  Write the code yourself.
3.  Run it only after reasoning.
4.  Explain WHY the output occurs.
5.  Compare with the solution after attempting it.

------------------------------------------------------------------------

# Assignment 1 --- BankAccount Fundamentals

Create a `BankAccount` class with:

-   `account_number`
-   `owner`
-   `balance`

Create two accounts:

``` text
101, Rahul, 50000
102, Amit, 70000
```

Add an instance method:

``` text
display()
```

### Expected behavior

Each object should display its own account information.

### Your original solution from today's session

``` python
class Bank:

    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def display(self):
        print(self.account_number, self.owner, self.balance)


e1 = Bank(101, "Amit", 500000)
e2 = Bank(102, "Neha", 6000000)

e1.display()
e2.display()
```

### Review

This was correct.

A semantic improvement would be:

``` python
class BankAccount:
```

because each object represents an account rather than the entire bank.

------------------------------------------------------------------------

# Assignment 2 --- Class Variable

Modify the BankAccount class so that:

``` python
company = "ABC Technologies"
```

is a class variable.

Then demonstrate that two account objects can access the same
class-level value.

------------------------------------------------------------------------

# Assignment 3 --- Class Method

Add:

``` python
@classmethod
def change_company(cls, new_company):
    ...
```

Change the company to:

``` text
XYZ Technologies
```

Then verify the class-level value.

------------------------------------------------------------------------

# Assignment 4 --- Static Method

Add:

``` python
@staticmethod
def is_valid_salary(salary):
    ...
```

Return `True` when salary is greater than zero and `False` otherwise.

------------------------------------------------------------------------

# Assignment 5 --- Attribute Lookup

Predict the output before running:

``` python
class Employee:
    company = "ABC"

e1 = Employee()
e2 = Employee()

print(e1.company)

e1.company = "XYZ"

print(e1.company)
print(e2.company)
print(Employee.company)

Employee.company = "PQR"

print(e1.company)
print(e2.company)
print(Employee.company)
```

### Explain

Why does `e1.company` remain `"XYZ"` after `Employee.company` becomes
`"PQR"`?

### Expected reasoning

`e1.company = "XYZ"` created an instance attribute that shadows the
class attribute.

------------------------------------------------------------------------

# Assignment 6 --- Instance vs Class vs Static Method

Given:

``` python
class Employee:

    company = "ABC"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, amount):
        self.salary += amount

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    @staticmethod
    def calculate_bonus(salary):
        return salary * 0.10
```

Answer:

1.  Which method modifies one employee's salary?
2.  Which method changes the class-level company?
3.  Which method requires neither `self` nor `cls`?
4.  Why would `calculate_bonus()` not naturally be an instance method?

------------------------------------------------------------------------

# Assignment 7 --- Animal and Dog

Create:

``` text
Animal
  |
  Dog
```

Animal should have:

-   `name`
-   `food`
-   `eat()`
-   `sleep()`

Dog should have:

-   `breed`
-   `bark()`

Use inheritance.

------------------------------------------------------------------------

# Assignment 8 --- Child **init** + super()

Modify the Dog class so it accepts:

``` text
name
breed
food
```

Use:

``` python
super().__init__(name, food)
```

to let Animal initialize its state.

### Your corrected solution from today's session

``` python
class Animal:

    def __init__(self, name, food):
        self.name = name
        self.food = food

    def eat(self):
        print(f"I am {self.name} and I eat {self.food}")

    def sleep(self):
        print("I am Sleeping zzz")


class Dog(Animal):

    def __init__(self, name, breed, food):
        self.breed = breed
        super().__init__(name, food)

    def bark(self):
        print("I am barking !!")

    def fav_food(self, food):
        self.food = food
        print(
            f"I am {self.name} and my favourite food is {self.food}"
        )


animal1 = Animal("Tommy", "Chicken")
animal1.eat()
animal1.sleep()

animal2 = Dog("Dexter", "Labrador", "chicken")
animal2.eat()
animal2.sleep()
animal2.fav_food("Egg")
```

### What you learned from this

The child constructor receives all information needed to construct the
Dog:

``` text
name  -> parent
food  -> parent
breed -> child
```

Then:

``` python
super().__init__(name, food)
```

delegates parent-owned initialization to `Animal`.

------------------------------------------------------------------------

# Assignment 9 --- State vs Method Input

Modify `eat()` so both work:

``` python
dog.eat()
dog.eat("Egg")
```

Rules:

-   `dog.eat()` should use stored `self.food`
-   `dog.eat("Egg")` should use Egg only for that call
-   Calling `dog.eat("Egg")` should NOT automatically change `dog.food`

### Hint

Use a default parameter.

------------------------------------------------------------------------

# Assignment 10 --- Method Overriding

Create:

``` python
class Animal:
    def eat(self):
        print("Animal eating")


class Dog(Animal):
    def eat(self):
        print("Dog eating")
```

Predict:

``` python
Animal().eat()
Dog().eat()
```

Then explain why the Dog version runs for the Dog object.

------------------------------------------------------------------------

# Assignment 11 --- Override + super()

Modify Dog's `eat()` so that it:

1.  prints Dog's message
2.  calls Animal's `eat()`

Expected:

``` text
Dog eating
Animal eating
```

Use:

``` python
super().eat()
```

------------------------------------------------------------------------

# Assignment 12 --- Simple MRO

Given:

``` python
class A:
    pass

class B(A):
    pass

class C(B):
    pass
```

Predict:

``` python
C.mro()
```

Conceptually:

``` text
C -> B -> A -> object
```

------------------------------------------------------------------------

# Assignment 13 --- Multiple Inheritance

Given:

``` python
class A:
    def show(self):
        print("A")


class B:
    def show(self):
        print("B")


class C(A, B):
    pass
```

Answer:

1.  What does `C().show()` print?
2.  What is the conceptual MRO?
3.  Why is B not selected?

------------------------------------------------------------------------

# Assignment 14 --- Diamond Problem

Predict without running:

``` python
class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        print("B")
        super().show()


class C(A):

    def show(self):
        print("C")
        super().show()


class D(B, C):
    pass


D().show()
```

### Important

Do NOT reason:

``` text
B -> A -> C -> A
```

Instead reason using the MRO.

Conceptual MRO:

``` text
D -> B -> C -> A -> object
```

Expected output:

``` text
B
C
A
```

------------------------------------------------------------------------

# Assignment 15 --- Diamond + D Override

Predict:

``` python
class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        print("B")
        super().show()


class C(A):

    def show(self):
        print("C")
        super().show()


class D(B, C):

    def show(self):
        print("D")
        super().show()


D().show()
```

### Expected

``` text
D
B
C
A
```

### Explain

Why does `super()` inside B go to C rather than directly to A?

------------------------------------------------------------------------

# Assignment 16 --- Polymorphism

Create:

``` python
class Dog:
    def speak(self):
        print("Woof")


class Cat:
    def speak(self):
        print("Meow")
```

Write:

``` python
def make_sound(obj):
    ...
```

so that:

``` python
make_sound(Dog())
make_sound(Cat())
```

works without checking the object's type.

------------------------------------------------------------------------

# Assignment 17 --- Duck Typing

Add an unrelated class:

``` python
class Robot:
    def speak(self):
        print("Beep")
```

Make this work:

``` python
make_sound(Robot())
```

Then create:

``` python
class BrokenRobot:
    def beep(self):
        print("Beep")
```

Predict what happens:

``` python
make_sound(BrokenRobot())
```

### Explain

Why does Robot work while BrokenRobot fails?

------------------------------------------------------------------------

# Assignment 18 --- Interview Reasoning

Answer these without looking at the notes:

1.  What is the difference between a class and an object?
2.  What exactly does `self` represent?
3.  Why is `self.name` different from `name`?
4.  When would you use an instance method?
5.  When would you use a class method?
6.  When would you use a static method?
7.  What happens if a child doesn't define `__init__`?
8.  What happens if a child defines its own `__init__`?
9.  Why do we use `super()`?
10. Why is "`super()` means parent" an incomplete explanation?
11. What is method overriding?
12. What is MRO?
13. Why does multiple inheritance require MRO?
14. What is the Diamond Problem?
15. What is polymorphism?
16. What is duck typing?
17. Does polymorphism require inheritance in Python?
18. What does "instance attribute shadows class attribute" mean?

------------------------------------------------------------------------

# Assignment 19 --- Final Integrated Problem

Build this hierarchy:

``` text
                 Employee
                /        \
               /          \
      DataEngineer       Manager
```

`Employee`:

-   `name`
-   `salary`
-   `display()`

`DataEngineer`:

-   `cloud`
-   its own `display()`

`Manager`:

-   `team_size`
-   its own `display()`

Requirements:

1.  Use inheritance.
2.  Use child `__init__`.
3.  Use `super()`.
4.  Override `display()`.
5.  Store child-specific data as instance variables.
6.  Create one object of each child.
7.  Demonstrate polymorphism by putting them in a list and calling
    `display()`.

Do not use `isinstance()` or explicit type checks.

------------------------------------------------------------------------

# End-of-Day Self Check

Before moving to the next OOP chapter, you should be able to explain
this chain:

``` text
Class
  ↓
Object
  ↓
self
  ↓
__init__
  ↓
Instance variables
  ↓
Class variables
  ↓
Attribute lookup
  ↓
Instance/Class/Static methods
  ↓
Inheritance
  ↓
Child __init__
  ↓
super()
  ↓
Method overriding
  ↓
MRO
  ↓
Multiple inheritance
  ↓
Diamond problem
  ↓
Polymorphism
  ↓
Duck typing
```
