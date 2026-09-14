# Python Day 3 — Assignment

## Instructions

Solve these problems without looking at the solution first.

Focus on explaining:
- what each closure remembers
- which scope each variable comes from
- why `nonlocal` is or is not required
- what function object a decorated name points to
- how arguments and return values flow through wrappers

---

## Assignment 1 — Closure Counter

Create:

```python
def counter():
    ...
```

Expected:

```python
c = counter()

print(c())  # 1
print(c())  # 2
print(c())  # 3
```

Requirements:
- Use a closure.
- Use `nonlocal`.
- Do not use a global variable.

### Extension

Create two counters:

```python
c1 = counter()
c2 = counter()
```

Verify that their state is independent.

---

## Assignment 2 — Basic Decorator

Create a decorator called `logger`.

Expected:

```python
@logger
def greet():
    print("Hello")
```

Output:

```text
Function greet is starting
Hello
Function greet has finished
```

Requirements:
- nested `wrapper`
- call original function
- use `functools.wraps`

---

## Assignment 3 — Decorator With `*args`

Create a logger that works with:

```python
@logger
def add(a, b):
    return a + b
```

Expected:

```python
result = add(10, 20)
print(result)
```

Output should include the logging messages and:

```text
30
```

Requirements:
- use `*args`
- preserve the return value

---

## Assignment 4 — Decorator With `*args` and `**kwargs`

Make the decorator work with:

```python
@logger
def greet(name, age):
    return f"Hello {name}, age {age}"
```

Test:

```python
greet("Nishant", age=35)
```

The decorator must correctly forward both positional and keyword arguments.

---

## Assignment 5 — Parameterized Decorator

Create:

```python
@repeat(3)
def greet():
    print("Hello")
```

Expected:

```text
Hello
Hello
Hello
```

Requirements:
- `repeat(n)` receives configuration
- `decorator(func)` receives the function
- `wrapper()` performs repeated execution

Explain why three layers are required.

---

## Assignment 6 — Parameterized Logger

Create:

```python
@logger("DEBUG")
def add(a, b):
    return a + b
```

and:

```python
@logger("INFO")
def greet(name):
    return f"Hello {name}"
```

Expected style:

```text
[DEBUG] Calling add
[DEBUG] add finished
30
```

Requirements:
- parameterized decorator
- `*args`
- `**kwargs`
- `wraps`
- preserve return value

---

## Assignment 7 — Stacked Decorators

Create two decorators:

```python
@decorator1
@decorator2
def greet():
    print("Hello")
```

Predict the output before executing the code.

Then explain why:

```python
@decorator1
@decorator2
def greet():
    ...
```

is equivalent to:

```python
greet = decorator1(decorator2(greet))
```

---

## Assignment 8 — Final Challenge: Retry Decorator

Create:

```python
@retry(3)
def divide(a, b):
    return a / b
```

Requirements:
- attempt the function up to `n` times when an exception occurs
- accept arbitrary `*args` and `**kwargs`
- preserve metadata using `wraps`
- return the successful result
- after all attempts fail, allow the final exception to propagate

Test:

```python
divide(10, 2)
```

and:

```python
divide(10, 0)
```

Before coding, identify:
1. Where does `n` live?
2. Where does `func` live?
3. Where should `try/except` be placed?
4. What should `wrapper` return?
