# SOLID — Final Assignment
#
# Build a maintainable e-commerce order-processing system.
#
# IMPORTANT:
# First design the classes on paper.
# Then implement them.
# Then explain where each SOLID principle appears.

# ============================================================
# PART 1 — DOMAIN
# ============================================================
# Product:
#   name
#   price
#   quantity
#
# Order:
#   contain products
#   expose order-related behavior
#
# Order must NOT be responsible for:
#   - database persistence
#   - notifications
#   - payment processing


# ============================================================
# PART 2 — CALCULATION
# ============================================================
# Create OrderCalculator.
#
# Example:
# Product A: ₹100 x 2
# Product B: ₹200 x 1
# Total: ₹400


# ============================================================
# PART 3 — DISCOUNTS
# ============================================================
# Create a discount abstraction.
#
# Implement:
#   RegularDiscount -> 5%
#   PremiumDiscount -> 10%
#   VIPDiscount     -> 20%
#   StudentDiscount -> 15%
#
# Each should support:
#   apply(amount)
#
# Do not create a central if/elif chain.


# ============================================================
# PART 4 — PAYMENTS
# ============================================================
# Create a payment abstraction.
#
# Implement:
#   UPIPayment
#   CardPayment
#   PayPalPayment
#
# Each should support:
#   pay(amount)


# ============================================================
# PART 5 — REPOSITORY
# ============================================================
# Create a repository abstraction.
#
# Implement:
#   MySQLRepository
#   PostgreSQLRepository
#
# Each should support:
#   save(order)


# ============================================================
# PART 6 — NOTIFICATION
# ============================================================
# Create a focused notification abstraction.
#
# Implement:
#   EmailNotification
#   WhatsAppNotification
#   SMSNotification
#
# Each should support:
#   send(message)


# ============================================================
# PART 7 — DEPENDENCY INJECTION
# ============================================================
# Create OrderService.
#
# Dependencies should be supplied from outside:
#
# service = OrderService(
#     calculator,
#     discount,
#     payment,
#     repository,
#     notification
# )
#
# Do NOT hard-code concrete dependencies inside OrderService.


# ============================================================
# PART 8 — SOLID VERIFICATION
# ============================================================
# Add comments explaining where:
#
# S = Single Responsibility
# O = Open/Closed
# L = Liskov Substitution
# I = Interface Segregation
# D = Dependency Inversion
#
# are being applied.


# ============================================================
# PART 9 — EXTENSION TEST
# ============================================================
# Without changing core OrderService, add:
#
# CorporateDiscount -> 25%
# NetBankingPayment
# MongoDBRepository
# SlackNotification
#
# Demonstrate that existing high-level logic still works.


# ============================================================
# PART 10 — TESTING WITH FAKE DEPENDENCIES
# ============================================================
# Create:
#
# FakeRepository
# FakePayment
#
# Inject them into OrderService and demonstrate that the
# service can be tested without a real database/payment gateway.


# ============================================================
# BONUS
# ============================================================
# Build the same design twice:
#
# Version 1:
#   ABC + @abstractmethod
#
# Version 2:
#   Duck typing without inheritance
#
# Compare:
#   - readability
#   - explicit contracts
#   - flexibility
#   - testing
#   - maintainability
#
# Save your comparison as:
#     design-notes.md
