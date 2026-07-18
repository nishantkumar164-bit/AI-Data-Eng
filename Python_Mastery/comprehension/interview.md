# Python Comprehensions Interview Notes

## Why use list comprehensions?

- Cleaner syntax
- More readable
- Slightly faster than append loops
- Pythonic

---

## Difference

Filtering

```python
[x for x in nums if x > 10]
```

Transformation

```python
["Large" if x > 10 else "Small" for x in nums]
```

---

## Nested Comprehension

Normal loop

```python
for row in matrix:
    for item in row:
```

Equivalent

```python
[item for row in matrix for item in row]
```

---

## Dictionary Comprehension

```python
{
    employee["id"]: employee["salary"]
    for employee in employees
}
```

---

## Set Comprehension

```python
{
    skill
    for skill in skills
}
```

---

## Is there a Tuple Comprehension?

No.

```python
(x for x in range(5))
```

creates a

Generator Expression

not a tuple.

---

## Time Complexity

List

O(n)

Dictionary

O(n)

Set

O(n)

---

## Production Use Cases

- Flatten API responses
- Create lookup dictionaries
- Remove duplicates
- Filter records before ETL
- Prepare data before Spark DataFrame creation

---

## Best Practice

Keep comprehensions readable.

If the comprehension becomes difficult to understand, use normal loops.

Readability > Cleverness.