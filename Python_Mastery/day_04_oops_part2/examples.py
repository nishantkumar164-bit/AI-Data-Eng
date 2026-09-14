"""
Python OOP — Module 5
Examples

Run this file section by section while revising.
"""

from abc import ABC, abstractmethod


# ============================================================
# 1. CLASS, OBJECT, __init__, INSTANCE METHODS
# ============================================================

class Employee:
    company = "ABC Technologies"  # class attribute

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def introduce(self):
        return f"My name is {self.name} and my salary is {self.salary}"


employee1 = Employee("Rahul", 50000)
employee2 = Employee("Priya", 60000)

print(employee1.introduce())
print(employee2.introduce())


# ============================================================
# 2. CLASS METHOD
# ============================================================

class EmployeeWithClassMethod:
    company = "ABC"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, company_name):
        cls.company = company_name


EmployeeWithClassMethod.change_company("XYZ")
print(EmployeeWithClassMethod.company)


# Alternative constructor
class EmployeeFactory:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, data):
        name, salary = data.split(",")
        return cls(name, int(salary))


employee = EmployeeFactory.from_string("Nishant,75000")
print(employee.name, employee.salary)


# ============================================================
# 3. STATIC METHOD
# ============================================================

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_positive(number):
        return number > 0


print(Calculator.add(10, 20))
print(Calculator.is_positive(10))


# ============================================================
# 4. ENCAPSULATION
# ============================================================

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True

        return False

    def get_balance(self):
        return self._balance


account = BankAccount("Nishant", 5000)
account.deposit(2000)
account.withdraw(1000)
print(account.get_balance())

# Note:
# _balance is not a strict private attribute.
# This is still technically possible:
# account._balance = 999999


# ============================================================
# 5. ABSTRACTION
# ============================================================

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using credit card")


class UPIPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using UPI")


payments = [
    CreditCardPayment(),
    UPIPayment()
]

for payment in payments:
    payment.pay(1000)


# ============================================================
# 6. INHERITANCE
# ============================================================

class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def bark(self):
        print("Woof")


dog = Dog()
dog.eat()   # inherited behavior
dog.bark()  # own behavior


# ============================================================
# 7. METHOD OVERRIDING / POLYMORPHISM
# ============================================================

class AnimalBase:

    def speak(self):
        print("Some animal sound")


class DogAnimal(AnimalBase):

    def speak(self):
        print("Woof")


class CatAnimal(AnimalBase):

    def speak(self):
        print("Meow")


animals = [DogAnimal(), CatAnimal()]

for animal in animals:
    animal.speak()


# ============================================================
# 8. COMPOSITION
# ============================================================

class Engine:

    def start(self):
        print("Engine started")


class Car:

    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()
        print("Car started")


petrol_engine = Engine()
car = Car(petrol_engine)
car.start()


# ============================================================
# 9. __str__
# ============================================================

class EmployeeString:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.name} earns {self.salary} INR"


employee = EmployeeString("Rahul", 50000)
print(employee)


# ============================================================
# 10. __repr__
# ============================================================

class EmployeeRepresentation:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.name} earns {self.salary} INR"

    def __repr__(self):
        return f"EmployeeRepresentation({self.name!r}, {self.salary!r})"


employee = EmployeeRepresentation("Rahul", 50000)

print(employee)
print(repr(employee))
print([employee])


# ============================================================
# 11. __len__
# ============================================================

class Team:

    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)


team = Team(["Rahul", "Amit", "Priya"])
print(len(team))


# ============================================================
# 12. __eq__
# ============================================================

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented

        return self.name == other.name and self.price == other.price


p1 = Product("Laptop", 50000)
p2 = Product("Laptop", 50000)
p3 = Product("Mouse", 1000)

print(p1 == p2)  # True
print(p1 == p3)  # False


# ============================================================
# 13. __iter__
# ============================================================

class Playlist:

    def __init__(self, songs):
        self.songs = songs

    def __iter__(self):
        return iter(self.songs)


playlist = Playlist(["Song A", "Song B", "Song C"])

for song in playlist:
    print(song)


# ============================================================
# 14. __call__
# ============================================================

class Multiplier:

    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor


double = Multiplier(2)
triple = Multiplier(3)

print(double(10))
print(triple(10))


# ============================================================
# 15. PROPERTY / GETTER / SETTER
# ============================================================

class BankAccountProperty:

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        """Getter: controlled read access."""
        return self._balance

    @balance.setter
    def balance(self, amount):
        """Setter: controlled write access."""
        if amount >= 0:
            self._balance = amount
        else:
            raise ValueError("Balance cannot be negative")


account = BankAccountProperty("Nishant", 5000)

print(account.balance)  # getter

account.balance = 10000  # setter
print(account.balance)


# ============================================================
# 16. PROPERTY WITH A READ-ONLY ATTRIBUTE
# ============================================================

class Circle:

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return 3.14159 * self._radius ** 2


circle = Circle(5)

print(circle.radius)
print(circle.area)

# There is intentionally no area setter.
# circle.area = 100  # would raise AttributeError


# ============================================================
# 17. POLYMORPHISM + COMPOSITION
# ============================================================

class PetrolEngine:

    def start(self):
        print("Petrol engine started")


class ElectricEngine:

    def start(self):
        print("Electric engine started")


class FlexibleCar:

    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()


car1 = FlexibleCar(PetrolEngine())
car2 = FlexibleCar(ElectricEngine())

car1.start()
car2.start()


# ============================================================
# 18. COMBINED EXAMPLE
# ============================================================

class Order:

    def __init__(self, customer, amount):
        self.customer = customer
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value < 0:
            raise ValueError("Order amount cannot be negative")
        self._amount = value

    def __str__(self):
        return f"Order(customer={self.customer}, amount={self.amount})"

    def __repr__(self):
        return f"Order({self.customer!r}, {self.amount!r})"

    def __eq__(self, other):
        if not isinstance(other, Order):
            return NotImplemented
        return self.customer == other.customer and self.amount == other.amount


order1 = Order("Nishant", 2500)
order2 = Order("Nishant", 2500)

print(order1)
print(repr(order1))
print(order1 == order2)

order1.amount = 3000
print(order1)
