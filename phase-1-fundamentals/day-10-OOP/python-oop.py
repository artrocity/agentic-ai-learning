"""
[ ] Day 10: Object-Oriented Programming (OOP) Basics
• Topic: Classes, objects, methods.
• Resource: Corey Schafer’s OOP Python Tutorial (YouTube, first 30 minutes).
• Task: Create a User class with attributes for name and stress level.
"""

# Day 10
# Task: Create a User class with attributes for name and stress level.

class User:
    
    def __init__(self, name: str, stress_lvl: int) -> None:
        self.name = name
        self.stress_lvl = stress_lvl

    def __str__(self):
        return f'Name: {self.name} | Stress Level: {self.stress_lvl}'

user1 = User(name='Test User', stress_lvl= 8)

print(user1)


