# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar
from datetime import date

d,m,y = map(int, input().split())

day = calendar.day_name[date(y, d, m).weekday()]

print(day.upper())