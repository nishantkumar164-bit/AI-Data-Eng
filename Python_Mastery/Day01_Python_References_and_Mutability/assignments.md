# Day 01 Assignments

## Assignment 1 — Predict the Output

Do not run the code before predicting the output.

```python
a = [1, 2]

b = a

b.append(3)

b = [10, 20]

print(a)
print(b)
```

Explain every operation.

---

## Assignment 2 — Nested Mutation

Predict the output:

```python
a = [[1, 2], [3, 4]]

b = a

b[0].append(99)

print(a)
print(b)
```

Explain why the value `99` appears in the output.

---

## Assignment 3 — Immutable Objects

Predict the output:

```python
a = 10
b = a

b += 5

print(a)
print(b)
```

Explain why `a` does not change.

---

## Assignment 4 — Fix the Function

Fix the following function:

```python
def add_record(record, records=[]):
    records.append(record)
    return records
```

The function must return a new list when no list is explicitly provided.

Explain why your solution works.

---

## Assignment 5 — ETL Mutation Problem

Consider the following ETL code:

```python
raw_records = [
    {"id": 1, "status": "raw"},
    {"id": 2, "status": "raw"}
]

processed_records = raw_records

for record in processed_records:
    record["status"] = "processed"

print(raw_records)
```

Answer the following questions:

1. What will be printed?
2. Why was `raw_records` modified?
3. How would you prevent the original records from being modified?
4. Why could this become a production issue in a Data Engineering pipeline?
