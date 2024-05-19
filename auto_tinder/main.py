'''
This script uses Selenium to automate the Tinder web app by logging in 
with Google credentials and performing "like" actions on profiles.

Prerequisites:

    Python 3.x
    Google Chrome browser
    ChromeDriver (compatible with your version of Chrome)


Usage:
1. Change USERNAM and PASSWORD constants
2. $ python3 main.py    

'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

URL = "https://tinder.com/app/explore"
USERNAME = "*******"
PASSWORD = "*******"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

main_page = driver.current_window_handle

######################## PREPARATION ########################

# Click Accept button
driver.implicitly_wait(2)
click_accept = driver.find_element(By.XPATH, "//*[@id='t2067052097']/div/div[2]/div/div/div[1]/div[1]/button").click()

# Click Login
driver.implicitly_wait(5)
click_login= (driver.find_element(By.XPATH, '//*[text()="Log in"]')).click()

# Click Sign up with Google
driver.implicitly_wait(7)
click_google = (driver.find_element(By.XPATH, '//*[text()="Weiter mit Google"]')).click()
#click_google = (driver.find_element(By.XPATH,"//*[@id='container']/div/div[1]")).click()

driver.implicitly_wait(10)

# changing to the pop-up window
for handle in driver.window_handles:
    if handle != main_page:
        login_page = handle
              
driver.switch_to.window(login_page)

# Input Google user date in pop-window
driver.implicitly_wait(10)
input_name = driver.find_element(By.XPATH, "//*[@id='identifierId']").send_keys(USERNAME)
click_next = driver.find_element(By.XPATH, value='//*[text()="Next"]').click()
sleep(3)
input_password = driver.find_element(By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input").send_keys(PASSWORD)
sleep(3)
click_next = driver.find_element(By.XPATH, value='//*[text()="Next"]').click()
sleep(3)

# back to main page
driver.switch_to.window(main_page)

# Click Allow set your location
driver.implicitly_wait(3)
click_allow = driver.find_element(By.XPATH, value='//*[text()="Allow"]').click()
sleep(5)
click_allow = driver.find_element(By.XPATH, value="//*[@id='t338671021']/div/div/div/div/div[3]/button[2]").click()
sleep(5)
#click_cancel = driver.find_element(By.XPATH, "//*[@id='t338671021']/div/div[2]/div[2]/button").click()
#sleep(5)

######################## MAIN LOOP ########################

for n in range(100):

    sleep(3)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH, value='//*[@id="t2067052097"]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[4]/button/span/span/svg/path').click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(3)