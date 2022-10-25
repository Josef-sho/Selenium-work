from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
#
# username = input('input your username please')
# passw = input('what is your password please')
# serr = input('Hey josef what service do you want to go to, type 1 or 2 :')

opera_path = "C:\dev\chromedriver.exe"
ser = Service(opera_path)
driver = webdriver.Chrome(service=ser)
driver.get("https://att.lmu.edu.ng/log/login")

user = driver.find_element(By.NAME, 'username')
user.send_keys(f'shodunke.joseph')
password = driver.find_element(By.NAME, 'password')
password.send_keys(f'tbontbtitq123')
submit = driver.find_element(By.NAME, 'submit')
submit.click()

service = driver.find_element(By.XPATH, '/html/body/div[2]/div/ul/li[5]/a')
service.click()

cs = driver.find_element(By.NAME, 'pudate')

# if serr == 2:
dd = Select(cs)
dd.select_by_index(1)

# elif serr == 1:
#     dd = Select(cs)
#     dd.select_by_index(2)


tag = driver.find_element(By.CLASS_NAME, 'check')
tag.click()

alert = driver.switch_to.alert
alert.accept()

last = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/form/div/div[2]/div[2]/input')
last.click()

# tbontbtitq123
# shodunke.joseph