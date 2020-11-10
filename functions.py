import datetime
import time

def workingHours():
    currentDate= datetime.datetime.today()
    currentDay = currentDate.weekday()
    currentHour = currentDate.hour

    if currentDay > 4:
        return False
    
    if currentHour > 18 or currentHour < 8:
        return False

    return True

def convertSeconds(seconds): 
    return time.strftime("%H:%M:%S", time.gmtime(seconds))
