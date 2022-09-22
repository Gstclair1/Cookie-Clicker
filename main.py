from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

timeout = time.time() + 5
five_min = time.time() + 60*5

while True:
    cookie.click()
    if time.time() > timeout:
        try:
            driver.find_element(By.XPATH, '//*[@id="buyTime machine"]').click()
        except:
            pass
        try:
            driver.find_element(By.XPATH, '//*[@id="buyPortal"]').click()
        except:
            pass
        try:
            driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]').click()
        except:
            pass
        try:
            driver.find_element(By.XPATH, '//*[@id="buyShipment"]').click()
        except:
            pass
        try:
            driver.find_element(By.XPATH, '//*[@id="buyMine"]').click()
        except:
            pass
        try:
            driver.find_element(By.XPATH, '//*[@id="buyFactory"]').click()
        except:
            pass
        try:
            driver.find_element(By.XPATH, '//*[@id="buyGrandma"]').click()
        except:
            pass
        try:
            driver.find_element(By.XPATH, '//*[@id="buyCursor"]').click()
        except:
            pass
        timeout = time.time() + 5
    if time.time() > five_min:
        cookie_per_second = driver.find_element(By.ID, "cps").text
        print(cookie_per_second)
        break
