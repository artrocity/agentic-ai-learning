"""
[ ] Day 11: OOP Inheritance
• Topic: Inheritance, subclasses.
• Resource: Real Python OOP Inheritance.
• Task: Extend the User class to a MentalHealthUser subclass with a method to log stress.
"""

# Day 11 Task:
# Extend the User class to a MentalHealthUser subclass with a method to log stress

# Inheritance Youtube Video
# https://www.youtube.com/watch?v=an6wd3dpEjA

# Day 10 OOP Code

class User:
    
    def __init__(self, name: str, stress_lvl: int) -> None:
        self.name = name
        self.stress_lvl = stress_lvl

    def __str__(self):
        return f'Name: {self.name} | Stress Level: {self.stress_lvl}'
    
# Day 11 Create a subclass with a method to log stress
class MentalHealthUser(User):
    def __init__(self, name: str, stress_lvl: int) -> None:
        super().__init__(name, stress_lvl)
        self.stress_logs: list[dict] = []

    def log_stress(self, stress_log: str) -> None:
        self.stress_log = stress_log

        # Create a log entry
        log_entry = {
            'name': self.name,
            'stress_lvl': self.stress_lvl,
            'log': stress_log
        }

        self.stress_logs.append(log_entry)

        try:
            with open('./stress_log.txt', 'a', encoding='utf-8') as file:
                file.write(f'{stress_log} \n')
        except IOError as e:
            print(f'Error writing to log file: {e}')

# Test the User class
basic_user = User('John', 5)
print(f'User:  {basic_user}')
print()

# Test the MentalHealthClass
mental_health_user = MentalHealthUser('Jane', 6)
print(f'User:  {mental_health_user}')
print()

# Test the log entry

# Add log entries
mental_health_user.log_stress('Feeling good today. Work went well!')

mental_health_user.log_stress('Workout went well today. Completed 1.5 hours!')

mental_health_user.log_stress('Stressful meeting this morning.')

# Check the logs
print('Checking the stored log entries: ')
print(f'Total Mental Health Logs: {len(mental_health_user.stress_logs)}')
for i, log in enumerate(mental_health_user.stress_logs, 1):
    print(f'    Log {i}: {log}')
print()
