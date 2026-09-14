# Python OOP — SOLID Principles

## Overview

SOLID is a set of object-oriented design principles that help make software easier to maintain, extend, test, understand, and change safely.

| Letter | Principle | Core Question |
|---|---|---|
| S | Single Responsibility Principle | Is this class doing too many unrelated things? |
| O | Open/Closed Principle | Can I add behavior without repeatedly modifying stable code? |
| L | Liskov Substitution Principle | Can child classes safely substitute their parent abstraction? |
| I | Interface Segregation Principle | Am I forcing classes to implement methods they don't need? |
| D | Dependency Inversion Principle | Is high-level code tightly coupled to concrete implementations? |

---

# S — Single Responsibility Principle

> A class should have one reason to change.

Think: **group related behavior into the appropriate class instead of stuffing unrelated responsibilities into one class.**

Bad:

```python
class Employee:
    def calculate_salary(self): pass
    def save_to_database(self): pass
    def send_email(self): pass
    def generate_report(self): pass
```

Better:

```python
class Employee:
    def calculate_salary(self): pass

class EmployeeRepository:
    def save(self, employee): pass

class EmailService:
    def send(self, employee, message): pass

class EmployeeReport:
    def generate(self, employee): pass
```

SRP does **not** mean one method per class. The methods should form one cohesive responsibility and have a common reason to change.

---

# O — Open/Closed Principle

> Software entities should be open for extension but closed for modification.

Bad:

```python
class PaymentProcessor:
    def process(self, payment_type, amount):
        if payment_type == "upi":
            print("UPI")
        elif payment_type == "card":
            print("Card")
        elif payment_type == "cash":
            print("Cash")
```

Every new payment type requires modification.

Better:

```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"UPI: {amount}")

class CardPayment(Payment):
    def pay(self, amount):
        print(f"Card: {amount}")

class PaymentProcessor:
    def process(self, payment, amount):
        payment.pay(amount)
```

A new `PayPalPayment` can be added without modifying `PaymentProcessor`.

OCP commonly works with polymorphism, inheritance, abstraction, and duck typing.

---

# L — Liskov Substitution Principle

> A child/subtype should be usable wherever the parent is expected without breaking expected behavior.

Bad:

```python
class Bird:
    def fly(self):
        print("Flying")

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins cannot fly")
```

If code expects a `Bird` to support `fly()`, substituting `Penguin` breaks the contract.

Better:

```python
class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        print("Flying")

class Sparrow(FlyingBird):
    pass

class Penguin(Bird):
    pass
```

The parent abstraction should only promise behavior that every valid subtype can support.

---

# I — Interface Segregation Principle

> Clients should not be forced to depend on methods they do not use.

Bad:

```python
class Worker(ABC):
    @abstractmethod
    def work(self): pass

    @abstractmethod
    def drive(self): pass

    @abstractmethod
    def cook(self): pass

    @abstractmethod
    def manage_team(self): pass
```

A developer may need `work()` but not `drive()` or `cook()`.

Better: create focused capabilities:

```python
class Workable(ABC):
    @abstractmethod
    def work(self): pass

class Drivable(ABC):
    @abstractmethod
    def drive(self): pass

class Cookable(ABC):
    @abstractmethod
    def cook(self): pass

class TeamManager(ABC):
    @abstractmethod
    def manage_team(self): pass
```

Then classes implement only what they need:

```python
class Developer(Workable):
    def work(self):
        print("Developer working")

class Driver(Workable, Drivable):
    def work(self):
        print("Driver working")

    def drive(self):
        print("Driving")
```

Think in terms of **capabilities/behaviors**, not one giant role-based interface.

---

# D — Dependency Inversion Principle

> High-level modules should not directly depend on low-level implementation details. Both should depend on abstractions.

Bad:

```python
class MySQLDatabase:
    def save(self, data):
        print("Saving to MySQL")

class CustomerService:
    def __init__(self):
        self.database = MySQLDatabase()
```

`CustomerService` is tightly coupled to MySQL.

Better:

```python
from abc import ABC, abstractmethod

class CustomerRepository(ABC):
    @abstractmethod
    def save(self, customer):
        pass

class MySQLRepository(CustomerRepository):
    def save(self, customer):
        print("Saving to MySQL")

class PostgreSQLRepository(CustomerRepository):
    def save(self, customer):
        print("Saving to PostgreSQL")

class CustomerService:
    def __init__(self, repository):
        self.repository = repository

    def save_customer(self, customer):
        self.repository.save(customer)
```

Usage:

```python
service = CustomerService(MySQLRepository())
```

or:

```python
service = CustomerService(PostgreSQLRepository())
```

## DIP vs Dependency Injection

- **DIP** = design principle.
- **Dependency Injection (DI)** = technique commonly used to implement DIP.

```python
class CustomerService:
    def __init__(self, repository):
        self.repository = repository
```

The dependency is supplied from outside.

---

# Complete SOLID Example — E-commerce

A good e-commerce architecture might contain:

```text
OrderService
    |
    +-- OrderCalculator
    +-- Discount
    +-- Payment
    +-- OrderRepository
    +-- Notification
```

Discount implementations:

```text
Discount
  ├── RegularDiscount
  ├── PremiumDiscount
  ├── VIPDiscount
  └── StudentDiscount
```

Payment implementations:

```text
Payment
  ├── UPIPayment
  ├── CardPayment
  └── PayPalPayment
```

Repository implementations:

```text
OrderRepository
  ├── MySQLRepository
  └── PostgreSQLRepository
```

Notification implementations:

```text
Notification
  ├── EmailNotification
  ├── WhatsAppNotification
  └── SMSNotification
```

This architecture demonstrates:

- **SRP:** responsibilities are separated.
- **OCP:** new implementations can be added without changing stable processing logic.
- **LSP:** implementations honor their abstractions.
- **ISP:** interfaces/capabilities stay focused.
- **DIP:** high-level order logic depends on abstractions and receives dependencies from outside.

---

# SOLID Mental Model

When reviewing code, ask:

```text
S → Is this class doing too many unrelated things?

O → Will adding a new variation require modifying
    existing stable code?

L → Can every child genuinely behave like its parent?

I → Am I forcing a class to implement methods it doesn't need?

D → Is important business logic tightly coupled to
    concrete implementation details?
```

## Connection to OOP

```text
Encapsulation
    ↓
Control access to internal state

Abstraction
    ↓
Expose essential behavior / hide implementation

Inheritance
    ↓
Create related types

Polymorphism
    ↓
Same interface, different implementations

SOLID
    ↓
Organize classes and their relationships
for maintainable application design
```

SOLID is not a replacement for OOP. It is a set of design principles applied on top of OOP.

---

# Final Revision Checklist

- [ ] Explain all five principles in your own words
- [ ] Identify SRP violations
- [ ] Identify OCP violations
- [ ] Use polymorphism for extensibility
- [ ] Explain duck typing vs ABC
- [ ] Identify LSP violations
- [ ] Recognize bad inheritance relationships
- [ ] Explain focused interfaces
- [ ] Identify ISP violations
- [ ] Explain DIP
- [ ] Explain Dependency Injection
- [ ] Distinguish DIP from DI
- [ ] Identify tight coupling
- [ ] Design a small system using multiple SOLID principles
