"""
Python OOP — Day 4 Examples
Runnable examples for all topics covered today.
"""

# ============================================================
# 1. CLASS, OBJECT, self, __init__, INSTANCE VARIABLES
# ============================================================

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary)


e1 = Employee("Rahul", 50000)
e2 = Employee("Amit", 70000)

e1.display()
e2.display()


# ============================================================
# 2. CLASS VARIABLE + ATTRIBUTE LOOKUP + SHADOWING
# ============================================================

class CompanyEmployee:
    company = "ABC"

    def __init__(self, name):
        self.name = name


a1 = CompanyEmployee("Amit")
a2 = CompanyEmployee("Neha")

print(a1.company)       # ABC
print(a2.company)       # ABC
print(CompanyEmployee.company)  # ABC

# Creates an instance attribute; does NOT modify the class variable.
a1.company = "XYZ"

print(a1.company)       # XYZ
print(a2.company)       # ABC
print(CompanyEmployee.company)  # ABC

# Change the actual class variable.
CompanyEmployee.company = "PQR"

print(a1.company)       # XYZ (shadowing instance attribute)
print(a2.company)       # PQR
print(CompanyEmployee.company)  # PQR


# ============================================================
# 3. INSTANCE METHOD / CLASS METHOD / STATIC METHOD
# ============================================================

class EmployeeMethods:
    company = "ABC"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Instance method: needs object-specific state.
    def increase_salary(self, amount):
        self.salary += amount

    # Class method: works with class-level state.
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    # Static method: needs neither instance nor class state.
    @staticmethod
    def is_valid_salary(salary):
        return salary > 0


emp = EmployeeMethods("Amit", 50000)
emp.increase_salary(5000)
print(emp.salary)  # 55000

EmployeeMethods.change_company("XYZ")
print(emp.company)  # XYZ

print(EmployeeMethods.is_valid_salary(50000))  # True
print(EmployeeMethods.is_valid_salary(-100))   # False


# ============================================================
# 4. INHERITANCE
# ============================================================

class Animal:
    def __init__(self, name, food):
        self.name = name
        self.food = food

    def eat(self):
        print(f"I am {self.name} and I eat {self.food}")

    def sleep(self):
        print("I am sleeping ZZZ")


class SimpleDog(Animal):
    def bark(self):
        print("Woof!")


dog = SimpleDog("Dexter", "Chicken")
dog.eat()     # inherited
dog.sleep()   # inherited
dog.bark()    # Dog's own method


# ============================================================
# 5. CHILD __init__ + super()
# ============================================================

class Dog(Animal):
    def __init__(self, name, breed, food):
        self.breed = breed
        super().__init__(name, food)

    def bark(self):
        print("I am barking!")

    def change_food(self, food):
        self.food = food


dog = Dog("Dexter", "Labrador", "Chicken")

print(dog.name)       # Dexter
print(dog.food)       # Chicken
print(dog.breed)      # Labrador

dog.eat()
dog.bark()

dog.change_food("Egg")
dog.eat()


# ============================================================
# 6. METHOD OVERRIDING
# ============================================================

class AnimalOverride:
    def eat(self):
        print("Animal is eating")


class DogOverride(AnimalOverride):
    def eat(self):
        print("Dog is eating bones")


animal = AnimalOverride()
dog = DogOverride()

animal.eat()  # Animal is eating
dog.eat()     # Dog is eating bones


# ============================================================
# 7. OVERRIDING + super()
# ============================================================

class AnimalWithSuper:
    def eat(self):
        print("Animal eating")


class DogWithSuper(AnimalWithSuper):
    def eat(self):
        print("Dog eating")
        super().eat()


DogWithSuper().eat()
# Dog eating
# Animal eating


# ============================================================
# 8. MRO — SIMPLE INHERITANCE
# ============================================================

class A:
    def show(self):
        print("A")


class B(A):
    pass


class C(B):
    pass


print(C.mro())
# Conceptually: C -> B -> A -> object


# ============================================================
# 9. MULTIPLE INHERITANCE
# ============================================================

class First:
    def show(self):
        print("First")


class Second:
    def show(self):
        print("Second")


class Third(First, Second):
    pass


third = Third()
third.show()

print(Third.mro())
# Conceptually: Third -> First -> Second -> object


# ============================================================
# 10. DIAMOND PROBLEM + COOPERATIVE super()
# ============================================================

class A_Diamond:
    def show(self):
        print("A")


class B_Diamond(A_Diamond):
    def show(self):
        print("B")
        super().show()


class C_Diamond(A_Diamond):
    def show(self):
        print("C")
        super().show()


class D_Diamond(B_Diamond, C_Diamond):
    pass


d = D_Diamond()
d.show()

print(D_Diamond.mro())
# Conceptually:
# D_Diamond -> B_Diamond -> C_Diamond -> A_Diamond -> object


# ============================================================
# 11. DIAMOND WITH D.show()
# ============================================================

class A2:
    def show(self):
        print("A")


class B2(A2):
    def show(self):
        print("B")
        super().show()


class C2(A2):
    def show(self):
        print("C")
        super().show()


class D2(B2, C2):
    def show(self):
        print("D")
        super().show()


D2().show()
# D
# B
# C
# A


# ============================================================
# 12. POLYMORPHISM
# ============================================================

class DogSound:
    def speak(self):
        print("Woof")


class CatSound:
    def speak(self):
        print("Meow")


def make_sound(obj):
    obj.speak()


make_sound(DogSound())
make_sound(CatSound())


# ============================================================
# 13. DUCK TYPING — UNRELATED CLASS
# ============================================================

class Robot:
    def speak(self):
        print("Beep")


make_sound(Robot())
# Robot does not inherit from DogSound or CatSound.
# It works because it provides the expected speak() behavior.


# ============================================================
# 14. DUCK TYPING FAILURE
# ============================================================

class BrokenRobot:
    def beep(self):
        print("Beep")


# The following would raise AttributeError:
#
# make_sound(BrokenRobot())
#
# Why?
# make_sound() requires obj.speak(), but BrokenRobot only has beep().
