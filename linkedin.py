from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


ser = Service('C:\dev\chromedriver.exe')
driver = webdriver.Chrome(service=ser)
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3325354619&f_AL=true&f_WT=2&geoId=105365761&keywords='
           'python%20developer&location=Nigeria&refresh=true')

signin = driver.find_element(By.LINK_TEXT, 'Sign in')
signin.click()


username = driver.find_element(By.ID, 'username')
username.send_keys('josephshodunke4@gmail.com')

password = driver.find_element(By.ID, 'password')
password.send_keys('banke123')
time.sleep(2)

signin2 = driver.find_element(By.CLASS_NAME, 'btn__primary--large')
signin2.click()
#
jobs = driver.find_element(By.CLASS_NAME, 'job-card-list__title')
jobs.click()

apply = driver.find_element(By.CLASS_NAME, 'artdeco-button__icon--in-bug')
apply.click()

num = driver.find_element(By.CLASS_NAME, 'fb-single-line-text__input')
num.send_keys('09090386260')

next = driver.find_element(By.CLASS_NAME, 'artdeco-button--primary ember-view')
next.click()





# skip = driver.find_element(By.CLASS_NAME, 'secondary-action')


