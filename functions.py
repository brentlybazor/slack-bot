import datetime
import time

def workingHours():
    currentDate= datetime.datetime.today()
    currentDay = currentDate.weekday()
    currentHour = currentDate.hour
    currentMinute = currentDate.minute

    if currentDay > 4:
        return False
    
    if currentHour >= 17 or currentHour < 8:
        return False

    if currentDay == 4 and currentHour >= 16:
        return False

    return True

def convertSeconds(seconds): 
    return time.strftime("%H:%M:%S", time.gmtime(seconds))
