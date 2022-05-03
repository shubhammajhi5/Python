# entering the required date
dob = '23/08/1996'
date, month, year = map(int, dob.split('/'))

# creating list of all leap years in the 20th century
all_leap_years = [i for i in range(1901,2001) if i%4 == 0]

# creating the month keys for the 20th century
month_key = {1:1, 2:4, 3:4, 4:0, 5:2, 6:5, 7:0, 8:3, 9:6, 10:1, 11:4, 12:6}

# creating the days keys
day_key = {0:'Saturday', 1:'Sunday', 2:'Monday', 3:'Tuesday', 4:'Wednesday', 5:'Thursday', 6:'Friday'}


# function to return the list of all leap years uptill the given year
def leap_years_list(x):
  if x <= year:
    return True
  else:
    return False

# counting the total no of leap years uptill the given year
no_of_leap_years = len(list(filter(leap_years_list, all_leap_years)))


# creating a function to get the last two digit of a year
def get_last_two_digit(year):
    if year == 2000:
        return 100
    else:
        return year % 100

# getting the last two digit of a year
year_last_two_digit = get_last_two_digit(year)

# getting the final value to compare with the corresponding day_key
val = (year_last_two_digit + no_of_leap_years + month_key[month] + date) % 7


if year in all_leap_years and month in (1, 2):
    print(f'The day on {dob} was : {day_key[val - 1]}')
else:
    print(f'The day on {dob} was : {day_key[val]}')
