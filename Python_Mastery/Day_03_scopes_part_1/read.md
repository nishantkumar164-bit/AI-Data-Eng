# Day 03 - Functions, Scope & Object References

## Learning Objectives

Today we learned how Python handles:

- Functions
- Parameters
- Object References
- Mutation vs Reassignment
- Scope
- LEGB Rule
- Global
- Nonlocal
- State Lifetime
- Production Design Thinking

---

# 1. Function Parameters

Python passes object references by assignment.

Example

```python
def modify(data):
    data.append(4)

a = [1,2,3]

modify(a)

print(a)