"""
[ ] Day 6: Dictionaries and Sets
• Topic: Key-value pairs, sets for unique items.
• Resource: Real Python Dictionaries Tutorial.
• Task: Store 3 user profiles (name, stress level) in a dictionary and print them.
"""

# Task: Store 3 user profiles (name, stress level) in a dictionary and print them

# Store 3 user profiles
users = {
  'user_1' : {
    'name' : 'Ryan',
    'stress_lvl' : 5
  },
  'user_2' : {
  'name' : 'John',
  'stress_lvl' : 6
  },
  'user_3' : {
  'name' : 'Jane',
  'stress_lvl' : 2
  }
}

# Print the all users
# for user, stress in users.items():
#   print(f'User: {stress['name']} Stress: {stress['stress_lvl']}')

# For better user data we would need to store users with stable identifiers
# To achieve this, we can use a list of dictionaries

users_2 = [
  {'id': 1, 'name': 'Ryan', 'stress_lvl': 5},
  {'id': 2, 'name': 'John', 'stress_lvl': 6},
  {'id': 3, 'name': 'Jane', 'stress_lvl': 2}
]

# Print the list
for user in users_2:
  print(f'ID: {user['id']}, Name: {user['name']}, Stress: {user['stress_lvl']}')




