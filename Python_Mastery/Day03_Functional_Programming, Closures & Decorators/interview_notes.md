# Python Foundations - Day 3

# Interview Notes

## First-Class Functions

### Q1. What are first-class functions?

Functions in Python are treated as objects. They can be assigned to variables, passed as arguments, returned from other functions, and stored in collections.

---

## Lambda

### Q2. Difference between lambda and normal function?

| Lambda                | Normal Function     |
| --------------------- | ------------------- |
| Anonymous             | Named               |
| Single expression     | Multiple statements |
| Used once             | Reusable            |
| Small transformations | Business logic      |

---

## map()

### Q3. Why is map() lazy?

map() returns an iterator instead of immediately producing results.

Execution happens only when consumed.

---

## filter()

### Q4. Difference between map() and filter()?

map transforms data.

filter selects data.

---

## reduce()

### Q5. What does reduce() do?

It repeatedly combines values into a single result using an accumulator.

---

## *args

### Q6. Why use *args?

Allows functions to accept any number of positional arguments.

Internally stored as a tuple.

---

## **kwargs

### Q7. Why use **kwargs?

Allows functions to accept any number of keyword arguments.

Internally stored as a dictionary.

---

## Packing vs Unpacking

### Q8. Difference?

Packing collects arguments.

Unpacking expands iterables into arguments.

---

## Closures

### Q9. What is a closure?

A closure is an inner function that remembers variables from its enclosing function even after the outer function has returned.

---

## Decorators

### Q10. What is a decorator?

A decorator adds extra functionality to an existing function without modifying its source code.

---

### Q11. How does @ work internally?

```python
@logger
def greet():
```

becomes

```python
greet = logger(greet)
```

---

## functools.wraps

### Q12. Why use wraps?

Preserves function metadata.

Without wraps

```python
greet.__name__
```

returns

```
wrapper
```

---

## Parameterized Decorators

### Q13. Why another function?

Because configuration must be processed before the decorator receives the function.

---

## Stacked Decorators

### Q14. Order of execution?

Bottom decorator wraps first.

Top decorator executes first.

---

## Common Production Uses

* Authentication
* Authorization
* Logging
* Retry
* Caching
* Timing
* Monitoring
* API Routing

---

## Common Mistakes

❌ Forgetting to return wrapper

❌ Forgetting *args and **kwargs

❌ Not using functools.wraps

❌ Writing huge decorators instead of small reusable ones
