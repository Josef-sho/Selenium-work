from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


ser = Service('C:\dev\chromedriver.exe')
driver = webdriver.Chrome(service=ser)
driver.get('https://netsurf.lmu.edu.ng')

balance = driver.find_element(By.XPATH, '/html/body/div[2]/div/ul[2]/li[2]/a/span')
balance.click()

username = driver.find_element(By.ID, 'username')
password = driver.find_element(By.ID, 'pass')

username.send_keys('50G32575')
password.send_keys('2960')

submit = driver.find_element(By.NAME ,'checkBal')
submit.click()