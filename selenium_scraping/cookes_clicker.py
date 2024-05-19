'''
This Python script uses Selenium to automate playing the Cookie Clicker game 
available at "https://orteil.dashnet.org/cookieclicker/". 
It automatically clicks the cookie and purchases upgrades when they become available.

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

URL = "https://orteil.dashnet.org/cookieclicker/"
is_on = True

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Click the Consent button
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]"))).click()

# Click on language option
driver.implicitly_wait(2)
language_button_english = driver.find_element(By.XPATH, "//*[@id='langSelect-EN']")
language_button_english.click()


driver.implicitly_wait(2)
# Cookie button
cookie_button = driver.find_element(By.ID, "bigCookie")
number_of_cookies = int(driver.find_element(By.ID, "cookies").text.split()[0])


def check_upgrades():
    upgrades = driver.find_elements(By.CSS_SELECTOR, value="#store>div:not(.grayed)")
    upgrades[-1].click()

 
try:
    while True:
        cookie_button.click()
        # every 5 seconds
        if int(time.time()) % 5 == 0 and number_of_cookies > 15:
            check_upgrades()

except KeyboardInterrupt:
    print("\n[-] Detected CTRL + C ...............")
    print("[-] Quitting.")