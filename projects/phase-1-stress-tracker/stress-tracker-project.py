# Imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import json

# Function to gather user's name
def get_user_name() -> tuple:
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
    user_name = get_user_name()

    # Obtain user heart rate and stress level
    hr, stress_level = get_hr_stress()

    # Get current date and time
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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
        with open('./data/user_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # loop through data and see if user exists and add their entry
        if any(user_name.lower() == d['name'].lower() for d in data):
            # Grab user's log entry and append just the entries portion to their record
            for user in data:
                if user_name.lower() == user['name'].lower():
                    user['entries'].append(log_entry['entries'][0])

            # Write the entry to the file
            with open('./data/user_data.json', 'w', encoding='utf-8') as file:
                json.dump(data, file)

            # Notify the user their entry has been added
            print(f'Entry for {user_name} has been created.')

        # If they dont exist append their record
        else:
            # Notify user not found
            print(f'User not found, Creating a record for {user_name} now...')

            # Append the entry to the log
            data.append(log_entry)

            # Write the entry to the file
            with open('./data/user_data.json', 'w', encoding='utf-8') as file:
                json.dump(data, file)
        
    
    except FileNotFoundError:
        with open('./data/user_data.json', 'w', encoding='utf-8') as file:
            # Notify the user the file wasn't found
            print('User data file not found. Creating it now...')

            # Create an empty list of users
            user_data = []

            # Append log entry to file
            user_data.append(log_entry)

            # Convert to a JSON string and write it to a file
            json.dump(user_data, file)

            # Notify user that the file has been created
            print(f'User data file created. Log file created for: {user_name}')


def view_entries():
    # Obtain user's profile to plot
    user_name = get_user_name()

    # Notify the user that we're attempting to access the records
    print(f'Attempting to access records for: {user_name}')

    with open('./data/user_data.json', 'r', encoding='utf-8') as file:
        user_data = json.load(file)

    # Loop through the data and find the relevant user profile
    for record in user_data:
        if record['name'].lower() == user_name.lower():
            print(f'Found User: {user_name}\n')
            print('------RECORDS------')
            print(f'Entries for {user_name}')
            for entries in record['entries']:
                print(f'    {entries}')
        else:
            print(f'User {user_name} not found')

def plot_entries():
    # Obtain user's profile to plot
    user_name = get_user_name()

    with open('./data/user_data.json', 'r', encoding='utf-8') as file:
        user_data = json.load(file)

    # Notify the user that we're attempting to access the records
    print(f'Attempting to access records for: {user_name}')

    try:
        with open('./data/user_data.json', 'r', encoding='utf-8') as file:
            user_data = json.load(file)

        # Find the user's data
        user_found = False
        for record in user_data:
            if record['name'].lower() == user_name.lower():
                user_found = True
                print(f'Found User: {user_name}')
                
                # Check if user has any entries
                if not record['entries']:
                    print(f'No entries found for {user_name}')
                    return
                
                # Convert entries to DataFrame
                df = pd.DataFrame(record['entries'])
                
                # Convert date strings to datetime objects
                df['date'] = pd.to_datetime(df['date'])
                
                # Sort entries by date 
                df = df.sort_values('date')
                
                # Simple plotting approach
                plt.figure(figsize=(10, 6))
                
                # Plot both lines on the same graph
                plt.plot(df['date'], df['heart_rate'], 'b-o', label='Heart Rate (BPM)')
                plt.plot(df['date'], df['stress_level'], 'r-s', label='Stress Level (1-10)')
                
                # Add labels and title
                plt.xlabel('Date')
                plt.ylabel('Values')
                plt.title(f'Health Tracking Data for {user_name}')
                plt.legend()  
                plt.xticks(rotation=45)
                
                # Display the plot
                plt.show()
                
                # Print some basic statistics
                print(f"\n--- Statistics for {user_name} ---")
                print(f"Total entries: {len(df)}")
                print(f"Average heart rate: {df['heart_rate'].mean():.1f} BPM")
                print(f"Average stress level: {df['stress_level'].mean():.1f}")
                print(f"Highest stress level: {df['stress_level'].max()}")
                
                break
        
        if not user_found:
            print(f'User {user_name} not found')
            
    except FileNotFoundError:
        print('User data file not found. Please log some data first.')
    except Exception as e:
        print(f'Error reading data: {e}')


def delete_data():
    print('Deleting Data....')

# Main Function
def main():

    print('Welcome to your personal stress tracker')
    print('Available Options')
    print('------ 1.) Record your stress level and heart rate.')
    print('------ 2.) View a complete record of your entries.')
    print('------ 3.) View a graph summary of your entries.')
    print('------ 4.) Delete your personal record data. \n')

    try:
        user_choice = input('Please choose an option: 1 - 4: ')

        match user_choice:
            case '1':
                log_data()
            case '2':
                view_entries()
            case '3':
                plot_entries()
            case '4':
                delete_data()
            case _:
                print("Invalid option. Please choose a number between 1-4")

    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()