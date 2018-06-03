# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 13:16:05 2018

@author: soviv
"""
#project1
import datetime 

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month
      
    Returns:
      The number of days in the input month
    """
    date1= datetime.datetime(year,month,1)
    
    if month!=12:
        date2= datetime.datetime(year,month+1,1)
    else:
        date2= datetime.datetime(year+1,1,1)
    
    timedelta= date2 - date1
    return timedelta.days


#problem2Checking if a date is valid
def is_valid_date(year,month,day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day
      
    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    isValidDate= True
    try:
        datetime.datetime(int(year), 
                          int(month), int(day))
    except ValueError :
            print ("False")
            isValidDate = False
        
    if(isValidDate):
            return ("True")
    else :
            return ("False")

#problem3Checking if a date is valid
"""
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date
      
    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is 
      before the first date.
    """
def days_between(year1, month1, day1, year2, month2, day2):

    try:
        date3= datetime.datetime(year1,month1,day1)
        date4= datetime.datetime(year2,month2,day2)
        if date3 < date4:
            return date4-date3    
        else:
            return 0    
    except ValueError:
        return 0
    
#project4 Calculating a person's age in days
def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day
      
    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid of if the input
      date is in the future.
    """
    try:
        birthday=datetime.datetime(year,month,day)
        date5=datetime.datetime.today()
        if birthday <date5:
            return date5-birthday
        else:
            return 0
    except ValueError:
        return 0


