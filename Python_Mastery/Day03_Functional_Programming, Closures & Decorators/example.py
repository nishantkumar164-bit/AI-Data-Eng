"""
Python Foundations - Day 3
examples.py

Run this file section by section to understand each concept.
"""

from functools import reduce, wraps


# ============================================================
# 1. First-Class Functions
# ============================================================

print("\n========== First-Class Functions ==========")

def greet():
    return "Hello"

x = greet

print(greet())
print(x())
print(id(greet))
print(id(x))


# ============================================================
# 2. Lambda
# ============================================================

print("\n========== Lambda ==========")

square = lambda x: x * x

print(square(5))


# ============================================================
# 3. map()
# ============================================================

print("\n========== map() ==========")

numbers = [1, 2, 3, 4, 5]

result = map(lambda x: x * 10, numbers)

print(list(result))


# ============================================================
# 4. filter()
# ============================================================

print("\n========== filter() ==========")

numbers = [5, 10, 15, 20]

result = filter(lambda x: x > 10, numbers)

print(list(result))


# ============================================================
# 5. reduce()
# ============================================================

print("\n========== reduce() ==========")

numbers = [1, 2, 3, 4]

print(reduce(lambda x, y: x + y, numbers))

print(reduce(lambda x, y: x if x > y else y, numbers))


# ============================================================
# 6. *args
# ============================================================

print("\n========== *args ==========")

def add(*args):
    return sum(args)

print(add(10, 20))
print(add(10, 20, 30))
print(add(10, 20, 30, 40))


# ============================================================
# 7. **kwargs
# ============================================================

print("\n========== **kwargs ==========")

def student(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student(name="Nishant", age=35)


# ============================================================
# 8. Packing & Unpacking
# ============================================================

print("\n========== Packing / Unpacking ==========")

def multiply(a, b, c):
    print(a * b * c)

nums = [2, 3, 4]

multiply(*nums)

person = {
    "name": "Nishant",
    "age": 35
}

student(**person)


# ============================================================
# 9. Closures
# ============================================================

print("\n========== Closures ==========")

def outer():

    count = 0

    def inner():
        nonlocal count
        count += 1
        print(count)

    return inner

counter = outer()

counter()
counter()
counter()


# ============================================================
# 10. Basic Decorator
# ============================================================

print("\n========== Decorator ==========")

def logger(func):

    def wrapper():
        print("Before Function")
        func()
        print("After Function")

    return wrapper


@logger
def hello():
    print("Hello World")

hello()


# ============================================================
# 11. wraps
# ============================================================

print("\n========== functools.wraps ==========")

def logger(func):

    @wraps(func)
    def wrapper():
        func()

    return wrapper


@logger
def demo():
    """Sample Function"""
    print("Demo")

print(demo.__name__)
print(demo.__doc__)


# ============================================================
# 12. Parameterized Decorator
# ============================================================

print("\n========== Parameterized Decorator ==========")

def logger(level):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            print(f"[{level}] Executing {func.__name__}")

            return func(*args, **kwargs)

        return wrapper

    return decorator


@logger("INFO")
def greet_user(name):
    print("Hello", name)

greet_user("Nishant")


# ============================================================
# 13. Stacked Decorators
# ============================================================

print("\n========== Stacked Decorators ==========")

def A(func):

    @wraps(func)
    def wrapper():
        print("A Start")
        func()
        print("A End")

    return wrapper


def B(func):

    @wraps(func)
    def wrapper():
        print("B Start")
        func()
        print("B End")

    return wrapper


@A
@B
def test():
    print("Hello")

test()
