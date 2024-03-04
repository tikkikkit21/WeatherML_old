from datetime import datetime

def percent(num):
    return format(num, '.2%')

def time_to_int(timeString):
    timeObj = datetime.strptime(timeString, '%H:%M').time()
    timeInt = timeObj.hour * 60 + timeObj.minute
    return timeInt
