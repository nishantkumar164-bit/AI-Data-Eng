# ================================
# List Comprehension
# ================================

numbers = [1, 2, 3, 4, 5]

squares = [n ** 2 for n in numbers]

print(squares)

# ================================
# Filtering
# ================================

evens = [n for n in numbers if n % 2 == 0]

print(evens)

# ================================
# if else
# ================================

result = [
    "Even" if n % 2 == 0 else "Odd"
    for n in numbers
]

print(result)

# ================================
# Nested
# ================================

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

flatten = [
    num
    for row in matrix
    for num in row
]

print(flatten)

# ================================
# Dictionary
# ================================

employees = [
    {"id": 101, "salary": 80000},
    {"id": 102, "salary": 120000},
    {"id": 103, "salary": 95000}
]

salary_lookup = {
    emp["id"]: emp["salary"]
    for emp in employees
}

print(salary_lookup)

# ================================
# Dictionary Filter
# ================================

high_salary = {
    emp["id"]: emp["salary"]
    for emp in employees
    if emp["salary"] >= 100000
}

print(high_salary)

# ================================
# Set
# ================================

skills = [
    "Python",
    "SQL",
    "Python",
    "AWS",
    "SQL",
    "PySpark"
]

unique_skills = {
    skill
    for skill in skills
}

print(unique_skills)