import time
import pandas as pd
import numpy as np

data = { 'chicago': 'chicago.csv',
         'new york city': 'new_york_city.csv',
         'washington': 'washington.csv' }
month_list = ['january', 'february', 'march', 'april', 'may', 'june']
days_list = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

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

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(data[city])
    # extract month and day
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    # filter by month if applicable
    if month != 'all':
        month = month_list.index(month)+1
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        day = days_list.index(day)
        df = df[df['day_of_week'] == day]
    
    return df

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    # Display counts of user types
    print('Number of different user types:\n',df['User Type'].value_counts())
    # Display counts of gender and
    # Display earliest, most recent, and most common year of birth
    if city != 'washington':
        print('\nUsers gender:\n',df['Gender'].value_counts())
        print('\n The oldest user was born in: ',df['Birth Year'].min())
        print('The youngest user was born in: ',df['Birth Year'].max())
    else:
        print('\nGender and birth year data is not available for this city.')
    
    

city, month, day = filters()
df = load_data(city, month, day)
user_stats(df, city)