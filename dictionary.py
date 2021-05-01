import calendar
import datetime
from datetime import date

def solution(D):
    inputDictionary = {'Mon':0, 'Tue':0, 'Wed':0,'Thu':0, 'Fri':0,'Sat':0, 'Sun':0}
    days =['Mon', 'Tue', 'Wed', 'Thu','Fri', 'Sat', 'Sun']
    for value in D:
        date = value
        yyyy,mm,dd = (int(i) for i in date.split('-'))
        dayVal = calendar.weekday(yyyy, mm, dd)
        inputDictionary[days[dayVal]]+=D[value]
    print(inputDictionary)

#this is the first test case
#D = {'2020-01-01':4,'2020-01-02':4,'2020-01-03':6,'2020-01-04':8,'2020-01-05':2,'2020-01-06':-6,'2020-01-07':2,'2020-01-08':-2}

#this is the second case .. Couldn't sort the dictionary for mean when the data is missing
D = {'2020-01-01':6,'2020-01-04':12,'2020-01-05':14,'2020-01-06':2,'2020-01-07':4}

solution(D)
