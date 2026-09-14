# Python OOP --- Day 4 Study Notes

## What we covered

Today we built the first major part of Python Object-Oriented
Programming using a memory-mapping approach rather than memorizing
syntax.

Covered topics:

-   Classes
-   Objects / Instances
-   `self`
-   `__init__`
-   Instance variables
-   Class variables
-   Attribute lookup and shadowing
-   Instance methods
-   Class methods
-   Static methods
-   Inheritance
-   Child `__init__`
-   `super()`
-   Method overriding
-   Method lookup
-   MRO
-   Multiple inheritance
-   Diamond problem
-   Polymorphism
-   Duck typing

------------------------------------------------------------------------

# 1. Why OOP?

Without OOP, data and functions can become increasingly disconnected as
an application grows.

For example:

``` python
customer1_name = "Rahul"
customer1_balance = 50000

def deposit(balance, amount):
    return balance + amount
```

OOP groups related **state + behavior** into objects.

Mental model:

``` text
                    Customer
                       |
             +---------+---------+
             |                   |
            DATA             BEHAVIOR
             |                   |
          name              deposit()
          balance           withdraw()
          account_no        transfer()
```

### Memory hook

> OOP bundles related data and behavior together.

------------------------------------------------------------------------

# 2. Class vs Object

A **class** describes what an object should contain and what it can do.

An **object** is an actual instance created from that class.

``` python
class Customer:
    pass

c1 = Customer()
c2 = Customer()
```

Mental model:

``` text
Class
 |
 +---- Object 1
 |
 +---- Object 2
```

### Memory hook

> Class describes. Object exists.

------------------------------------------------------------------------

# 3. `self`

`self` refers to the **current instance itself**.

Example:

``` python
class Employee:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)
```

When:

``` python
e1.display()
```

is called, conceptually Python does something similar to:

``` python
Employee.display(e1)
```

Therefore:

``` text
self -> e1
self.name -> e1.name
```

If:

``` python
e2.display()
```

then:

``` text
self -> e2
```

### Important distinction

> `self` = the current object\
> `self.attribute` = data belonging to that object

`self` is a conventional parameter name, not a Python keyword.

------------------------------------------------------------------------

# 4. `__init__`

`__init__` initializes an already-created instance.

``` python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
```

Creating:

``` python
e1 = Employee("Rahul", 50000)
```

results conceptually in:

``` text
e1
 |
 +-- name   -> Rahul
 +-- salary -> 50000
```

### Memory hook

> Object creation and object initialization are related but distinct.
> `__init__` performs initialization.

Technically, Python's object creation process involves `__new__`;
`__init__` initializes the instance.

------------------------------------------------------------------------

# 5. Instance Variables

Instance variables belong to an individual object.

``` python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
```

``` python
e1 = Employee("Rahul", 50000)
e2 = Employee("Amit", 70000)
```

Conceptually:

``` text
e1                  e2
 |                   |
 +-- name Rahul      +-- name Amit
 +-- salary 50000    +-- salary 70000
```

Changing:

``` python
e1.salary = 60000
```

does not change `e2.salary`.

### Memory hook

> Instance variable = object-specific state.

------------------------------------------------------------------------

# 6. Class Variables

A class variable is defined on the class.

``` python
class Employee:
    company = "ABC Corp"

    def __init__(self, name):
        self.name = name
```

Both objects can access:

``` python
e1.company
e2.company
```

because attribute lookup can fall back to the class.

Important: Python does **not** simply copy the class variable into every
object.

------------------------------------------------------------------------

# 7. Attribute Lookup and Shadowing

Consider:

``` python
class Employee:
    company = "ABC"

e1 = Employee()
e2 = Employee()
```

Initially:

``` python
e1.company
```

works by looking at the class because `e1` has no own `company`.

Mental model:

``` text
e1.company
    |
    +-- Is it on e1? No
    |
    +-- Look at class
            |
            +-- Employee.company -> "ABC"
```

Now:

``` python
e1.company = "XYZ"
```

creates an instance attribute:

``` text
Employee
 |
 +-- company = ABC

e1
 |
 +-- company = XYZ

e2
 |
 +-- no company
```

Therefore:

``` python
e1.company       # XYZ
e2.company       # ABC
Employee.company # ABC
```

The instance attribute **shadows** the class attribute.

### Very important correction

Do not think:

> "The object inherited/copied the class variable."

Think:

> "If the instance doesn't have the attribute, lookup can fall back to
> the class."

------------------------------------------------------------------------

# 8. Instance Methods

An instance method operates on a particular object.

``` python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, amount):
        self.salary += amount
```

Calling:

``` python
e1.increase_salary(5000)
```

