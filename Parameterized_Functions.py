'''
The program will take three arguments(a year, a month, and day of the month)
and return the corresponding day of the year or return none 
if any of the argument is invalid.
'''

def is_leap_year(year):
    # checking if the year is divisible by 4
    if year % 4 != 0:
        return False 
    # checking if the year is divisible by 400
    if year % 400 != 0:
        return True
    # checking if the year is divisible by 100
    if year % 100 != 0:
        return False
    else:
        return True


def days_in_month(year, month):
    # number of days in each month
    days_month=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # checking a month if it february and if it is a leap year 
    if month == 2 and is_leap_year (year):
        return 29
    elif 1 <= month <= 12:
        return days_month [month - 1]
    else:
        return None

def day_of_year(year, month, day):
    # checking if the month is valid
    if month < 1 or month > 12:
        return None
    # checking if the day is valid for the month
    day_in_this_month = days_in_month(year, month)
    if day <1 or day > day_in_this_month:
        return None
    
    # calculation of the da of the year
    total_days = 0
    for i in range(1, month):
        total_days += days_in_month(year, i)
    total_days += day
    
    return total_days

# couple of Test Cases
test_cases = [
    (2023, 1, 1, 1),
    (2023, 12, 31, 365),
    (2020, 2, 29, 60),  # Leap year
    (2019, 3, 1, 60),
    (2023, 6, 15, 166),
    (2023, 2, 29, None),  # Invalid date
    (2023, 0, 10, None),  # Invalid month
    (2023, 13, 10, None)  # Invalid month
]

for year, month, day, expected in test_cases:
    result = day_of_year(year, month, day)
    print(f"Year: {year}, Month: {month}, Day: {day}, Expected {expected}, Result: {result}")
    assert result == expected, f'Test Failed for {year}-{month}-{day}'