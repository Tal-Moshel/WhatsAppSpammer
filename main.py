# region imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
import atexit
# endregion

# Initialises driver object with properties(options)
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(
    ChromeDriverManager().install(), options=options)


# Loads whatsapp-web to the window and waits
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

# Scan the code before proceeding further
input('Enter anything after scanning QR code')

runProgram = True
while (runProgram):
    # Asks for the contact name
    nameExists = False
    user = ""
    while(nameExists == False):
        name = str(input('Enter Group/Contanct Name: '))
        try:
            user = driver.find_element_by_xpath(
                ' /html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div//span[@title = "{}"]'.format(name))
            # driver.switch_to.frame(user)
            nameExists = True
        except:
            nameExists = False

    # Asks for the contact message and count
    msg = str(input('Enter message: '))
    count = int(input('Enter the count: '))
    delay = float(input('Enter the delay between every message: '))

    # Clicks on the selected user
    # user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    # Variable for the message box
    msg_box = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")

    # Executes the amount of times specified in the COUNT variable
    for i in range(count):
        # Types the message to send
        msg_box.send_keys(msg)
        # Clicks the send button
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]").click()
        if(delay > 0):
            time.sleep(delay)
