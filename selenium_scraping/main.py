'''
Web Scraping Product Price

This Python script scrapes product page and shows the price.

Prerequisites:
- Google Chrome
- Selenium Webdriver
- AmazonCaptcha

Usage:
1. Modify the URL variable in the script to specify the URL of the webpage containing the product.
2. Run the script:
$ python3 main.py
3. The script will bypass captcha and show the price of the product.

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from amazoncaptcha import AmazonCaptcha

URL = "https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/?th=1"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)


# Solving the Captcha to bypass
link = driver.find_element(By.XPATH, "//div[@class = 'a-row a-text-center']//img").get_attribute('src')
img_captcha = AmazonCaptcha.fromlink(link)
captcha_solved = AmazonCaptcha.solve(img_captcha)
input_field = driver.find_element(By.ID, "captchacharacters").send_keys(captcha_solved)
press_continue_shopping = driver.find_element(By.CLASS_NAME, "a-button-text")
press_continue_shopping.click()

# Scraping the price
price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

print(f"The price is {price_dollar.text}.{price_cents.text}")

#driver.close()
driver.quit()