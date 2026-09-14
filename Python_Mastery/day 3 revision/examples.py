# Python Day 3 — Examples

from functools import wraps


# ============================================================
# 1. Basic Closure
# ============================================================

def outer():
    x = 10

    def inner():
        return x

    return inner


func = outer()
print("Basic closure:", func())


# ============================================================
# 2. Closure Uses Current Enclosing Binding
# ============================================================

def outer_changed():
    x = 10

    def inner():
        return x

    x = 20
    return inner


func = outer_changed()
print("Changed enclosing value:", func())


# ============================================================
# 3. nonlocal
# ============================================================

def counter():
    i = 0

    def inner():
        nonlocal i
        i += 1
        return i

    return inner


c = counter()

print("Counter:", c())
print("Counter:", c())
print("Counter:", c())


# Independent closure state
c1 = counter()
c2 = counter()

print("c1:", c1())
print("c1:", c1())
print("c2:", c2())
print("c2:", c2())


# ============================================================
# 4. First-Class Functions
# ============================================================

def greet():
    print("Hello")


func = greet
func()


def execute(func):
    func()


execute(greet)


# ============================================================
# 5. Basic Decorator
# ============================================================

def decorator(func):

    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper


@decorator
def basic_greet():
    print("Hello")


basic_greet()


# Equivalent:
#
# def basic_greet():
#     print("Hello")
#
# basic_greet = decorator(basic_greet)


# ============================================================
# 6. functools.wraps
# ============================================================

def metadata_decorator(func):

    @wraps(func)
    def wrapper():
        func()

    return wrapper


@metadata_decorator
def documented_greet():
    """This is the original greet function."""
    print("Hello")


print("Name:", documented_greet.__name__)
print("Doc:", documented_greet.__doc__)


# ============================================================
# 7. Decorator With *args
# ============================================================

def logger_args(func):

    @wraps(func)
    def wrapper(*args):
        print(f"Function {func.__name__} is starting")

        result = func(*args)

        print(f"Function {func.__name__} is finished")

        return result

    return wrapper


@logger_args
def add(a, b):
    return a + b


print("add result:", add(10, 20))


# ============================================================
# 8. Decorator With *args and **kwargs
# ============================================================

def logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} is starting")

        result = func(*args, **kwargs)

        print(f"Function {func.__name__} is finished")

        return result

    return wrapper


@logger
def greet_person(name, age):
    return f"Hello {name}, age {age}"


print(greet_person("Nishant", age=35))


# ============================================================
# 9. Parameterized Decorator
# ============================================================

def repeat(n):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None

            for _ in range(n):
                result = func(*args, **kwargs)

            return result

        return wrapper

    return decorator


@repeat(3)
def say_hello():
    print("Hello")


say_hello()


# ============================================================
# 10. Parameterized Logger
# ============================================================

def parameterized_logger(level):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{level}] Function {func.__name__} is starting")

            result = func(*args, **kwargs)

            print(f"[{level}] Function {func.__name__} is finished")

            return result

        return wrapper

    return decorator


@parameterized_logger("DEBUG")
def multiply(a, b):
    return a * b


@parameterized_logger("INFO")
def hello(name):
    return f"Hello {name}"


print("multiply:", multiply(5, 4))
print("hello:", hello("Nishant"))


# ============================================================
# 11. Stacked Decorators
# ============================================================

def decorator1(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator 1")
        return func(*args, **kwargs)

    return wrapper


def decorator2(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator 2")
        return func(*args, **kwargs)

    return wrapper


@decorator1
@decorator2
def stacked_greet():
    print("Hello")


stacked_greet()

# Application:
# stacked_greet = decorator1(decorator2(stacked_greet))
#
# Execution:
# Decorator 1
# Decorator 2
# Hello


# ============================================================
# 12. Retry Decorator — Reference Example
# ============================================================

def retry(n):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(n):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == n - 1:
                        raise

        return wrapper

    return decorator


@retry(3)
def divide(a, b):
    return a / b


print("divide:", divide(10, 2))

# Uncomment to test three failed attempts:
# divide(10, 0)
