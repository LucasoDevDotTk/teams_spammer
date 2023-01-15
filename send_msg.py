"""
All code in this file is licensed under the MIT License, the whole license and copyright holder(s) is in ./LICENSE.
You shall follow all the terms of the MIT License (./LICENSE).
"""


# ----- Requires: selenium == 4.7.2 -----
# ----- Requires: webdriver-manager == 3.8.5 -----

from time import sleep

# Import all selenium and webdriver tools
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from lib import login

microsoft_authentication_link = "https://go.microsoft.com/fwlink/p/?linkid=873020"
email = input("Email: ")
password = input("Password: ")
message = input("Please enter spam message: ")
count = int(input("How many times: "))
user_nr = input("Which user (nr. 1 from top): ")

# driver = webdriver.Chrome(ChromeDriverManager().install())

# driver.get(microsoft_authentication_link)

driver = login.login(email, password, microsoft_authentication_link)

sleep(6)

click_chat = driver.find_element_by_css_selector(".icons-chat")
click_chat.click()

sleep(2)

click_user = driver.find_element_by_css_selector(f"div:nth-child({user_nr}) > .recipient-group-list-item .cle-title > .single-line-truncation")
click_user.click()

sleep(2)


WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe.embedded-electron-webview.embedded-page-content")))

for i in range(count):
    driver.execute_script(f'document.querySelector(".ck-placeholder").innerHTML = "{message}";')
    send = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[6]/div/div/div[2]/div/div[4]/div[2]/div[3]/button")
    send.click()
    sleep(0.5)

print("Done with the spam")


driver.close()
driver.quit()
