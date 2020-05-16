NAME  
tesco.py  
  
REQUIRED MODULES  
you will need to install python: https://www.python.org/downloads/  
we will need these modules: selenium, requests  
install the modules using this command in the shell: pip install modulename  
e.g. pip install selenium  
  
WEBDRIVER  
the bot uses the chrome webdriver to automate the process  
find your chrome version by entering this url in the browser: chrome://version/  
download the relevant webdriver here: https://chromedriver.chromium.org/downloads  
the webdriver must be in a folder that's in the system path  
to do this on windows, run this command: set PATH=%PATH%;C:\insert\directory\here\  
  
ACCOUNT DETAILS  
open the code using a text editor
enter your tesco username in this line: username.send_keys("ADD USERNAME HERE")  
enter your tesco password in this line: password.send_keys("ADD PASSWORD HERE")  
  
NOTIFICATIONS  
we will send notifications to your phone using ifttt  
sign up for ifttt here, or use the app: ifttt.com      
create an applet here, or use the app: https://ifttt.com/create    
click on the big THIS button  
choose the “webhooks” service and select the “Receive a web request” trigger  
name the event tesco  
click on the big THAT button, select the “Notifications” service and select the “Send a rich notification from the IFTTT app” action  
give it a title, like “Tesco slots available!”  
set the message to "Slots available in week ${{Value1}  
optionally you can add a link url to the tesco website: https://www.tesco.com/groceries/en-GB/slots/delivery  
create the action and finish setting up the applet  
go to this page, log in if necessary, and click on the “Documentation” button in the top right corner: https://ifttt.com/maker_webhooks  
the documentation page contains the webhook URL and it looks like this: https://maker.ifttt.com/trigger/{event}/with/key/{your-IFTTT-key}  
replace the {event} with tesco  
replace the url in this line of code with your own url: richtrigger = 'https://maker.ifttt.com/trigger/tesco/with/key/{your-IFTTT-key}'  
make sure you have the ifttt app on your phone and that you're logged in, so that you can receive notifications  
  
the bot should now be ready, enjoy  
