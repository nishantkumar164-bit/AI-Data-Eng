"""
Day 01
Python References and Mutability
"""


# --------------------------------------------------
# Example 1: Shared List Reference
# --------------------------------------------------

a = [1, 2, 3]
b = a

b.append(4)

print("Example 1")
print("a:", a)
print("b:", b)


# --------------------------------------------------
# Example 2: Immutable String
# --------------------------------------------------

c = "hello"
d = c

d = d + " world"

print("\nExample 2")
print("c:", c)
print("d:", d)


# --------------------------------------------------
# Example 3: Mutation vs Reassignment
# --------------------------------------------------

numbers = [1, 2, 3]

numbers.append(4)

print("\nAfter mutation:")
print(numbers)

numbers = [10, 20]

print("After reassignment:")
print(numbers)


# --------------------------------------------------
# Example 4: Mutable Default Argument
# --------------------------------------------------

def add_item(item, items=[]):
    items.append(item)
    return items


print("\nMutable Default Argument")

print(add_item("new"))
print(add_item("new"))
print(add_item("new"))


# --------------------------------------------------
# Example 5: Correct Default Argument
# --------------------------------------------------

def add_item_safe(item, items=None):
    if items is None:
        items = []

    items.append(item)

    return items


print("\nSafe Default Argument")

print(add_item_safe("new"))
print(add_item_safe("new"))
print(add_item_safe("new"))