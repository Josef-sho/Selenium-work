from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

path = "C:\dev\chromedriver.exe"

ser = Service(path)

driver = webdriver.Chrome(service=ser)

driver.get('http://secure-retreat-92358.herokuapp.com')

fname = driver.find_element(By.NAME, 'fName')
lname = driver.find_element(By.NAME, 'lName')
email = driver.find_element(By.NAME, 'email')
submit = driver.find_element(By.TAG_NAME, 'button')

fname.send_keys('josef')
lname.send_keys('sho')
email.send_keys('josephshodunke4@gmail.com')

submit.click()


# articleC = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
#
# print(articleC.text)

# driver.close()