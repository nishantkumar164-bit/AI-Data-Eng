# Python Foundations - Day 3

# Assignments

---

# First-Class Functions

* Assign a function to another variable.
* Store functions inside a list and execute them.
* Return a function from another function.

---

# Lambda

* Square a number.
* Cube every element of a list.
* Sort students by age using lambda.

---

# map()

* Convert Celsius to Fahrenheit.
* Double every number.
* Convert names to uppercase.

---

# filter()

* Find even numbers.
* Filter employees earning more than 50,000.
* Remove empty strings from a list.

---

# reduce()

* Find sum.
* Find product.
* Find maximum.
* Find minimum.

---

# *args

* Create your own sum function.
* Find maximum using *args.
* Calculate average.

---

# **kwargs

* Print employee details.
* Accept unlimited configuration values.
* Build a profile generator.

---

# Packing & Unpacking

* Pass list using *.
* Pass dictionary using **.
* Practice both together.

---

# Closures

* Build a counter.
* Build a multiplier factory.
* Build a greeting factory.

---

# Decorators

Create decorators for:

* Logging
* Execution Time
* Authentication
* Retry

---

# functools.wraps

Create a decorator.

Observe

```
function.__name__
```

before and after using wraps.

---

# Parameterized Decorators

Create

```python
@logger("INFO")
```

Create

```python
@logger("ERROR")
```

Observe the output.

---

# Stacked Decorators

Combine

* Logger
* Timer
* Authentication

Observe execution order.

---

# Challenge Questions

1. Why are decorators implemented using closures?

2. Why does wrapper need *args and **kwargs?

3. Difference between parameterized decorators and stacked decorators?

4. Why is map() lazy?

5. Explain packing vs unpacking with examples.

6. Why do frameworks heavily use decorators?

7. Explain decorator execution flow without using @ syntax.

8. How would you implement your own logger decorator?

---

# Mini Project

Build a small Employee Management System.

Requirements:

* Use decorators for logging.
* Use parameterized decorators for log levels.
* Use stacked decorators for authentication and logging.
* Use closures wherever appropriate.
* Use functools.wraps.
