from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=options)


driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

print("----------------------------------------------------------------------------------")
name = str(input('Enter Group/Contanct Name: '))
msg = str(input('Enter message: '))
count = int(input('Enter the count: '))

# Scan the code before proceeding further
input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_xpath(
    "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")

for i in range(count):
    msg_box.send_keys(msg)
    # should replace the button's parent
    driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]").click()
