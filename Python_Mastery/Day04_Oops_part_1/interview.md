# Python OOP --- Day 4 Interview Preparation

## Core interview questions and answers

------------------------------------------------------------------------

## 1. What is OOP?

OOP is a programming paradigm that organizes related **state and
behavior** into objects created from classes.

A useful mental model:

``` text
Object = state + behavior
```

------------------------------------------------------------------------

## 2. What is a class?

A class is a blueprint/definition describing the attributes and behavior
that its instances can have.

Memory hook:

> Class describes. Object exists.

------------------------------------------------------------------------

## 3. What is an object?

An object is an instance created from a class.

``` python
class Employee:
    pass

e = Employee()
```

`Employee` is the class and `e` is an instance.

------------------------------------------------------------------------

## 4. What is `self`?

`self` refers to the current instance.

For:

``` python
e.display()
```

conceptually think:

``` python
Employee.display(e)
```

Therefore inside `display()`:

``` text
self -> e
```

`self` is a conventional name, not a Python keyword.

------------------------------------------------------------------------

## 5. What is the difference between `name` and `self.name`?

``` python
def __init__(self, name):
    self.name = name
```

`name` is a local parameter.

`self.name` is an attribute stored on the current object.

Memory:

``` text
name      -> incoming value
self.name -> object's stored state
```

------------------------------------------------------------------------

## 6. What is `__init__`?

`__init__` initializes an instance after it has been created.

It is commonly used to establish instance attributes.

Technically, `__init__` is not the low-level object creation mechanism;
`__new__` participates in object creation.

------------------------------------------------------------------------

## 7. What is an instance variable?

An instance variable belongs to an individual object.

``` python
self.name = name
self.salary = salary
```

Two objects can have different values for those attributes.

------------------------------------------------------------------------

## 8. What is a class variable?

A class variable is defined on the class and can be shared/accessed by
instances when they don't have their own attribute of the same name.

``` python
class Employee:
    company = "ABC"
```

------------------------------------------------------------------------

## 9. What happens when an instance and class have the same attribute?

Example:

``` python
class Employee:
    company = "ABC"

e = Employee()
e.company = "XYZ"
```

Now:

``` text
e.company       -> XYZ
Employee.company -> ABC
```

The instance attribute shadows the class attribute.

Important:

> The class value was not copied into the instance. Attribute lookup can
> fall back to the class.

------------------------------------------------------------------------

## 10. What is an instance method?

A method whose behavior operates on a particular instance.

``` python
def increase_salary(self, amount):
    self.salary += amount
```

Use it when the operation needs instance-specific state.

------------------------------------------------------------------------

## 11. What is a class method?

A method bound to the class.

``` python
@classmethod
def change_company(cls, name):
    cls.company = name
```

`cls` refers to the relevant class.

------------------------------------------------------------------------

## 12. What is a static method?

A method that does not receive an instance or class automatically.

``` python
@staticmethod
def is_valid_salary(salary):
    return salary > 0
```

Use it when the operation needs neither instance state nor class state.

------------------------------------------------------------------------

## 13. How do you decide between instance/class/static method?

Ask:

``` text
Needs instance state?
    -> instance method / self

Needs class state?
    -> class method / cls

Needs neither?
    -> static method
```

------------------------------------------------------------------------

## 14. What is inheritance?

Inheritance allows a child class to reuse and specialize behavior from a
parent.

Example:

``` python
class Dog(Animal):
    pass
```

The relationship should usually represent:

> Dog IS-A Animal.

------------------------------------------------------------------------

## 15. Does a child always need `__init__`?

No.

If the parent's initialization is sufficient:

``` python
class Dog(Animal):
    pass
```

Dog can use inherited initialization.

A child defines its own `__init__` when it needs different or additional
initialization behavior.

------------------------------------------------------------------------

## 16. What happens when the child defines `__init__`?

The child's `__init__` becomes the initialization method used for the
child.

The parent initializer does not automatically execute merely because
inheritance exists.

If the parent initialization is needed, explicitly delegate using:

``` python
super().__init__(...)
```

------------------------------------------------------------------------

## 17. What is `super()`?

Accurate interview answer:

> `super()` returns a proxy that delegates attribute/method lookup
> according to the MRO, starting after the current class.

For simple inheritance, this often looks like calling the parent
implementation, but "super means parent" is incomplete.

------------------------------------------------------------------------

## 18. Why not just call the parent directly?

You could write:

``` python
Animal.__init__(self, name, food)
```

But cooperative inheritance is better served by:

``` python
super().__init__(name, food)
```

because `super()` participates in the MRO and works correctly with
cooperative multiple inheritance.

------------------------------------------------------------------------

## 19. What is method overriding?

When a child defines a method with the same name as one inherited from
the parent.

``` python
class Animal:
    def eat(self):
        print("Animal")


class Dog(Animal):
    def eat(self):
        print("Dog")
```

For a Dog instance, Dog's implementation is found first.

------------------------------------------------------------------------

## 20. What is MRO?

MRO means **Method Resolution Order**.

It is the order Python follows when resolving attributes/methods through
inheritance.

Example:

``` python
class A:
    pass

class B(A):
    pass

class C(B):
    pass
```

