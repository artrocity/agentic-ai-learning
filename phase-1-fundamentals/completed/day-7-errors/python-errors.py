"""
[ ] Day 7: Error Handling
• Topic: Try-except blocks, handling invalid inputs.
• Resource: Programiz Python Exception Handling.
• Task: Modify Day 5’s function to handle non-numeric inputs gracefully.
"""

# Day 7 Task
# Modify Day 5’s function to handle non-numeric inputs gracefully.

# Day 5's work
# Create a function that takes heart rate value and returns "Normal" or "Elevated" (threshold: 100 bpm)

# Define a function to check a given heart rate
def get_user_hr() -> int:
    user_hr = None

    while user_hr is None:
        try:
            user_hr = int(input('Please provide your current heart rate: '))
        except ValueError:
            print(f'Heart rate has to be a valid number')

    return user_hr
          
def check_hr(hr_value: int) -> str:
    if hr_value > 100:
        return 'Elevated'
    else:
        return 'Normal'


def main():
    heart_rate = get_user_hr()
    hr_value = check_hr(heart_rate)
    print(f'Your current heart rate is: {hr_value}')

if __name__ == '__main__':
    main()