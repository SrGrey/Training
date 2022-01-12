'''
Script for to know data after N days

Input start data as YYYY MM DD press Enter,
Input days, print Enter

Script will return new data
'''

import datetime as dt
from time import strptime, strftime

start_date = dt.datetime.strptime(input(), "%Y %m %d")
print(actual_date)
days = dt.timedelta(int(input()))
print(days)
new_date = start_date + days
print(new_date.strftime("%Y %#m %#d"))
