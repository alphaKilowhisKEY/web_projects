
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://en.wikipedia.org/wiki/Main_Page"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

article_element = driver.find_element(By.CSS_SELECTOR, "#articlecount a")

print(article_element.text)

driver.quit()