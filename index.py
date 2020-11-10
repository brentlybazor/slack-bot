import dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from functions import *
from pathlib import Path
import random

dotenv.load_dotenv()
env_path = Path('.') / '.env.local'
dotenv.load_dotenv(dotenv_path=env_path)

PATH = os.getenv("webdriverPath")

page = os.getenv("page")
email = os.getenv("email")
domainName = os.getenv("domainName")
password = os.getenv("password")

thingsToType = [
    "This is a message", 
    "Pretending to type", 
    "Hi there, I a busy typing on slack", 
]

# set the driver to false
driver = False
# continues indefinately until the program is manually stopped
while True:
    # checks to see if they program should run based on the working hours
    if workingHours():
        # check to see if the driver or browers is already set (it initializes after the first load)
        # this check prevents multiple browser windows from opening when the program loops
        if not driver:
            # sets the driver to a chrome page
            driver = webdriver.Chrome(PATH)

            # opens the desired page in the browser and waits for some time before continuing
            driver.get(page)
            time.sleep(2)

            # enters the domain name associated with slack and submits the name in the form
            domainInput = driver.find_element_by_name('domain')
            domainInput.send_keys(domainName)
            domainInput.send_keys(Keys.RETURN)
            time.sleep(2)

            # fills our email and password on the login screen and presses enter
            emailInput = driver.find_elements_by_xpath('//*[@id="email"]')[0]
            emailInput.send_keys(email)

            passwordInput = driver.find_elements_by_xpath('//*[@id="password"]')[0]
            passwordInput.send_keys(password)
            passwordInput.send_keys(Keys.RETURN)
            time.sleep(2)
        else:
            # opens the desired page in the browser and waits for some time before continuing
            driver.get(page)
            time.sleep(2)


        # finds the field for the chat box and clicks it to enable typing
        textInput = driver.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]')[0]
        textInput.click()
        
        # gets random text to type from the array above 
        textToType = thingsToType[random.randrange(len(thingsToType))]

        # loops through each letter in the string and simulates typing
        typeIndex = 0
        while typeIndex < len(textToType):
            textInput.send_keys(textToType[typeIndex])
            time.sleep(.25)
            typeIndex += 1

        time.sleep(2)

        # loops through each letter in the string and simulates deleting text
        while len(textInput.text) > 0:
            textInput.send_keys(Keys.BACK_SPACE)
            time.sleep(.25)

        # creates a randome number of mins (up to 15 mins) to wait before running the program again
        secondsToSleep = random.randrange(15) * 60
        # this loop run for every second in secondsToSleep and displays a countdown timer in the console
        # if time has not expired display the timer
        while int(secondsToSleep) > 0:
            if int(secondsToSleep) != 0:
                print(convertSeconds(secondsToSleep) + ' until next try\t\t\t\t', end="\r")
                time.sleep(1)
                # set the time to decrement by 1  
                secondsToSleep -= 1
            
            # the secondsToSleep decrement above so this can check if they countdown is expired
            # if expired, the text changed to currently running and then restarts the program
            if int(secondsToSleep) == 0:
                print('currently running\t\t\t\t', end='\r')

    else:
        # creates a countdown time for 25 mins and then runs the program again
        secondsToSleep = 25 * 60
        while int(secondsToSleep) > 0:
            print("not currently working hours. trying again in " + convertSeconds(secondsToSleep), end='\r')
            time.sleep(1)
            secondsToSleep -= 1
