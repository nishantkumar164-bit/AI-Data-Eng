# Python Foundations - Day 3

## Functional Programming, Closures & Decorators

---

# 📌 Objective

Day 3 focuses on Python's functional programming capabilities and the concepts that power many popular frameworks like Flask, FastAPI, Airflow, Django, Pytest, LangChain, and many more.

Rather than memorizing syntax, the goal is to understand **how Python treats functions internally** and how decorators are built from first principles.

---

# 📚 Topics Covered

## 1. First-Class Functions

### Definition

In Python, functions are first-class objects.

This means functions can:

* Be assigned to variables
* Be passed as arguments
* Be returned from other functions
* Be stored inside collections

### Example

```python
def greet():
    return "Hello"

x = greet

print(x())
```

### Key Takeaways

* Function names are references.
* Multiple variables can point to the same function object.
* Functions behave like any other Python object.

---

## 2. Lambda Functions

### Definition

A lambda function is a small anonymous function used for short, one-time operations.

### Syntax

```python
lambda arguments: expression
```

### Example

```python
square = lambda x: x * x

print(square(5))
```

### When to Use

* Short transformations
* map()
* filter()
* sorted()
* Key functions

### Avoid

Do not use lambda for large business logic.

---

## 3. map()

### Purpose

Transforms every element of an iterable.

### Example

```python
numbers = [1,2,3]

result = map(lambda x: x*2, numbers)

print(list(result))
```

### Important

* map() is lazy.
* Returns an iterator.
* Executes only when consumed.

---

## 4. filter()

### Purpose

Selects only elements satisfying a condition.

### Example

```python
numbers = [5,10,15,20]

result = filter(lambda x: x>10, numbers)

print(list(result))
```

### Important

* Returns an iterator.
* Does not modify original data.

---

## 5. reduce()

### Purpose

Combines multiple values into one.

### Example

```python
from functools import reduce

numbers = [1,2,3,4]

result = reduce(lambda x,y: x+y, numbers)

print(result)
```

### Common Uses

* Sum
* Product
* Maximum
* Minimum
* Aggregations

---

## map vs filter vs reduce

| Function | Purpose        |
| -------- | -------------- |
| map()    | Transform data |
| filter() | Select data    |
| reduce() | Aggregate data |

---

# Flexible Function Arguments

---

## 6. *args

### Purpose

Accepts any number of positional arguments.

### Example

```python
def add(*args):
    return sum(args)
```

### Important

* Stored as a tuple.
* Useful when number of arguments is unknown.

---

## 7. **kwargs

### Purpose

Accepts any number of keyword arguments.

### Example

```python
def display(**kwargs):
    print(kwargs)
```

### Important

* Stored as a dictionary.
* Frequently used for configuration.

---

## 8. Packing & Unpacking

### Packing

```python
def demo(*args):
    pass
```

Arguments are packed into a tuple.

---

### Unpacking

```python
nums = [10,20,30]

add(*nums)
```

Elements are unpacked into separate arguments.

Dictionary unpacking:

```python
student = {"name":"Nishant","age":35}

display(**student)
```

---

# Closures

---

## 9. Closures

### Definition

A closure is an inner function that remembers and preserves variables from its enclosing function even after the enclosing function has finished execution.

### Example

```python
def outer():

    x = 10

    def inner():
        print(x)

    return inner

f = outer()

f()
```

### Why Closures Exist

Normally, local variables are removed after a function returns.

Closures preserve only the variables still required by the returned inner function.

### Common Uses

* Decorators
* State preservation
* Counters
* Function factories

---

# Decorators

---

## 10. Decorators

### Purpose

A decorator adds additional functionality to an existing function without modifying the original function.

### Basic Structure

```python
def decorator(func):

    def wrapper(*args, **kwargs):

        return func(*args, **kwargs)

    return wrapper
```

### Internal Working

```python
@logger
def greet():
    pass
```

Python internally performs:

```python
greet = logger(greet)
```

---

## 11. functools.wraps

### Problem

Without wraps, metadata is lost.

```python
greet.__name__
```

becomes

```
wrapper
```

### Solution

```python
from functools import wraps

@wraps(func)
```

### Benefit

Preserves:

* Function name
* Docstring
* Metadata

---

## 12. Parameterized Decorators

### Purpose

Pass configuration to decorators.

Example

```python
@logger("INFO")
```

Internal Flow

```text
logger("INFO")
        ↓
returns decorator
        ↓
decorator(greet)
        ↓
returns wrapper
        ↓
greet = wrapper
```

### Structure

```python
def logger(level):

    def decorator(func):

        def wrapper(*args, **kwargs):

            return func(*args, **kwargs)

        return wrapper

    return decorator
```

---

## 13. Stacked Decorators

Multiple decorators can be applied to the same function.

Example

```python
@logger
@timer
def greet():
    pass
```

Python converts it into:

```python
greet = timer(greet)
greet = logger(greet)
```

Execution Flow

```text
greet()
    ↓
Logger Wrapper
    ↓
Timer Wrapper
    ↓
Original Function
    ↓
Timer Ends
    ↓
Logger Ends
```

---

# Real-World Applications

* Flask (`@app.route`)
* FastAPI (`@app.get`)
* Airflow (`@task`, `@dag`)
* Django
* Pytest
* Authentication
* Authorization
* Logging
* Performance Monitoring
* Retry Logic
* Caching

---

# Best Practices

* Keep decorators focused on a single responsibility.
* Use `functools.wraps` for production decorators.
* Prefer normal functions over lambda for complex logic.
* Use `map()` and `filter()` only when they improve readability.
* Avoid deeply nested decorators unless required.
* Write decorators that support both `*args` and `**kwargs`.

---

# Common Interview Questions

1. What are first-class functions?
2. Difference between lambda and normal functions?
3. Why is map() lazy?
4. Difference between map(), filter(), and reduce()?
5. Explain packing and unpacking.
6. What is a closure?
7. Why do decorators require closures?
8. What does `functools.wraps` do?
9. Explain parameterized decorators.
10. Explain stacked decorators.
11. Difference between parameterized and stacked decorators.
12. How does Python execute decorators internally?

---

# Key Learning Outcomes

By the end of Day 3, I can:

* Explain first-class functions.
* Use lambda effectively.
* Apply map(), filter(), and reduce().
* Work with `*args` and `**kwargs`.
* Understand packing and unpacking.
* Explain closures and state preservation.
* Build decorators from scratch.
* Preserve metadata using `functools.wraps`.
* Create parameterized decorators.
* Understand the execution order of stacked decorators.
* Recognize decorators used by production frameworks.

---

## 🚀 Next Topic

**Day 4 – Object-Oriented Programming (OOP)**

Topics include:

* Classes & Objects
* self
* **init**
* Instance vs Class Variables
* Instance Methods
* @staticmethod
* @classmethod
* Inheritance
* Polymorphism
* Encapsulation
* Abstraction
* Dunder Methods
* Properties
* Composition vs Inheritance
* SOLID Principles
