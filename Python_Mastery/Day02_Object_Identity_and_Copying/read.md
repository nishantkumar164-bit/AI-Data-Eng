# Day 02 — Object Identity and Copying

## Topics Covered

* Object identity
* The `id()` function
* Equality vs identity
* `==` vs `is`
* Shallow copy
* Deep copy
* Nested mutable objects
* Python `copy` module
* Memory behavior

## Object Identity

Every Python object has an identity.

The `id()` function can be used to inspect an object's identity.

```python
a = [1, 2, 3]
b = a

print(id(a))
print(id(b))
```

Both values will be the same because `a` and `b` reference the same object.

## Equality vs Identity

Python provides two different comparisons.

### Equality

```python
==
```

Checks whether two objects contain equal values.

### Identity

```python
is
```

Checks whether two variables reference the same object.

Example:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
```

Output:

```text
True
False
```

The values are equal.

However, the lists are different objects.

## Shallow Copy

A shallow copy creates a new outer object.

Nested objects are still shared.

```python
import copy

a = [[1, 2], [3, 4]]

b = copy.copy(a)

b[0].append(99)

print(a)
print(b)
```

Output:

```text
[[1, 2, 99], [3, 4]]
[[1, 2, 99], [3, 4]]
```

The outer lists are different objects.

The nested lists are shared.

Conceptually:

```text
a ──► Outer List A
       │
       ├──► Nested List 1
       └──► Nested List 2

b ──► Outer List B
       │
       ├──► Nested List 1
       └──► Nested List 2
```

## Deep Copy

A deep copy recursively copies nested objects.

```python
import copy

a = [[1, 2], [3, 4]]

b = copy.deepcopy(a)

b[0].append(99)

print(a)
print(b)
```

Output:

```text
[[1, 2], [3, 4]]
[[1, 2, 99], [3, 4]]
```

The nested lists are no longer shared.

## Assignment vs Shallow Copy vs Deep Copy

### Assignment

```python
b = a
```

No copy is created.

Both variables reference the same object.

### Shallow Copy

```python
b = copy.copy(a)
```

A new outer object is created.

Nested objects remain shared.

### Deep Copy

```python
b = copy.deepcopy(a)
```

A completely independent nested object structure is created.

## Data Engineering Connection

Consider nested API data:

```python
api_record = {
    "user_id": 101,
    "metadata": {
        "source": "mobile",
        "status": "raw"
    }
}
```

A shallow copy:

```python
processed_record = api_record.copy()

processed_record["metadata"]["status"] = "processed"
```

The original object is also modified because the nested dictionary is shared.

For nested records, understanding shallow and deep copying is important when transforming API responses or Python objects before loading data into S3, Glue, or downstream processing systems.

## Performance Consideration

Deep copy is not automatically the best solution.

Deep copying a large object can increase:

* Memory usage
* CPU usage
* Processing time

In production systems, copy only when object isolation is actually required.

## Key Takeaways

* `id()` represents object identity.
* `==` compares values.
* `is` compares object identity.
* Assignment does not create a copy.
* Shallow copy creates a new outer object.
* Nested mutable objects remain shared in a shallow copy.
* Deep copy recursively copies nested objects.
* Deep copy has memory and performance costs.
