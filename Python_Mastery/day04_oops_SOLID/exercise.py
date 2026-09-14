# SOLID — Exercises
#
# Work through these before looking for a solution.
# Focus first on identifying the design problem and explaining your reasoning.

# ============================================================
# Exercise 1 — SRP
# ============================================================
# Identify the responsibilities and refactor this class.
#
# class User:
#     def register(self): pass
#     def validate_email(self): pass
#     def hash_password(self): pass
#     def save_to_database(self): pass
#     def send_welcome_email(self): pass


# ============================================================
# Exercise 2 — SRP
# ============================================================
# Refactor this into focused classes.
#
# class Order:
#     def calculate_total(self): pass
#     def save_to_database(self): pass
#     def send_confirmation_email(self): pass
#     def generate_invoice(self): pass


# ============================================================
# Exercise 3 — OCP
# ============================================================
# Refactor this so StudentDiscount can be added without
# modifying the main discount-processing logic.
#
# class DiscountCalculator:
#     def calculate(self, customer_type, amount):
#         if customer_type == "regular":
#             return amount * 0.05
#         elif customer_type == "premium":
#             return amount * 0.10
#         elif customer_type == "vip":
#             return amount * 0.20


# ============================================================
# Exercise 4 — OCP + Duck Typing
# ============================================================
# Create PDFReport, CSVReport, ExcelReport, JSONReport.
# Each must have generate().
#
# Then write:
#
# def generate_report(report):
#     ...
#
# Add XMLReport afterward without changing generate_report().


# ============================================================
# Exercise 5 — LSP
# ============================================================
# Explain and refactor:
#
# class Bird:
#     def fly(self):
#         print("Flying")
#
# class Penguin(Bird):
#     def fly(self):
#         raise Exception("Cannot fly")


# ============================================================
# Exercise 6 — LSP
# ============================================================
# Redesign so every child honors its parent's contract.
#
# class Employee:
#     def work(self):
#         print("Working")
#
#     def get_salary(self):
#         return 50000
#
# class Intern(Employee):
#     def get_salary(self):
#         raise Exception("Intern has no salary")


# ============================================================
# Exercise 7 — ISP
# ============================================================
# Split this giant interface into focused capabilities.
#
# class Worker(ABC):
#     @abstractmethod
#     def work(self): pass
#
#     @abstractmethod
#     def drive(self): pass
#
#     @abstractmethod
#     def cook(self): pass
#
#     @abstractmethod
#     def manage_team(self): pass
#
# Create Developer, Driver, Chef, and Manager.


# ============================================================
# Exercise 8 — ISP
# ============================================================
# Smart-home capabilities:
#     TurnOn
#     TurnOff
#     SetTemperature
#     PlayMusic
#     DisplayVideo
#
# Design Light, AirConditioner, SmartSpeaker, and SmartTV
# without forcing devices to implement unnecessary methods.


# ============================================================
# Exercise 9 — DIP
# ============================================================
# Refactor this so OrderService does not directly create
# FileLogger.
#
# class FileLogger:
#     def log(self, message):
#         print(f"Writing to file: {message}")
#
# class OrderService:
#     def __init__(self):
#         self.logger = FileLogger()
#
#     def place_order(self, order):
#         print("Order placed")
#         self.logger.log("Order was placed")


# ============================================================
# Exercise 10 — DIP + Testing
# ============================================================
# Create:
#     PaymentGateway
#         ├── StripeGateway
#         ├── RazorpayGateway
#         └── FakePaymentGateway
#
# Create CheckoutService using dependency injection.
# Use FakePaymentGateway to test without a real payment service.


# ============================================================
# FINAL INTEGRATED EXERCISE
# ============================================================
# Build a small e-commerce system with:
#
# Product
# Order
# Discount
# Payment
# Repository
# Notification
#
# Support:
#     Discounts: Regular, Premium, VIP, Student
#     Payments: UPI, Card, PayPal
#     Repositories: MySQL, PostgreSQL
#     Notifications: Email, WhatsApp, SMS
#
# Requirements:
# 1. Follow SRP.
# 2. Follow OCP when adding new discounts/payments.
# 3. Ensure implementations satisfy their abstractions (LSP).
# 4. Avoid giant interfaces (ISP).
# 5. Inject repositories/payment/notification dependencies (DIP).
#
# Extension test:
# Add:
#     CorporateDiscount
#     NetBankingPayment
#     MongoDBRepository
#     SlackNotification
#
# Try to do this with zero modification to the core OrderService.
