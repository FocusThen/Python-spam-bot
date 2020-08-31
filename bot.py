from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

import time
import pandas as pd  # Pandas Excel kayıt ettirmek için.

#This example requires Selenium WebDriver 3.13 or newer

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

data = pd.read_csv('deneme.csv')

time.sleep(2)

for i in range(len(data)):
    driver.get("https://velibilgi.sj.k12.tr/")
    tcInput = driver.find_element_by_css_selector('#txtTcNo')
    tcInput.send_keys(str(data['TC'][i]))
    link = driver.find_element_by_css_selector('#jqLnkLostPass')
    link.click()
    time.sleep(1)