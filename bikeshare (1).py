import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'new york city', 'washington']
MONTHS = ['january', 'february','march','april','may','june','all']
DAYS = ['sunday','monday', 'tuesday','wednesday','thursday','friday','saturday','all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze

        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('Enter city name as suggested above in the dictionary:').lower()
            if city in CITIES:
                break
        except:
            print('Enter a valid city:')
        print('\nAttempted Input\n')
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('Enter month name as suggested above in the dictionary:').lower()
            if month in MONTHS:
                break
        except:
            print('Enter a valid month:')
        print('\nAttempted Input\n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Enter day name as suggested above in the dictionary:').lower()
            if day in DAYS:
                break
        except:
            print('Enter a valid day:')
        print('\nAttempted Input\n')


    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city])

    #convert the Start Time by using datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #convert the month, day, hour by using datetime
    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    df['hour'] = df['Start Time'].dt.hour


    #TO DO: if user input wants to view all months
    if month != 'all':
        month =  MONTHS.index(month) + 1
        df = df[ df['month'] == month ]
    print(df['day_of_week'].head())

    # filter by day of week if applicable
    if day != 'all':
        df = df[ df['day_of_week'] == day.title()]
    print(df['day_of_week'].head())
    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()
    print('The most common month is:{}'.format(most_common_month))


    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()
    print('The most common d.o.w is:{}'.format(most_common_day))

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()
    print('The most common hour is:{}'.format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))

    print(df.head())
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :{}".format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :{}".format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    most_used_station = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('The most frequent of the End Station and Start station:{}'.format(most_used_station))
    print("\nThis took %s seconds." % (time.time() - start_time))


    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_distance_travelled = df['Trip Duration'].sum()
    print('The cummulative total distance travelled by users is:{}'.format(total_distance_travelled))

    # TO DO: display mean travel time
    mean_distance_travelled = df['Trip Duration'].mean()
    print('The mean distance travelled is:{}'.format(mean_distance_travelled))

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    Count_users = df['User Type'].value_counts()
    for name,count_user in enumerate(Count_users):
        print('{}:{}'.format(Count_users.index[name],count_user))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_stat(df)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        birth_stat(df)

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)
def gender_stat(df):
    gender_counts = df['Gender'].value_counts()
    for name,gender_count in enumerate(gender_counts):
        print('{}:{}'.format(gender_counts.index[name],gender_count))

def birth_stat(df):
    #The most common year of birth
    common_birth = df['Birth Year']
    most_common_birth = common_birth.mode()
    print('The most common year of birth:{}'.format(most_common_birth))

    #The most recent year of birth
    birth_year = df['Birth Year']
    most_recent = birth_year.max()
    print("The most recent birth year:{}".format(most_recent))
    #The earliest year of birth
    mini_year = df['Birth Year']
    earliest_birth = birth_year.min()
    print("The most earliest birth year:{}".format(earliest_birth))
  
def row_view(df):
    """This is to show the user the five rows of the data set for the respective city,month and day respectively"""
    print("do you want to view 5 rows of data? answer the next question below ")
    start = 0
    stop = 5
    update = input("To view five rows of the data enter yes or no: ")
    while(update == 'yes'):
        print(df.iloc[start:stop])
        start += 5
        stop += 5
        update = input(" Do you wish to continue? enter yes or no: ")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        row_view(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

"""to help with the code i used various sites which include"""
#geeks for geeks
#stackoverflow
