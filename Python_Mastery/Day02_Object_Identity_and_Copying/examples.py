"""
Day 02
Object Identity and Copying
"""

import copy


# --------------------------------------------------
# Example 1: Object Identity
# --------------------------------------------------

a = [1, 2, 3]
b = a

print("Object Identity")

print(id(a))
print(id(b))

print("Same object:", a is b)


# --------------------------------------------------
# Example 2: Equality vs Identity
# --------------------------------------------------

a = [1, 2, 3]
b = [1, 2, 3]

print("\nEquality vs Identity")

print("a == b:", a == b)
print("a is b:", a is b)


# --------------------------------------------------
# Example 3: Shallow Copy
# --------------------------------------------------

a = [[1, 2], [3, 4]]

b = copy.copy(a)

b[0].append(99)

print("\nShallow Copy")

print("a:", a)
print("b:", b)


# --------------------------------------------------
# Example 4: Deep Copy
# --------------------------------------------------

a = [[1, 2], [3, 4]]

b = copy.deepcopy(a)

b[0].append(99)

print("\nDeep Copy")

print("a:", a)
print("b:", b)


# --------------------------------------------------
# Example 5: Nested Dictionary
# --------------------------------------------------

api_record = {
    "user_id": 101,
    "metadata": {
        "source": "mobile",
        "status": "raw"
    }
}

processed_record = api_record.copy()

processed_record["metadata"]["status"] = "processed"

print("\nNested Dictionary Shallow Copy")

print("Original:", api_record)
print("Processed:", processed_record)