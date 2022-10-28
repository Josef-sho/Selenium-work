from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


ser = Service('C:\dev\chromedriver.exe')
driver = webdriver.Chrome(service=ser)
driver.get('https://www.linkedin.com/')

signin = driver.find_element(By.LINK_TEXT, 'Sign in')
signin.click()



username = driver.find_element(By.ID, 'username')
username.send_keys('josephshodunke4@gmail.com')
time.sleep(2)
password = driver.find_element(By.ID, 'password')
password.send_keys('banke123')
time.sleep(2)

signin2 = driver.find_element(By.CLASS_NAME, 'btn__primary--large')
signin2.click()

jobs = driver.find_element(By.XPATH, '/html/body/div[5]/header/div/nav/ul/li[3]/a')
jobs.click()

search1 = driver.find_element(By.CLASS_NAME, 'jobs-search-box__input-icon')
search1.send_keys('python developer')
search1.send_keys(Keys.ENTER)


# skip = driver.find_element(By.CLASS_NAME, 'secondary-action')


