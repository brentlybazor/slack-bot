import dotenv
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from functions import *
from pathlib import Path
import random

env_path = Path('.') / '.env.local'
dotenv.load_dotenv(dotenv_path=env_path)
dotenv.load_dotenv()

PATH = os.getenv("webdriverPath")

chrome_options = Options()  
chrome_options.add_argument("--log-level=3") 

page = os.getenv("page")
email = os.getenv("email")
domainName = os.getenv("domainName")
password = os.getenv("password")

with open('messages.txt') as my_file:
    thingsToType = my_file.readlines()

def forceRun():
    if '-force' in sys.argv:
        return True
    
    return False

def determineHeadless():
    if '-hl' in sys.argv:
        chrome_options.add_argument("--headless") 
        chrome_options.add_argument("--disable-gpu") 
        chrome_options.add_argument("--window-size=1920,1200")
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

def navigateToPage(page):    
    # opens the desired page in the browser and waits for some time before continuing
    driver.get(page)
    time.sleep(2)

def enterDomain():
    # enters the domain name associated with slack and submits the name in the form
    domainInput = driver.find_element_by_name('domain')
    domainInput.send_keys(domainName)
    domainInput.send_keys(Keys.RETURN)
    time.sleep(2)

def fillOutLogin():
    # fills our email and password on the login screen and presses enter
    emailInput = driver.find_elements_by_xpath('//*[@id="email"]')[0]
    emailInput.send_keys(email)

    passwordInput = driver.find_elements_by_xpath('//*[@id="password"]')[0]
    passwordInput.send_keys(password)
    passwordInput.send_keys(Keys.RETURN)
    time.sleep(2)

def clearPopup():
    popupButton = driver.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/div/button')
    if popupButton:
        popupButton[0].click()
        time.sleep(2)

def getTextToType():
    # gets random text to type from the array above 
    return thingsToType[random.randrange(len(thingsToType))].rstrip('\n')

def simulateTypeMessage(textToType, textInput):
    # loops through each letter in the string and simulates typing
    typeIndex = 0
    while typeIndex < len(textToType):
        textInput.send_keys(textToType[typeIndex])
        time.sleep(.25)
        typeIndex += 1
    time.sleep(2)

def simulateDeleteMessage(textInput):
    # loops through each letter in the string and simulates deleting text
    if len(textInput.text) > 0:
        while len(textInput.text) > 0:
            textInput.send_keys(Keys.BACK_SPACE)
            time.sleep(.25)

def simulateBeingBusy():
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



def typeMessageSequence():
    
    textInputXPath = '/html/body/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]'
    textInput = driver.find_elements_by_xpath(textInputXPath)[0]
    textInput.click()

    textToType = getTextToType()
        
    simulateTypeMessage(textToType, textInput)

    simulateDeleteMessage(textInput)

    simulateBeingBusy()

def downTimeSequence():
    # creates a countdown time for 25 mins and then runs the program again
    secondsToSleep = 25 * 60
    while int(secondsToSleep) > 0:
        print("not currently working hours. trying again in " + convertSeconds(secondsToSleep), end='\r')
        time.sleep(1)
        secondsToSleep -= 1


# set the driver to false
driver = False
# continues indefinately until the program is manually stopped
while True:
    # checks to see if they program should run based on the working hours
    if forceRun() or workingHours():
        # check to see if the driver or browers is already set (it initializes after the first load)
        # this check prevents multiple browser windows from opening when the program loops
        if not driver:
            determineHeadless()
            driver = webdriver.Chrome(PATH, options=chrome_options)
            navigateToPage(page)
            enterDomain()
            fillOutLogin()

        else:
            # opens the desired page in the browser and waits for some time before continuing
            navigateToPage(page)

        clearPopup()

        typeMessageSequence()

    else:
        downTimeSequence()