conceptually passes `e1` as `self`.

Use an instance method when the operation needs or modifies
object-specific state.

------------------------------------------------------------------------

# 9. Class Methods

A class method operates with the class.

``` python
class Employee:

    company = "ABC"

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
```

Calling:

``` python
Employee.change_company("XYZ")
```

means conceptually:

``` text
cls -> Employee
```

Use a class method when the operation needs class-level state or
represents an alternative class-level constructor/operation.

### Memory hook

``` text
self -> instance
cls  -> class
```

------------------------------------------------------------------------

# 10. Static Methods

A static method does not require an instance or class.

``` python
class Employee:

    @staticmethod
    def is_valid_salary(salary):
        return salary > 0
```

Usage:

``` python
Employee.is_valid_salary(50000)
```

Use it when the operation is logically related to the class but needs
neither instance state nor class state.

------------------------------------------------------------------------

# 11. Choosing the Method Type

Ask these questions:

``` text
Does the operation need object-specific state?
    |
   YES -> instance method -> self

Does it need class-level state?
    |
   YES -> class method -> cls

Does it need neither?
    |
   YES -> static method
```

Examples:

``` text
deposit()                 -> instance method
withdraw()                -> instance method
change_bank_name()        -> class method
is_valid_account_number() -> static method
```

------------------------------------------------------------------------

# 12. Inheritance

Inheritance allows a child class to reuse and specialize behavior from a
parent class.

Example:

``` python
class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Woof")
```

Now:

``` python
dog = Dog()

dog.eat()   # inherited
dog.bark()  # Dog's own method
```

Mental model:

``` text
Animal
 |
 +-- eat()
 |
Dog
 |
 +-- bark()
```

### Memory hook

> Inheritance represents an **IS-A** relationship.

Examples:

``` text
Dog IS-A Animal
Developer IS-A Employee
Car IS-A Vehicle
```

But:

``` text
Engine IS-A Car      -> No
Engine is part of Car -> Yes
```

That distinction becomes important when we study composition.

------------------------------------------------------------------------

# 13. Inherited `__init__`

If the child doesn't define its own `__init__`, it can use the inherited
initialization behavior.

``` python
class Animal:

    def __init__(self, name, food):
        self.name = name
        self.food = food


class Dog(Animal):
    pass
```

This works:

``` python
dog = Dog("Dexter", "Chicken")
```

The inherited initializer initializes the Dog instance.

------------------------------------------------------------------------

# 14. Child `__init__`

A child defines its own `__init__` when it needs different/additional
initialization behavior.

Example:

``` python
class Animal:

    def __init__(self, name, food):
        self.name = name
        self.food = food


class Dog(Animal):

    def __init__(self, name, food, breed):
        self.breed = breed
        super().__init__(name, food)
```

Creating:

``` python
dog = Dog("Dexter", "Chicken", "Labrador")
```

results in:

``` text
dog
 |
 +-- name = Dexter
 +-- food = Chicken
 +-- breed = Labrador
```

### Memory hook

> Parent owns parent state. Child owns child state.

------------------------------------------------------------------------

# 15. `super()`

The beginner approximation:

> `super()` lets the child use parent behavior.

The more accurate Python mental model:

> `super()` continues method lookup according to the MRO, starting after
> the current class.

For simple inheritance:

``` text
Dog -> Animal -> object
```

inside `Dog`:

``` python
super().eat()
```

will find `Animal.eat()`.

Do not permanently memorize:

> `super()` = one level up.

That breaks down with multiple inheritance.

------------------------------------------------------------------------

# 16. Method Overriding

A child can define a method with the same name as the parent.

``` python
class Animal:

    def eat(self):
        print("Animal eating")


class Dog(Animal):

    def eat(self):
        print("Dog eating")
```

Now:

``` python
dog = Dog()
dog.eat()
```

prints:

``` text
Dog eating
```

because Python finds `eat()` in `Dog` first.

### Memory hook

> Inheritance: "I can use your behavior."\
> Overriding: "I want my own version."

------------------------------------------------------------------------

# 17. Method Lookup

For:

``` python
dog.eat()
```

Python needs to find `eat`.

In simple inheritance, think:

``` text
dog
 |
Dog
 |
Animal
 |
object
```

It searches according to the inheritance/MRO order until the attribute
is found.

If Dog has `eat`, Animal's `eat` is not reached.

If Dog doesn't have it, Python can find Animal's `eat`.

------------------------------------------------------------------------

# 18. MRO --- Method Resolution Order

MRO is the ordered sequence Python uses when resolving
attributes/methods through inheritance.

For:

``` python
class Animal:
    pass

class Dog(Animal):
    pass
```

conceptually:

``` text
Dog -> Animal -> object
```

