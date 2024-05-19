'''
This script is a Python automation tool that uses Selenium to:

- Check Internet Speed: It navigates to the Speedtest website, initiates a speed test, and retrieves the download speed.
- Post on Twitter: If the download speed is lower than the promised speed by the Internet Service Provider (ISP),
 it logs into Twitter and posts a tweet to complain about the slow speed.

 Usage:
 Replace Constants by your data
 $ python3 main.py
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Internet Service Provider promised speed, Mbps
ISP_SPEED_DOWN = 150
ISP_SPEED_UP = 10

# Constants
ISP_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com"
TWITTER_EMAIL = "*******"
TWITTER_PASSWORD = "*******"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(ISP_URL)
        sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="onetrust-accept-btn-handler"]').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
        sleep(60)

        # try:
        #     wait = WebDriverWait(self.driver, 10)
        #     download_speed_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')))
        #     download_speed = download_speed_element.text

        #     if download_speed == "-":
        #         wait.until(lambda driver: download_speed_element.text != "-")
        #         download_speed = download_speed_element.text
        #     print(f"Download speed: {download_speed}")

        # finally:
        #     self.driver.quit()

        download_speed_element = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.down = float(download_speed_element.text)
        print(f"[+]Download speed: {self.down}")
        #self.driver.quit()
        return self.down


    def tweet_it(self, speed):
        self.driver.get(TWITTER_URL)
        main_page = self.driver.current_window_handle

        # Click Accept button
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[text()="Accept all cookies"]').click()

        # Click Sign up with Google
        sleep(5)
        (self.driver.find_element(By.XPATH, '//*[text()="Sign up with Google"]')).click()
        (self.driver.find_element(By.XPATH, '//*[text()="Mit Google anmelden"]')).click()
        sleep(5)

        # Changing to the pop-up window
        for handle in self.driver.window_handles:
            if handle != main_page:
                login_page = handle
                    
        self.driver.switch_to.window(login_page)

        # Input Google user date in pop-window
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(TWITTER_EMAIL)
        self.driver.find_element(By.XPATH, value='//*[text()="Next"]').click()
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(TWITTER_PASSWORD)
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[text()="Next"]').click()
        sleep(3)

        # Back to main page
        self.driver.switch_to.window(main_page)
        sleep(3)
        body = f"I was promised 150Mbps download. I have: {speed}."
        self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div').send_keys(body)
        sleep(3)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button').click()
        print("[+] Successfully posted on Twitter.")


    def compare_speeds(self, speed):

        if speed < ISP_SPEED_DOWN: 
            self.tweet_it(speed)



bot = InternetSpeedTwitterBot()
speed = bot.get_internet_speed()
bot.compare_speeds(speed)  