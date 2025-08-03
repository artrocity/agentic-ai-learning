"""
[ ] Day 8: File I/O
• Topic: Reading/writing text files for data storage.
• Resource: Automate the Boring Stuff (Chapter 10).
• Task: Save a list of stress levels to a file and read it back.
"""

# Day 8 Task
# Save a list of stress levels to a file and read it back.

# Define a list of stress levels
stress_levels = [3, 5, 2, 4, 6]

# Open a file and save the stress levels
with open('./stress_levels.txt', 'w') as file:
    for level in stress_levels:
        file.write(str(level) + '\n')

with open('./stress_levels.txt') as file:
    for line in file:
        print(line.strip())
