# Day 01 Interview Questions

## Question 1

What is the difference between a variable and an object in Python?

## Question 2

Predict the output:

```python
a = [1, 2, 3]
b = a

b.append(4)

print(a)
print(b)
```

Explain why.

## Question 3

What is the difference between mutation and reassignment?

## Question 4

Why are strings called immutable objects?

## Question 5

Predict the output:

```python
a = "hello"
b = a

b += " world"

print(a)
print(b)
```

Explain the memory behavior.

## Question 6

What is wrong with the following function?

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

## Question 7

Why are mutable default arguments dangerous?

## Question 8

How would you safely use a list as a function argument default value?

## Question 9

Consider an ETL pipeline where two variables reference the same list of dictionaries.

What data quality problems could unexpected mutation introduce?

## Question 10

Explain the following statement:

> Python variables are references to objects.
