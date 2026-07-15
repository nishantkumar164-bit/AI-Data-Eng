# Day 01 — Python References and Mutability

## Topics Covered

* Python variables and objects
* Object references
* Mutable objects
* Immutable objects
* List mutation
* String immutability
* Assignment behavior
* Function argument references
* Mutable default arguments

## Variables Are References

In Python, a variable does not directly contain an object.

A variable stores a reference to an object.

```python
a = [1, 2, 3]
b = a
```

Both `a` and `b` reference the same list object.

Therefore:

```python
b.append(4)

print(a)
print(b)
```

Output:

```text
[1, 2, 3, 4]
[1, 2, 3, 4]
```

The list was mutated.

A new list was not created.

## Mutable Objects

Mutable objects can be changed after creation.

Examples:

* list
* dictionary
* set

Example:

```python
numbers = [1, 2, 3]

numbers.append(4)

print(numbers)
```

The existing list object is modified.

## Immutable Objects

Immutable objects cannot be modified after creation.

Examples:

* int
* float
* string
* tuple

Example:

```python
a = "hello"
b = a

b = b + " world"
```

`b` now references a new string object.

The original string remains unchanged.

```python
print(a)
print(b)
```

Output:

```text
hello
hello world
```

## Mutation vs Reassignment

Mutation changes an existing object.

```python
a = [1, 2]

a.append(3)
```

Reassignment changes the object referenced by a variable.

```python
a = [1, 2]

a = [3, 4]
```

These are fundamentally different operations.

## Mutable Default Arguments

Consider:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

Calling the function multiple times:

```python
print(add_item("new"))
print(add_item("new"))
print(add_item("new"))
```

Output:

```text
['new']
['new', 'new']
['new', 'new', 'new']
```

The default list is created once when the function is defined.

The same list object is reused across function calls.

## Correct Approach

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)

    return items
```

A new list is created for each function call.

## Data Engineering Connection

Understanding references and mutation is important when processing records in Python ETL pipelines.

Example:

```python
records = [
    {"id": 1, "status": "raw"},
    {"id": 2, "status": "raw"}
]

processed_records = records

for record in processed_records:
    record["status"] = "processed"
```

Because both variables reference the same objects, the original records are modified.

Unexpected mutation can introduce difficult-to-debug data quality issues in ETL pipelines.

## Key Takeaways

* Python variables store references to objects.
* Multiple variables can reference the same object.
* Mutable objects can change in place.
* Immutable objects create new objects when modified.
* Mutation and reassignment are different.
* Mutable default arguments can cause unexpected state sharing.
