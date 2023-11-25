from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

import time


#PATH = "/Users/sainikhilkethireddy/Desktop/Work/Selenium/chromedriver.exe"
driver = webdriver.Chrome()

driver.get("https://www.google.com")
link = driver.find_element(By.LINK_TEXT,"Images")
link.click()

print(driver.title) 


search = driver.find_element("id","APjFqb")
search.send_keys("Welcome")
search.send_keys(Keys.RETURN)

time.sleep(30)

driver.quit()
