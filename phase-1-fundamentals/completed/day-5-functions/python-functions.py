"""
[ ] Day 5: Functions
• Topic: Defining functions, parameters, return statements.
• Resource: Python.org Functions Tutorial.
• Task: Create a function that takes a heart rate value and returns “Normal” or “Elevated” (threshold: 100 bpm).  
"""

# Create a function that takes heart rate value and returns "Normal" or "Elevated" (threshold: 100 bpm)

# Define a function to check a given heart rate
def check_hr(hr_value: int) -> str:
    if hr_value > 100:
        return 'Elevated'
    else:
        return 'Normal'

# Obtain current heart rate from the user
current_hr = int(input('Please provide your current heart rate: '))

hr_value = check_hr(current_hr)

print(f'Your current heart rate is: {hr_value}')