"""
All code in this file is licensed under the MIT License, the whole license and copyright holder(s) is in ./LICENSE.
You shall follow all the terms of the MIT License (./LICENSE).
"""


# ----- Requires: selenium == 4.7.2 -----
# ----- Requires: webdriver-manager == 3.8.5 -----

from time import sleep
from getpass import getpass


# Import all selenium and webdriver tools
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from lib import login
from lib import time_now
from lib import start

# Global Variables
microsoft_authentication_link = "https://go.microsoft.com/fwlink/p/?linkid=873020"
email = input(f"{time_now.time_now()} Email: ")
password = getpass(f"{time_now.time_now()} Password: ")
usr_message = input(f"{time_now.time_now()} Please enter spam message: ")
count = int(input(f"{time_now.time_now()} How many times to spam: "))
between = float(input(f"{time_now.time_now()} How many seconds between every spam message: "))
user_nr = input(f"{time_now.time_now()} Which user (nr. 1 from top): ")

# Chrome Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

print(f"{time_now.time_now()} Logging in with {email}")

driver = login.login(email, password, microsoft_authentication_link, chrome_options)
sleep(8)

# Going into chat
click_chat = driver.find_element_by_css_selector(".icons-chat")
click_chat.click()
sleep(2)

# Going into user
click_user = driver.find_element_by_css_selector(f"div:nth-child({user_nr}) > .recipient-group-list-item .cle-title > .single-line-truncation")
click_user.click()

user = click_user.text
print(f"{time_now.time_now()} User found: {user}")

sleep(2)

# Going into iframe of chat frame
WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe.embedded-electron-webview.embedded-page-content")))

# Spamming
for i in range(count):
    # message = f"{time_now.time_now()} {usr_message}"
    message = usr_message
    driver.execute_script(f'document.querySelector(".ck-placeholder").innerHTML = "{message}";')
    sleep(0.3)
    send = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[6]/div/div/div[2]/div/div[4]/div[2]/div[3]/button")
    send.click()
    print(f"{time_now.time_now()} Spammed {user} with {message}")
    sleep(between)

print(f"{time_now.time_now()} Done with the spam")


driver.close()
driver.quit()
