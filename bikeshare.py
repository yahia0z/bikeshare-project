import time
import pandas as pd
import numpy as np

data = { 'chicago': 'chicago.csv',
         'new york city': 'new_york_city.csv',
         'washington': 'washington.csv' }

def filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\nPlease enter a city to analyze its data.')
    # get user input for city
    while True:
        try:
            city = input('Please select a city from Chicago, New York City, or Washington.\n').lower()
        except ValueError:
            print('Not a valid input. Please select a city from Chicago, New York City, or Washington.')
        else:
            if (city=='chicago') or (city=='new york city') or (city=='washington'):
                print('Selected city is: ',city.title())
                break
            else:
                print('Not a valid city.')
    
            
filters()
