"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

#get today's info for when nothing is inputed
#today = datetime.today()
#year = datetime.now().year
#month = datetime.now().month
#print("The month is: ", str(month))

def calendarMaker():
  today = datetime.today()
  year = today.year
  month = today.month
  print("The month is: ", str(month))

#Inputs
month_input = input("Please enter the month: ex: 4: ")
year_input = input("Please enter a year: ex 1999: ")
print(month_input, year_input)

#Conditionals to print calendar
if len(month_input) > 0 and len(month_input) <= 2 and month_input.isdigit():
  month = int(month_input)

if len(year_input) > 0 and len(year_input) <=4 and year_input.isdigit():
  year = int(year_input)

if len(month_input) == 0 and len(year_input) == 0:
  year = datetime.today().year
  month = datetime.today().month

if len(month_input) > 0 and len(year_input) == 0:
  month = int(month_input)
  year = datetime.today().year

else:
  print("please enter 2 digit month and 4 digit year")

print(calendar.month(year, month))

calendarMaker()