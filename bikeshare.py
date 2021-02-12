import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


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
      city = input("which city would you like to filter by ? \n New York City? Chicago ? Washignton ? ").lower()
      if city not in ('new york city', 'chicago', 'washington'):
        print("sorry, I didn't catch that. Try again.")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month = input("Which month would you like to filter by? all, January, February, March, April, May, June? ").title()
      if month not in ('All', 'January', 'February', 'March', 'April', 'May', 'June'):
        print("sorry, I didn't catch that. Try again.")
        continue
      else:
        break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("Which Day would you like to filter by? All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday? ").title()
      if day not in ('All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'):
        print("sorry, I didn't catch that. Try again.")
        continue
      else:
        break

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
    #dataframe
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        df = df[df['month'] == month ]

    if day != 'All':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_status(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("Most common month:", popular_month)
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("Most common day:", popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("Most common hour:", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print("Most common used start station is: ", Start_Station)

    # TO DO: display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print("Most common used end station is: ", End_Station)


    # TO DO: display most frequent combination of start station and end station trip
    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print("Most common used combination station of start and end station is: ", Start_Station, " & ", End_Station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = sum(df['Trip Duration'])
    print("Total travel time:", Total_Travel_Time/86400, " days.")

    # TO DO: display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print("Mean travel time:", Mean_Travel_Time/60, " minutes.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User types: ", user_types)

    # TO DO: Display counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print("Gender types: ", gender_types)
    except KeyError:
      print("Gender Types: No data for this month")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      Earlist_Year = df['Birth Year'].min()
      print("Earlist year: ", Earlist_Year)
    except KeyError:
      print("Earlist year: No data for this month")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print("Most recent year: ", Most_Recent_Year)
    except KeyError:
      print("Most recent year: No data for this month")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print("Most common Year: ", Most_Common_Year)
    except KeyError:
      print("Most common year: No data for this month")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def ask_view(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while (view_data != 'no'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input("Do you wish to continue ?: ").lower()
        if view_display != 'yes':
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_status(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        ask_view(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
