# Python OOP — SOLID Interview Questions

## Basic

### 1. What does SOLID stand for?

S — Single Responsibility Principle  
O — Open/Closed Principle  
L — Liskov Substitution Principle  
I — Interface Segregation Principle  
D — Dependency Inversion Principle

SOLID is a group of object-oriented design principles intended to improve maintainability, extensibility, testability, and flexibility.

### 2. Is SOLID a programming language feature?

No. SOLID is a set of software design principles that guides how classes, responsibilities, abstractions, and dependencies are organized.

### 3. Explain SRP.

A class should have one responsibility or, more precisely, one primary reason to change.

It does not mean one method per class.

### 4. What does "reason to change" mean?

If different requirements can independently cause different parts of a class to change, the class may contain multiple responsibilities.

### 5. Explain OCP.

Software entities should be open for extension but closed for modification.

The goal is to add new behavior without repeatedly changing stable existing code.

### 6. How does polymorphism help OCP?

Instead of checking concrete types with if/elif, code can call a common behavior:

```python
def process(payment):
    payment.pay()
```

New implementations can be added without changing the caller.

### 7. Does OCP mean existing code can never be modified?

No. It means areas likely to vary should be designed so new behavior can generally be added through extension rather than repeated modification of stable code.

### 8. What is LSP?

A child/subtype should be usable wherever its parent abstraction is expected without breaking the expected behavior.

### 9. Is method overriding an LSP violation?

No. Overriding is normal polymorphism.

It becomes an LSP problem when the child violates the behavioral contract or expectations of the parent.

### 10. How can LSP violations be prevented?

Design parent abstractions around behavior that every valid subtype can support. Sometimes this means splitting a broad abstraction.

### 11. Explain ISP.

Clients should not be forced to depend on methods they do not use.

Prefer small, focused interfaces over large interfaces containing unrelated capabilities.

### 12. Give an ISP violation.

```python
class Worker:
    def work(self): pass
    def drive(self): pass
    def cook(self): pass
    def manage_team(self): pass
```

A developer may need `work()` but not `drive()` or `cook()`.

### 13. How would you fix an ISP violation?

Split the interface into capabilities such as:

```text
Workable
Drivable
Cookable
TeamManager
```

Classes implement only what they need.

### 14. What is DIP?

High-level modules should not directly depend on low-level implementation details. Both should depend on abstractions.

### 15. What is Dependency Injection?

Dependency Injection is a technique where dependencies are supplied to a class from outside instead of the class creating them itself.

```python
class OrderService:
    def __init__(self, repository):
        self.repository = repository
```

### 16. Is DIP the same as Dependency Injection?

No.

DIP is a design principle.

Dependency Injection is a technique commonly used to implement DIP.

### 17. Why does DIP improve testing?

Dependencies can be replaced with fake or mock implementations:

```python
service = OrderService(FakeRepository())
```

This allows business logic to be tested without a real database.

---

# Comparison Questions

### 18. SRP vs OCP?

SRP asks:

> Is the class responsible for too many unrelated things?

OCP asks:

> Can new behavior be added without repeatedly modifying stable existing code?

### 19. LSP vs ISP?

LSP focuses on subtype behavior and substitution:

> Can a subtype honor the parent's contract?

ISP focuses on interfaces:

> Is a class being forced to depend on methods it does not need?

### 20. DIP vs Dependency Injection?

DIP = principle.

DI = implementation technique.

### 21. Which principles connect strongly with polymorphism?

OCP commonly uses polymorphism to add new implementations.

LSP is also directly related to polymorphism because it defines how valid subtypes should behave when substituted for their parent abstraction.

---

# Scenario-Based Questions

### 22. A class has 20 methods. Is that automatically an SRP violation?

No.

The number of methods is not the deciding factor. Ask whether the methods represent one cohesive responsibility and share a common reason to change.

### 23. A large if/elif chain handles different payment types. Which principle might be violated?

OCP is a likely concern because each new payment type requires modifying existing decision logic.

### 24. A child class raises NotImplementedError for an inherited method. Which principle should you investigate?

LSP.

The child may not actually be a valid substitute for the parent abstraction.

ISP may also be relevant if the parent interface is unnecessarily broad.

### 25. A class directly creates MySQLDatabase, EmailService, and StripePayment objects. Which principle should you investigate?

DIP.

The high-level class is tightly coupled to concrete implementations.

### 26. A class is forced to implement ten methods although it only uses three. Which principle might be relevant?

ISP.

The interface may be too large.

---

# Strong Interview Answer

If asked "What is SOLID?", a concise answer is:

> SOLID is a set of object-oriented design principles that help make software easier to maintain, extend, test, and change. SRP focuses on cohesive responsibilities, OCP on extension without repeatedly modifying stable code, LSP on safe substitution of subtypes, ISP on focused interfaces, and DIP on depending on abstractions rather than concrete implementation details.

---

# Practical Interview Checklist

When reviewing code:

```text
1. Responsibility
   ↓
   SRP

2. New variations
   ↓
   OCP

3. Inheritance behavior
   ↓
   LSP

4. Interface size
   ↓
   ISP

5. Concrete dependencies
   ↓
   DIP
```
