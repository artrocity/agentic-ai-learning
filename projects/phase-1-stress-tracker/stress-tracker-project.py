# Imports
import pandas as pd
import matplotlib
import numpy as np
import datetime

# Function to gather user input data
def get_input():
    print('Getting Input....')

# Function to write the data
def log_data():
    print('Logging Data....')

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