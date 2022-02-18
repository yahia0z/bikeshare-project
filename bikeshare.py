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

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    # display most commonly used start station
    com_start = df['Start Station'].mode()[0]
    print('The most commonly used start station is:',com_start)
    # display most commonly used end station
    com_end = df['End Station'].mode()[0]
    print('The most commonly used end station is:',com_end)
    # display most frequent combination of start station and end station trip
    #com_trip_1(df)
    com_trip_2(df)
    
# method one for most common trip
def com_trip_1(df):
    trips = []
    trips_df = pd.DataFrame()
    trips_df['start'] = df['Start Station'].copy()
    trips_df['end'] = df['End Station'].copy()
    for start, end in zip(trips_df.start, trips_df.end):
        trips.append((start, end))
    trips = pd.Series(trips)
    com_trip = trips.mode()[0]
    print('Most common trip is from {} to {}.'.format(com_trip[0], com_trip[1]))

# method two for most common trip
def com_trip_2(df):
    trips = []
    for i, s in df.iterrows():
        trips.append((s['Start Station'], s['End Station']))
    trips = pd.Series(trips)
    com_trip = trips.mode()[0]
    print('Most common trip is from {} to {}.'.format(com_trip[0], com_trip[1]))

city, month, day = filters()
df = load_data(city, month, day)
station_stats(df)
