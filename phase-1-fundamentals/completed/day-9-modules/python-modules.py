"""
[ ] Day 9: Python Modules and Libraries
• Topic: Importing modules (e.g., math, random).
• Resource: Real Python Modules Tutorial.
• Task: Use the random module to simulate a heart rate (60–120 bpm).
"""

# Day 9
# Task: Use the random module to simulate a heart rate (60–120 bpm).

# Import random
import random

# Have random choose a heart rate between 60-120
random_hr = random.randint(60,120)

# Print the random heart rate
print(random_hr)