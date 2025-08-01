"""
[ ] Day 4: Conditionals
• Topic: If-else statements, comparison operators.
• Resource: Codecademy Python (free section on conditionals).
• Task: Write a program that checks if a number is positive, negative, or zero.  
"""

# Write a program that checks if a number is positive, negative, or zero. 

# Obtain a number from the user
user_num = int(input('Please provide a number: '))

# Calculate if the number is positive, negative, or zero
if user_num > 0:
  print(f'{user_num} is Positive!')
elif user_num == 0: 
  print(f'{user_num} is Zero')
elif user_num < 0:
  print(f'{user_num} is Negative')
else:
  print("Not a valid number")