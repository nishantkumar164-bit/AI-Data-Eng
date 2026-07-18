"""
Day 03 Assignments

Predict output first.

Do NOT execute immediately.

Explain:

1. Prediction

2. Reason

3. Object Graph

4. Engineering Connection
"""

# ------------------------------
# Assignment 1
# ------------------------------

def modify(data):
    data.append(5)

a = [1, 2]

modify(a)

print(a)

# ------------------------------
# Assignment 2
# ------------------------------

def modify(data):
    data = [10]

a = [1, 2]

modify(a)

print(a)

# ------------------------------
# Assignment 3
# ------------------------------

a = [[1], [2]]

def modify(data):
    data[1].append(99)

modify(a)

print(a)

# ------------------------------
# Assignment 4
# ------------------------------

a = [[1], [2]]

def modify(data):
    data[1] = [100]

modify(a)

print(a)

# ------------------------------
# Assignment 5
# ------------------------------

x = 100

def test():
    print(x)

test()

# ------------------------------
# Assignment 6
# ------------------------------

x = 100

def test():
    print(x)
    x = 50

test()

# ------------------------------
# Assignment 7
# ------------------------------

x = 100

def outer():

    x = 50

    def inner():
        print(x)

    inner()

outer()

# ------------------------------
# Assignment 8
# ------------------------------

x = 100

def outer():

    x = 50

    def inner():
        nonlocal x
        x = 25

    inner()

    print(x)

outer()

print(x)

# ------------------------------
# Assignment 9
# ------------------------------

"""
Architecture Question

Which design would you choose?

Approach A

cache = {}

def process():
    global cache

OR

Approach B

def process(cache):

Explain:

State Ownership

Lifetime

Testing

Debugging

Dependency Visibility

"""

# ------------------------------
# Assignment 10
# ------------------------------

"""
Hotel Analogy

S3 Client

failed_records

Explain

Which stays in room?

Which becomes new paper every guest?

Why?
"""

# ------------------------------
# Bonus
# ------------------------------

def hello():
    return "Hello"

a = hello

b = hello()

print(type(a))
print(type(b))