# Module 2 - Python Comprehensions

## Objective

Learn Python comprehensions to write concise, readable, and efficient code for transforming, filtering, and flattening collections.

This module focuses on production-ready usage rather than memorizing syntax.

---

# Topics Covered

## List Comprehensions

- Basic list comprehension
- Filtering using `if`
- Conditional expression (`if...else`)
- Multiple conditions
- Nested loops
- Nested loops with filtering
- Flattening nested lists
- Processing nested JSON

---

## Dictionary Comprehensions

- Creating dictionaries
- Filtering entries
- Creating lookup maps
- Production examples

---

## Set Comprehensions

- Creating unique collections
- Filtering
- Removing duplicates

---

# General Syntax

## List

```python
[expression for item in iterable]
```

With filter

```python
[expression for item in iterable if condition]
```

Conditional expression

```python
[true_value if condition else false_value for item in iterable]
```

Nested

```python
[
    expression
    for outer in collection
    for inner in outer
]
```

---

## Dictionary

```python
{
    key: value
    for item in iterable
}
```

Filtering

```python
{
    key: value
    for item in iterable
    if condition
}
```

---

## Set

```python
{
    expression
    for item in iterable
}
```

---

# Performance

Most comprehensions

Time Complexity

```
O(n)
```

Space Complexity

```
O(n)
```

---

# Best Practices

✅ Prefer meaningful variable names.

```python
employee
student
order
record
```

instead of

```python
e
s
x
```

for complex objects.

---

Keep comprehensions readable.

Good

```python
[
    employee["name"]
    for employee in employees
    if employee["active"]
]
```

Avoid writing very long nested comprehensions.

If readability suffers, use normal loops.

---

# Common Use Cases

- ETL pipelines
- API response transformation
- Data filtering
- Flattening nested JSON
- Lookup dictionary creation
- Removing duplicates

---

# Module Completed

- List Comprehensions
- Dictionary Comprehensions
- Set Comprehensions

