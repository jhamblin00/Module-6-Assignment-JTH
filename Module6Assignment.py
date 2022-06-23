#Module 6 Assignment

#The purpose of this assignmnet is to corect aspects from four bits of code.

#Code 1

import sys
for line in sys.stdin:
    data = line.strip().split('\t')
   if len(data) == 6:
        data = date, time, store, item, cost, payment = data
    print('{0}\t{1}'.format(item, cost))

#Code 2

from datetime import datetime
from datetime import timedelta
print(datetime.now() + timedelta(days=1))
print(datetime.now() - timedelta(seconds=60))
print(datetime.now() + timedelta(days=730))
  
#Code 3

from datetime import datetime
from datetime import timedelta
d = timedelta(microseconds=-1)
print(d.days,d.seconds,d.microseconds)
g = timedelta(minutes=144613)
print(g.days,g.seconds)

#Code 4

datetime_object = datetime.now()
def heightandtime(x,y,z):
    print('The height is ',x,' feet and ',y,' inches.')
    print(z)
x=input('Enter Feet - ')
y=input('Enter Inches - ')
heightandtime(x,y,datetime_object)
