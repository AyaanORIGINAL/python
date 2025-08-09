import random
import time

def getrandomdate(startDate, endDate):
    print('Printing random date between', startDate, 'and', endDate)

    randomGenerator = random.random()
    dateformat = "%d/%m/%Y"

    starttime =time.mktime(time.strptime(startDate, dateformat))
    endtime = time.mktime(time.strptime(endDate, dateformat))

    randomtime = starttime + randomGenerator * (endtime - starttime)
    randomdate = time.strftime(dateformat, time.localtime(randomtime))
    return randomdate

print('Random date is:', getrandomdate('1/1/1980', '9/8/2025'))