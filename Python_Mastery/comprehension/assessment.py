"""
Module 2 Assessment

Do NOT use normal loops unless explicitly asked.

Solve every question using comprehensions.
"""

# ------------------------------------------------
# Question 1
# ------------------------------------------------

numbers = [5, 10, 15, 20, 25]

# Create a list of squares.

# ------------------------------------------------
# Question 2
# ------------------------------------------------

numbers = [2, 7, 12, 17, 22, 27]

# Keep only numbers greater than 15.

# ------------------------------------------------
# Question 3
# ------------------------------------------------

numbers = [4, 9, 15, 20]

# Convert into
# ["Small", "Small", "Large", "Large"]

# Rule
# >=15 -> Large

# ------------------------------------------------
# Question 4
# ------------------------------------------------

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

# Flatten the matrix.

# ------------------------------------------------
# Question 5
# ------------------------------------------------

employees = [
    {"id": 1, "salary": 60000},
    {"id": 2, "salary": 120000},
    {"id": 3, "salary": 90000}
]

# Create
# {id : salary}

# ------------------------------------------------
# Question 6
# ------------------------------------------------

employees = [
    {"id": 1, "salary": 60000},
    {"id": 2, "salary": 120000},
    {"id": 3, "salary": 90000}
]

# Create dictionary only for salary >=100000

# ------------------------------------------------
# Question 7
# ------------------------------------------------

skills = [
    "Python",
    "SQL",
    "Python",
    "AWS",
    "Docker",
    "SQL"
]

# Create a set of unique skills.

# ------------------------------------------------
# Question 8 (Interview Level)
# ------------------------------------------------

customers = [
    {
        "customer": "A",
        "orders": [
            {"amount": 100},
            {"amount": 250}
        ]
    },
    {
        "customer": "B",
        "orders": [
            {"amount": 700},
            {"amount": 50}
        ]
    }
]

# Extract only amounts >=200.

# Expected

# [250,700]

print("\nModule 2 Assessment Complete")