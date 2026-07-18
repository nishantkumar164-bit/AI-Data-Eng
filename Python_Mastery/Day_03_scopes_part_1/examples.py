

"""
Day 03 Examples part 1
"""

# ----------------------------------
# Example 1
# Mutation
# ----------------------------------

def modify(data):
    data.append(4)

a = [1, 2, 3]

modify(a)

print(a)

# ----------------------------------
# Example 2
# Reassignment
# ----------------------------------

def modify(data):
    data = [10]

a = [1, 2]

modify(a)

print(a)

# ----------------------------------
# Example 3
# Local Scope
# ----------------------------------

x = 10

def test():
    x = 20
    print(x)

test()
print(x)

# ----------------------------------
# Example 4
# Global
# ----------------------------------

x = 10

def test():
    global x
    x = 30

test()

print(x)

# ----------------------------------
# Example 5
# Nonlocal
# ----------------------------------

def outer():

    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()

    print(x)

outer()

# ----------------------------------
# Example 6
# Nested Mutable Object
# ----------------------------------

a = [[1], [2]]

def modify(data):

    data[0].append(99)

modify(a)

print(a)

# ----------------------------------
# Example 7
# Function Object
# ----------------------------------

def hello():
    print("Hello")

a = hello

print(a)

a()

# ----------------------------------
# Example 8
# Returning Function
# ----------------------------------

def outer():

    def inner():
        print("Inside Inner")

    return inner

func = outer()

func()