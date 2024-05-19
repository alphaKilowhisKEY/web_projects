'''

This script automates the process of logging into Instagram, navigating to a specified account's followers, 
and attempting to follow those followers using Selenium.

'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep


INSTA_ACCOUNT = "INSTAGRAM ACCOUNT YOU WANT TO BECOME"
INSTA_USERNAME = "*****"
INSTA_PASSWORD = "************"
INSTA_URL = "https://instagram.com"
INSTA_URL_LOGIN = "https://www.instagram.com/accounts/login/"

class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)


    def login(self):
        self.driver.get(INSTA_URL_LOGIN)
        sleep(3)
        self.driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(INSTA_USERNAME)
        password = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(INSTA_PASSWORD)
        sleep(2)
        password.send_keys(Keys.ENTER)

        # Click "not now" on notifications prompt
        notifications_prompt = self.driver.find_element(by=By.XPATH, value="// button[contains(text(), 'Not Now')]")
        if notifications_prompt:
            notifications_prompt.click()

    def find_followers(self): 
        sleep(5)
        self.driver.get(f"https://www.instagram.com/{INSTA_ACCOUNT}/followers")
        sleep(8)
        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):

        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click() 


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()    