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
    
    # get user input for month
    month_list = ['january', 'february', 'march', 'april', 'may', 'june']
    print('Please select a month to filter by.')
    while True:
        try:
            month = input('Enter one of the first six months or \'all\' for all months:\n').lower()
        except ValueError:
            print('Not a valid input.')
        else:
            if month in month_list:
                print('Selected month is: ', month.title())
                break
            elif month == 'all':
                print('No month filter selected')
                break
            else:
                print('Not a valid input.')

    # get user input for day
    days_list = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while True:
        try:
            day = input('Enter a day to filter by or \'all\' for all days:\n').lower()
        except ValueError:
            print('Not a valid input.')
        else:
            if day in days_list:
                print('Selected day is: ', day.title())
                break
            elif day == 'all':
                print('No day filter selected')
                break
            else:
                print('Not a valid input.')

    return city, month, day
      
filters()
