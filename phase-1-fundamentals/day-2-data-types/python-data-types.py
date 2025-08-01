"""
[ X ] Day 2: Data Types and Operations
• Topic: Strings, integers, floats, basic arithmetic, and type conversion.
• Resource: W3Schools Python Data Types.
• Task: Write a program to calculate your age based on birth year input.
"""

# Obtain birth year from user
user_birth_year = input("Please enter the year you were born: ")

# Calculate the year user was born
current_age = 2025 - int(user_birth_year)

print(f'You are: {current_age} years old!')
