# Python Day 3 — Closures & Decorators Revision

## Topics Covered

1. Closures
2. `nonlocal`
3. First-class functions
4. Basic decorators
5. `functools.wraps`
6. Parameterized decorators
7. Stacked decorators
8. `*args` and `**kwargs` in decorators
9. Preserving return values
10. Nested closures in parameterized decorators

## 1. Closures

A closure is an inner function that retains access to variables from its enclosing scope even after the enclosing function has finished executing.

```python
def outer():
    x = 10

    def inner():
        return x

    return inner

func = outer()
print(func())  # 10
```

A closure retains access to the enclosing variable/binding rather than simply taking a snapshot of its value.

```python
def outer():
    x = 10

    def inner():
        return x

    x = 20
    return inner

func = outer()
print(func())  # 20
```

## 2. `nonlocal`

`nonlocal` is required when an inner function wants to rebind a variable belonging to an enclosing function scope.

Reading does not require `nonlocal`:

```python
def outer():
    x = 10

    def inner():
        print(x)

    return inner
```

Modifying/rebinding does:

```python
def outer():
    x = 10

    def inner():
        nonlocal x
        x += 1
        return x

    return inner
```

Important:
- `print(x)` → no `nonlocal`
- `x = 20` → `nonlocal` required if modifying enclosing `x`
- `x += 1` → `nonlocal` required
- Mutating an object such as `x.append(10)` does not rebind `x`

## 3. Closure With State

Closures can maintain state without global variables or a class.

```python
def counter():
    i = 0

    def inner():
        nonlocal i
        i += 1
        return i

    return inner

c = counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3
```

Each call to `counter()` creates independent state:

```python
c1 = counter()
c2 = counter()

print(c1())  # 1
print(c1())  # 2
print(c2())  # 1
print(c2())  # 2
```

## 4. First-Class Functions

Python functions are first-class objects. A function can be:
- assigned to a variable
- passed as an argument
- returned from another function
- stored inside collections

```python
def greet():
    print("Hello")

func = greet
func()
```

Important distinction:

```python
decorator(greet)    # pass function object
decorator(greet())  # execute greet first
```

## 5. Basic Decorators

A decorator accepts another function, adds/modifies behavior, and returns a function.

```python
def decorator(func):

    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper
```

Usage:

```python
@decorator
def greet():
    print("Hello")
```

This is effectively:

```python
def greet():
    print("Hello")

greet = decorator(greet)
```

The `wrapper` function closes over `func`.

```text
wrapper
   |
   └── closure → original greet
```

## 6. `functools.wraps`

Without `@wraps`, decorated metadata can appear to belong to the wrapper.

```python
def decorator(func):

    def wrapper():
        func()

    return wrapper
```

The decorated function may then have:

```python
greet.__name__  # "wrapper"
```

Use:

```python
from functools import wraps

def decorator(func):

    @wraps(func)
    def wrapper():
        func()

    return wrapper
```

Now important metadata such as the original name and docstring is preserved.

`wraps` does not change the execution flow; it preserves metadata on the wrapper.

## 7. Decorators With `*args` and `**kwargs`

A flexible decorator can support different function signatures:

```python
from functools import wraps

def logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} is starting")

        result = func(*args, **kwargs)

        print(f"Function {func.__name__} has finished")

        return result

    return wrapper
```

For:

```python
add(10, 20)
```

the wrapper receives:

```python
args = (10, 20)
kwargs = {}
```

For:

```python
greet("Nishant", age=35)
```

the wrapper receives:

```python
args = ("Nishant",)
kwargs = {"age": 35}
```

Then:

```python
func(*args, **kwargs)
```

reconstructs the original call.

## 8. Preserve Return Values

A common mistake:

```python
func(*args, **kwargs)
```

without returning the result.

Correct:

```python
result = func(*args, **kwargs)
return result
```

Otherwise the wrapper implicitly returns `None`.

## 9. Parameterized Decorators

A normal decorator:

```python
@decorator
def greet():
    ...
```

A parameterized decorator:

```python
@repeat(3)
def greet():
    ...
```

requires an additional layer:

```python
def repeat(n):

    def decorator(func):

        def wrapper():
            for i in range(n):
                func()

        return wrapper

    return decorator
```

Responsibilities:

- `repeat(n)` → receives configuration
- `decorator(func)` → receives the actual function
- `wrapper(...)` → executes enhanced behavior

The wrapper can access both `n` and `func` through closures.

## 10. Understanding Parameterized Decorator Syntax

This:

```python
@logger("DEBUG")
def add(a, b):
    return a + b
```

is equivalent to:

```python
add = logger("DEBUG")(add)
```

First call:

```python
logger("DEBUG")
```

captures the configuration and returns `decor`.

Second call:

```python
decor(add)
```

receives the original function and returns `wrapper`.

Final relationship:

```text
add → wrapper
       |
       ├── remembers func → original add
       └── remembers level → "DEBUG"
```

## 11. Stacked Decorators

```python
@decorator1
@decorator2
def greet():
    print("Hello")
```

is equivalent to:

```python
greet = decorator1(decorator2(greet))
```

The bottom decorator is applied first.

Application order:

```text
decorator2 → decorator1
```

Execution order:

```text
decorator1 → decorator2 → original function
```

Useful interview trick:

```python
@A
@B
def func():
    ...
```

mentally becomes:

```python
func = A(B(func))
```

## 12. Complete Parameterized Logger

```python
from functools import wraps

def logger(level):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{level}] Function {func.__name__} is starting")

            result = func(*args, **kwargs)

            print(f"[{level}] Function {func.__name__} is finished")

            return result

        return wrapper

    return decorator
```

This combines:
- closure
- parameterized decorator
- `*args`
- `**kwargs`
- `wraps`
- return-value preservation

## Key Interview Takeaways

### Closure
An inner function retaining access to variables from its enclosing scope even after the enclosing function has completed.

### `nonlocal`
Used when an inner function needs to rebind a variable from an enclosing function scope.

### Decorator
A function that accepts another function, enhances/modifies its behavior, and returns a function.

### `wraps`
Preserves important metadata of the original function on the wrapper.

### Parameterized decorator
Adds an outer function layer to capture configuration before receiving the decorated function.

### Stacked decorators

```python
@A
@B
def func():
    ...
```

means:

```python
func = A(B(func))
```

### Production decorator pattern

```python
@wraps(func)
def wrapper(*args, **kwargs):
    result = func(*args, **kwargs)
    return result
```
