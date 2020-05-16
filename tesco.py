from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep
import requests
import sys

# 0 Set global variables
noslots = 'No slots available! Try another day'
minutes = 1
sleeptime = 10
i = 1
# ENTER IFTTT TRIGGER URL HERE
richtrigger = 'https://maker.ifttt.com/trigger/tesco/with/key/{your-IFTTT-key}'
weeknumber = {'value1': float(1)}

if richtrigger == 'https://maker.ifttt.com/trigger/tesco/with/key/{your-IFTTT-key}':
    print("Program is not set up. Refer to the README file.")
    sleep(5)
    sys.exit()

# 1 Open browser and go to login
driver = webdriver.Chrome()
driver.get('https://secure.tesco.com/account/en-GB/login')
sleep(sleeptime)

# 1.1 Enter username, password, and press log in
username = driver.find_element_by_name('username')
# ADD YOUR USERNAME HERE
username.send_keys("ADD USERNAME HERE")
password = driver.find_element_by_name('password')
# ADD YOUR PASSWORD HERE
password.send_keys("ADD PASSWORD HERE")
login = driver.find_element_by_xpath('//button[@class="ui-component__button"]')
login.click()
sleep(sleeptime)

# 2 Start loop
while True:

    # 2.1 Once logged in, go to the delivery page
    driver.get('https://www.tesco.com/groceries/en-GB/slots/delivery')
    sleep(sleeptime)

    # 2.2 Get a list of all the week tabs as elements
    try:
        weeks = driver.find_elements_by_class_name('slot-selector--week-tabheader-link')

        # 2.3 Iterate through each of the tabs
        for week in weeks:
            try:
                week.click()
            except ElementClickInterceptedException:
                sleep(sleeptime)
                week.click()

            sleep(sleeptime)

            try:
                # 2.4 Find the info message, and print the text to the console
                status = driver.find_element_by_class_name('info-message')
                text = str(status.get_property("textContent"))
                print(i, text)

                # 2.5 If the info message doesn't say there are no slots, then send notification 
                if text != noslots:
                    requests.post(richtrigger, json=weeknumber)
                    sleep(sleeptime)
            
            # 2.6 If no info message element is found, then send notification
            except NoSuchElementException:
                requests.post(richtrigger, json=weeknumber)
            i += 1
            weeknumber["value1"] += 1
    
    # 2.7 If no week tab elements found, then return notification
    except NoSuchElementException:
        print("Week tabs not found")

    except:
        print("An unknown error occurred")
        
    # 2.8 Reset week counter to 1
    weeknumber["value1"] = float(1)

    # 2.9 Sleep for some minutes before restarting
    sleep(60 * minutes)