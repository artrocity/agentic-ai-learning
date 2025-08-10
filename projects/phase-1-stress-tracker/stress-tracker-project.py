# Imports
import pandas as pd
import matplotlib
import numpy as np
import datetime
import json

# Function to gather user's name
def get_input() -> tuple:
    while True:
        try:
            user_name = input('Please provide your full name: ').strip()
            
            if user_name:
                return user_name
        except Exception as e:
            print(f'Error: {e}')

# Function to gather user's heart rate and stress levels
def get_hr_stress():
    while True:
        try:
            hr = int(input('Please provide your current heart_rate: '))
            stress_level = int(input('Please provide your current stress level on a scale from 1-10: '))

            if hr and stress_level:
                return hr, stress_level
        
        except Exception as e:
            print(f'Error: {e}')

# Function to write the data
def log_data():
    # Obtain user name
    user_name = get_input()

    # Obtain user heart rate and stress level
    hr, stress_level = get_hr_stress()

    # Get current date and time
    current_datetime = datetime.datetime.now()

    # Model data for logging
    log_entry = {
        'name': user_name,
        'entries' : [
            {
                'date': current_datetime,
                'heart_rate': hr,
                'stress_level': stress_level
            }
        ]
    }

    # Read from file and see if user data exists
    try:
        with open('user_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # loop through data and see if user exists and add their entry
        if any(user_name.lower() == d['name'].lower() for d in data):
            # Grab user's log entry and append just the entries portion to their record
            for user in data:
                if user_name.lower() == user['name'].lower():
                    user['entries'].append(log_entry['entries'][0])

            with open('user_data.json', 'w', encoding='utf-8') as file:
                json.dump(data, file)

        # If they dont exist append their record
        else:
            data.append(log_entry)
            with open('user_data.json', 'w', encoding='utf-8') as file:
                json.dump(data, file)
        
    
    except FileNotFoundError:
        with open('user_data.json', 'w', encoding='utf-8') as file:
            # Create an empty list of users
            user_data = []

            # Convert to a JSON string and write it to a file
            json.dump(user_data, file)


def plot_data():
    print('Plotting Data....')

def delete_data():
    print('Deleting Data....')

# Main Function
def main():

    print('Welcome to your personal stress tracker')
    print('Available Options')
    print('------1.)Record your stress level and heart rate.')
    print('------2.)View your stress summary.')
    print('------3.)Delete your personal record data. \n')

    try:
        user_choice = input('Please choose an option: 1 - 3: ')

        match user_choice:
            case '1':
                log_data()
            case '2':
                plot_data()
            case '3':
                delete_data()

    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()