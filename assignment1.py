#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py 
The python code in this file is original work written by
Sean Ryan Rivera. No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Author: Sean Ryan Rivera
Semester: Fall 2024
Description: This program adds or subtracts from a date given by the user.
'''

import sys

def day_of_week(date: str) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    day, month, year = (int(x) for x in date.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7
    return days[num]

def leap_year(year: int) -> bool:
    "return true if the year is a leap year"
    leap_flag = False
    
    lyear = year % 4
    if lyear == 0:
        leap_flag = True
    
    lyear = year % 100
    if lyear == 0:
        leap_flag = False
        
    lyear = year % 400
    if lyear == 0:
        leap_flag = True
        
    return leap_flag

def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    mon_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    
    if month == 2 and leap_year(year):
        return 29
    else:
        return mon_dict[month]

def after(date: str) -> str: 
    '''
    after() -> date for next day in DD/MM/YYYY string format

    Return the date for the next day of the given date in DD/MM/YYYY format.
    This function has been tested to work for year after 1582
    '''
    day, mon, year = (int(x) for x in date.split('/'))
    day += 1  # next day

    lyear = year % 4
    if lyear == 0:
        leap_flag = True
    else:
        leap_flag = False  # this is not a leap year

    lyear = year % 100
    if lyear == 0:
        leap_flag = False  # this is not a leap year

    lyear = year % 400
    if lyear == 0:
        leap_flag = True  # this is a leap year
    
    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if mon == 2 and leap_flag:
        mon_max = 29
    else:
        mon_max = mon_dict[mon]
    
    if day > mon_max:
        mon += 1
        if mon > 12:
            year += 1
            mon = 1
        day = 1  # if tmp_day > this month's max, reset to 1 
    return f"{day:02}/{mon:02}/{year}"

def before(date: str) -> str:
    "Returns previous day's date as DD/MM/YYYY"
    day, mon, year = (int(x) for x in date.split('/'))
    day = day - 1
    
    if day < 1:
        # Moves to previous month or year
        mon = mon - 1
        if mon < 1:
            mon = 12
            year = year - 1
            
        # Leap year check
        lyear = year % 4
        if lyear == 0:
            leap_flag = True
        else:
            leap_flag = False  # this is not a leap year
        lyear = year % 100
        if lyear == 0:
            leap_flag = False  # this is not a leap year
        lyear = year % 400
        if lyear == 0:
            leap_flag = True  # this is a leap year
            
        # Retrieve the max days for the month
        mon_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        if mon == 2 and leap_flag:
            mon_max = 29
        else:
            mon_max = mon_dict[mon]
            
        day = mon_max  # Set to last day of previous month
        
    return f"{day:02}/{mon:02}/{year}"

def usage():
    "Print a usage message to the user"
    print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY NN")
    sys.exit()

def valid_date(date: str) -> bool:
    "check validity of date"
    day, mon, year = (int(x) for x in date.split('/'))
        
    # Check if date is valid
    if year < 1582 or mon < 1 or mon > 12 or day < 1:
        return False
        
    # Check day if valid for the month
    elif day <= mon_max(mon, year):
        return True

def day_iter(start_date: str, num: int) -> str:
    "iterates from start date by num to return end date in DD/MM/YYYY"
    current_date = start_date
    count = num
    
    if num > 0:
        while count > 0:
            current_date = after(current_date)
            count = count - 1
    else:
        while count < 0:
            current_date = before(current_date)
            count = count + 1
            
    return current_date
    
if __name__ == "__main__":
    # check length of arguments
    if len(sys.argv) != 3:
        usage()
    
    # check first arg is a valid date
    if not valid_date(sys.argv[1]):
        usage()
    
    # check that second arg is a valid number (+/-)
    try:
        num = int(sys.argv[2])
    except ValueError:
        usage()
    
    # call day_iter function to get end date, save to x
    x = day_iter(sys.argv[1], num)
    
    # print(f'The end date is {day_of_week(x)}, {x}.')
    print(f'The end date is {day_of_week(x)}, {x}.')