Conceptually:

``` text
C -> B -> A -> object
```

Inspect it with:

``` python
C.mro()
```

------------------------------------------------------------------------

## 21. Why is MRO important with multiple inheritance?

Consider:

``` text
    A
   / \
  B   C
   \ /
    D
```

There are multiple paths to A.

Python needs one deterministic lookup order.

MRO provides that order.

------------------------------------------------------------------------

## 22. What is the Diamond Problem?

A diamond occurs when two parent classes share a common ancestor:

``` text
       A
      / \
     B   C
      \ /
       D
```

Python's MRO resolves the lookup order so shared ancestors are handled
consistently.

For:

``` python
class D(B, C):
    pass
```

the simple conceptual MRO is:

``` text
D -> B -> C -> A -> object
```

------------------------------------------------------------------------

## 23. Why doesn't `super()` simply go to the parent?

Because with multiple inheritance, `super()` follows the MRO.

If:

``` text
D -> B -> C -> A -> object
```

then inside B:

``` python
super().show()
```

continues after B:

``` text
C -> A -> object
```

So it can call C rather than directly calling B's declared base A.

------------------------------------------------------------------------

## 24. What is polymorphism?

Polymorphism means different objects can respond to the same operation
with different behavior.

``` python
dog.speak()
cat.speak()
```

Both use the same conceptual interface:

``` text
speak()
```

but produce different behavior.

------------------------------------------------------------------------

## 25. Does polymorphism require inheritance?

No.

Python supports polymorphic behavior through duck typing even between
unrelated classes.

------------------------------------------------------------------------

## 26. What is duck typing?

Duck typing focuses on capabilities rather than explicit type
relationships.

If code does:

``` python
def make_sound(obj):
    obj.speak()
```

then the important requirement is that `obj` supports `speak()`.

An object doesn't have to inherit from a specific class.

------------------------------------------------------------------------

## 27. Why does this work?

``` python
class Dog:
    def speak(self):
        print("Woof")


class Robot:
    def speak(self):
        print("Beep")


def make_sound(obj):
    obj.speak()
```

Because both objects provide the behavior required by `make_sound()`:

``` text
Dog    -> speak()
Robot  -> speak()
```

------------------------------------------------------------------------

## 28. Why does this fail?

``` python
class Robot:
    def beep(self):
        print("Beep")
```

Then:

``` python
make_sound(Robot())
```

fails because `make_sound()` calls:

``` python
obj.speak()
```

but Robot only provides:

``` python
beep()
```

The likely exception is:

``` text
AttributeError
```

------------------------------------------------------------------------

# Strong interview answer: self vs cls vs static

> An instance method receives the current instance as `self` and is
> appropriate when the operation needs instance state. A class method
> receives the class as `cls` and is appropriate for class-level state
> or class-oriented operations. A static method receives neither
> automatically and is appropriate for a utility operation logically
> associated with the class but independent of instance and class state.

------------------------------------------------------------------------

# Strong interview answer: inheritance + super

> In inheritance, a child can reuse and specialize parent behavior. If
> the child defines its own `__init__`, the child's initializer is used,
> so parent initialization must be explicitly delegated when needed.
> `super()` is preferable to hard-coding the parent class because it
> follows the MRO and supports cooperative multiple inheritance.

------------------------------------------------------------------------

# Strong interview answer: MRO + super

> MRO is Python's method resolution order: the ordered sequence used to
> resolve attributes and methods across an inheritance hierarchy.
> `super()` does not simply mean "call my parent"; it continues lookup
> from the current class according to the MRO. This becomes especially
> important in multiple inheritance and the Diamond Problem.

------------------------------------------------------------------------

# Strong interview answer: polymorphism + duck typing

> Polymorphism allows different objects to respond to the same operation
> differently. Python's duck typing allows this without requiring
> explicit inheritance: code can rely on the behavior an object provides
> rather than its concrete type. If an object supports the required
> method, it can participate.

------------------------------------------------------------------------

# Interview traps to avoid

## Trap 1

Wrong:

> "`self` is a keyword."

Better:

> "`self` is the conventional name for the current instance parameter."

## Trap 2

Wrong:

> "`super()` always means parent."

Better:

> "`super()` continues lookup according to the MRO."

## Trap 3

Wrong:

> "Class variables are copied into every instance."

Better:

> "Instance lookup can fall back to the class when the instance doesn't
> have that attribute."

## Trap 4

Wrong:

> "Static methods are used because they're faster."

Better:

> "Static methods are appropriate when the operation needs neither
> instance nor class state."

## Trap 5

Wrong:

> "Polymorphism always requires inheritance."

Better:

> "Python supports polymorphism through duck typing even without
> inheritance."

------------------------------------------------------------------------

# Final rapid-fire test

You should be able to answer these in one or two sentences:

``` text
Class?
Object?
self?
__init__?
Instance variable?
Class variable?
Attribute shadowing?
Instance method?
Class method?
Static method?
Inheritance?
IS-A?
Child __init__?
super()?
Method overriding?
MRO?
Multiple inheritance?
Diamond Problem?
Polymorphism?
Duck typing?
```

If you can answer those without looking at the notes, today's OOP
foundation is solid.
