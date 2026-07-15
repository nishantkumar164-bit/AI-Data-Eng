# Day 02 Interview Questions

## Question 1

What is object identity in Python?

## Question 2

What does the `id()` function return?

## Question 3

Explain the difference between:

```python
==
```

and:

```python
is
```

## Question 4

Predict the output:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
```

## Question 5

What is a shallow copy?

## Question 6

Why are nested mutable objects shared in a shallow copy?

## Question 7

What is a deep copy?

## Question 8

Explain the difference between:

```python
b = a
```

```python
b = copy.copy(a)
```

```python
b = copy.deepcopy(a)
```

## Question 9

Why should `deepcopy()` not be used blindly in production systems?

## Question 10

You receive nested JSON data from an API.

You create a shallow copy and modify a nested dictionary.

Why might the original API record also change?

Explain how you would debug and fix the issue.
