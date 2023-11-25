from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(10)

lang = driver.find_element("id","langSelect-EN").click()
time.sleep(2)
counter = 0
get_cookie = driver.find_element("id","bigCookie")
while True:
    if counter <= 250:
        get_cookie.click()
        counter += 1
    else:
        print("Reached the end!")
        break
driver.quit()