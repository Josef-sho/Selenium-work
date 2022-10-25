from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

path = "C:\dev\chromedriver.exe"
ser = Service(path)

driver = webdriver.Chrome(service=ser)

driver.get('https://www.appbrewery.co/p/newsletter')
email = driver.find_element(By.NAME, 'email')
email.send_keys('josephshodunke4@gmail.com')

submit = driver.find_element(By.NAME, 'commit')
submit.click()
