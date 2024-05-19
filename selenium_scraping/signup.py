from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://secure-retreat-92358.herokuapp.com/"

FIRSTNAME = "User"
LASTNAME = "User"
EMAIL = "user@email.com"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)


input_field_first_name = driver.find_element(By.XPATH, "/html/body/form/input[1]").send_keys(FIRSTNAME)
input_field_last_name = driver.find_element(By.XPATH, "/html/body/form/input[2]").send_keys(LASTNAME)
input_field_email = driver.find_element(By.XPATH, "/html/body/form/input[3]").send_keys(EMAIL)

press_sign_up = driver.find_element(By.XPATH, "/html/body/form/button")
press_sign_up.click()

#driver.close()
#driver.quit()