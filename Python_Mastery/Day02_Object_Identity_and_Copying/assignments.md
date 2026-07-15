# Day 02 Assignments

## Assignment 1 — Identity

Predict the output:

```python
a = [1, 2, 3]

b = a

c = [1, 2, 3]

print(a == b)
print(a is b)

print(a == c)
print(a is c)
```

Explain every result.

---

## Assignment 2 — Shallow Copy

Predict the output:

```python
import copy

a = [[1, 2], [3, 4]]

b = copy.copy(a)

b.append([5, 6])

b[0].append(99)

print(a)
print(b)
```

Explain why the two operations behave differently.

---

## Assignment 3 — Deep Copy

Predict the output:

```python
import copy

a = {
    "users": [
        {"id": 1},
        {"id": 2}
    ]
}

b = copy.deepcopy(a)

b["users"][0]["id"] = 100

print(a)
print(b)
```

Explain the object isolation behavior.

---

## Assignment 4 — Debug the ETL Code

Consider:

```python
source_record = {
    "id": 101,
    "metadata": {
        "status": "raw",
        "source": "api"
    }
}

processed_record = source_record.copy()

processed_record["metadata"]["status"] = "processed"
```

The Data Engineer expects `source_record` to remain unchanged.

Answer:

1. Why does `source_record` change?
2. What objects are shared?
3. How can you verify this using `id()`?
4. How would you fix the problem?

---

## Assignment 5 — Engineering Decision

You are processing 10 million nested Python records.

A developer suggests using:

```python
copy.deepcopy(record)
```

for every record.

Answer:

1. Would you immediately approve this solution?
2. What memory concerns would you investigate?
3. What CPU concerns would you investigate?
4. Can the transformation be redesigned to avoid copying the entire object?
5. What would you measure before making the final decision?

Think like a production Data Engineer, not only a Python developer.