You can inspect it with:

``` python
Dog.mro()
```

or:

``` python
Dog.__mro__
```

------------------------------------------------------------------------

# 19. Multiple Inheritance

Python allows:

``` python
class A:
    pass

class B:
    pass

class C(A, B):
    pass
```

Conceptually:

``` text
    C
   / \
  A   B
   \ /
   object
```

Python needs a deterministic lookup order.

For the simple example above:

``` text
C -> A -> B -> object
```

------------------------------------------------------------------------

# 20. Diamond Problem

The diamond structure:

``` text
       A
      / \
     B   C
      \ /
       D
```

Example:

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
```

The MRO is conceptually:

``` text
D -> B -> C -> A -> object
```

Calling:

``` python
d = D()
d.show()
```

produces:

``` text
B
C
A
```

### Why?

`super()` does not simply mean "my immediate parent."

Inside `B`, Python continues after `B` in D's MRO:

``` text
D -> B -> C -> A -> object
         ^
       next
```

So it goes to `C`.

Inside `C`, it continues to `A`.

### Memory hook

> `super()` = next implementation in the MRO.

------------------------------------------------------------------------

# 21. `super()` with a Child Override

``` python
class Animal:

    def eat(self):
        print("Animal eating")


class Dog(Animal):

    def eat(self):
        print("Dog eating")
        super().eat()
```

Calling:

``` python
Dog().eat()
```

produces:

``` text
Dog eating
Animal eating
```

Execution:

``` text
Dog.eat()
 |
 +-- Dog behavior
 |
 +-- super().eat()
          |
          +-- Animal.eat()
```

------------------------------------------------------------------------

# 22. Polymorphism

Poly = many\
Morph = forms

Polymorphism means that the same operation/interface can result in
different behavior depending on the object.

``` python
class Dog:

    def speak(self):
        print("Woof")


class Cat:

    def speak(self):
        print("Meow")


def make_sound(obj):
    obj.speak()
```

Then:

``` python
make_sound(Dog())
make_sound(Cat())
```

produces:

``` text
Woof
Meow
```

### Memory hook

> One interface/operation, many implementations.

------------------------------------------------------------------------

# 23. Duck Typing

Duck typing is Python's behavior-focused approach.

The function:

``` python
def make_sound(obj):
    obj.speak()
```

does not need to ask:

``` text
"Are you a Dog?"
"Are you a Cat?"
"Do you inherit from Animal?"
```

It simply assumes the object provides:

``` python
speak()
```

So this works:

``` python
class Robot:

    def speak(self):
        print("Beep")
```

even if Robot has no relationship with Dog or Animal.

``` python
make_sound(Robot())
```

works because Robot provides `speak()`.

But:

``` python
class Robot:

    def beep(self):
        print("Beep")
```

will fail with `make_sound(Robot())`, because the function specifically
calls:

``` python
obj.speak()
```

and Robot doesn't provide `speak`.

### Memory hook

> Don't care what you are. Care what you can do.

------------------------------------------------------------------------

# 24. Polymorphism vs Duck Typing

### Polymorphism

The broader concept:

> Different objects can respond to the same operation with different
> behavior.

### Duck typing

Python's dynamic approach:

> Use an object's capabilities rather than requiring a particular
> explicit type/inheritance relationship.

Interview answer:

> Polymorphism does not require inheritance in Python. Duck typing
> allows unrelated objects to participate in the same operation as long
> as they provide the required behavior.

------------------------------------------------------------------------

# Master Memory Map

``` text
                         OOP
                          |
              +-----------+-----------+
              |                       |
           OBJECTS                 BEHAVIOR
              |                       |
            CLASS                  METHODS
              |                       |
       +------+-------+       +-------+-------+
       |              |       |       |       |
   Instance         Class   Instance Class  Static
   Variables       Variables Method  Method Method
       |              |       |       |       |
       +--------------+-------+-------+-------+
                          |
                   Attribute Lookup
                          |
                 instance -> class
                          |
                       Inheritance
                          |
                 +--------+--------+
                 |                 |
            Overriding        Multiple Inheritance
                 |                 |
                 |                MRO
                 |                 |
                 +-------> super()
                              |
                              |
                         Polymorphism
                              |
                         Duck Typing
```

------------------------------------------------------------------------

# What comes next

We stopped here today.

Next session:

``` text
Encapsulation
    |
Abstraction
    |
Composition vs Inheritance
    |
Dunder Methods
    +-- __str__
    +-- __repr__
    +-- __len__
    +-- __eq__
    +-- __iter__
    +-- __call__
    |
Properties
    +-- @property
    +-- Getter
    +-- Setter
    |
SOLID Principles
```
