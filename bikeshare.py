import time
import datetime
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

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    if month == 'all':
        com_month = month_list[df['month'].mode()[0]-1]
    else:
        com_month = month
    print('The most common month is',com_month.title())
    # display the most common day of week
    if day == 'all':
        com_day = days_list[df['day_of_week'].mode()[0]-1]
    else:
        com_day = day
    print('The most common day is',com_day.title())
    # display the most common start hour
    com_hour = df['Start Time'].dt.hour.mode()[0]
    print('The most common hour is {}:00'.format(com_hour))
    print('\nThis took {} seconds.'.format(time.time() - start_time))
    print('-'*40)
    
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
    com_trip_1(df)
    #com_trip_2(df)
    
# method one for most common trip
def com_trip_1(df):
    start_time = time.time()
    trips = []
    trips_df = pd.DataFrame()
    trips_df['start'] = df['Start Station'].copy()
    trips_df['end'] = df['End Station'].copy()
    for start, end in zip(trips_df.start, trips_df.end):
        trips.append((start, end))
    trips = pd.Series(trips)
    com_trip = trips.mode()[0]
    print('Most common trip is from {} to {}.'.format(com_trip[0], com_trip[1]))
    print("\nThis took {} seconds.".format(time.time() - start_time))

# method two for most common trip
def com_trip_2(df):
    start_time = time.time()
    trips = []
    for i, s in df.iterrows():
        trips.append((s['Start Station'], s['End Station']))
    trips = pd.Series(trips)
    com_trip = trips.mode()[0]
    print('Most common trip is from {} to {}.'.format(com_trip[0], com_trip[1]))
    print("\nThis took {} seconds.".format(time.time() - start_time))

def trip_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # total travel time
    total_time = str(datetime.timedelta(seconds = int(df['Trip Duration'].sum())))
    # average travel time
    avg_time = str(datetime.timedelta(seconds = int(df['Trip Duration'].mean())))
    print('Total travel time = {}\nAverage travel time = {}'.format(total_time, avg_time))
    print("\nThis took {} seconds.".format(time.time() - start_time))
    

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    print('Number of different user types:\n',df['User Type'].value_counts())
    # Display counts of gender and
    # Display earliest, most recent, and most common year of birth
    if city != 'washington':
        print('\nUsers gender:\n',df['Gender'].value_counts())
        print('\n The oldest user was born in: ',df['Birth Year'].min())
        print('The youngest user was born in: ',df['Birth Year'].max())
        print('The most common year of birth is: ',df['Birth Year'].mode()[0])
    else:
        print('\nGender and birth year data is not available for this city.')
    print("\nThis took {} seconds.".format(time.time() - start_time))

def disp_raw_data(df):
    """Displays the row data depending on the user's choice."""
    # adjust dataframe index
    df.index = list(range(0, len(df.index)))
    # get user response and display data
    answer = input('\nWould you like to see the raw data? Enter Y or N: ').lower()
    if answer == 'y':
        i = 0
        print('Displaying first 5 rows of the raw data...\n')
        while (answer == 'y'):
            print(df.iloc[i:i+5,:-2])
            i += 5
            if i >= len(df.index):
                print('No more data to display')
                break
            answer = input('\nWould you like to see more raw data? Enter Y or N:').lower()
            if answer == 'y':
                print('Displaying the next 5 rows of the raw data...\n')

def main():
    """Calls the different functions and allows for restarting the program."""
    while True:
        city, month, day = filters()
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_stats(df)
        user_stats(df, city)
        disp_raw_data(df)
        restart = input('\nWould you like to restart? Enter Y or N.\n')
        if restart.lower() != 'y':
            break  



if __name__ == "__main__":
	main()