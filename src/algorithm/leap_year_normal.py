# Write code to determine leap year
# 1. Years in which the year is divisible by 4 are (in principle) leap years.
# 2. However, the year in which the year is divisible by 100 is (in principle) a normal year.
# 3. However, the year in which the year is divisible by 400 is always a leap year.

def is_leap_year(year):
    if(year % 400 == 0):
        return True
    elif(year % 100 == 0):
        return False
    elif(year % 4 == 0):
        return True
    
    return False

