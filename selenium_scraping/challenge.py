'''
This Python script uses Selenium to interact with the Python.org website. 
It retrieves the upcoming events listed on the homepage and stores them in a dictionary.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.python.org/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Find the number of elements by XPath
li_elements = driver.find_elements(By.XPATH, "/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li")
number_li_elements = len(li_elements)

li_dictionary = {}


for index, li_element in enumerate(li_elements):

    li_dictionary[index] = {
        "time": li_element.find_element(By.XPATH, "time").text,
        "name" : li_element.find_element(By.TAG_NAME, "a").text
    }


print(li_dictionary)
driver.quit()