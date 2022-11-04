from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

serv = Service('C:\dev\chromedriver.exe')
PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_USERNAME = 'josephshodunke4@gmail.com'
TWITTER_PASSWORD = 'bankE123'


class Twitter:
    def __init__(self, ser):

        self.up = 0
        self.down = 0
        self.go = None
        self.driver = webdriver.Chrome(service=ser)


    def get_speed(self):
        self.driver.get('https://www.speedtest.net')
        accept_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        accept_button.click()
        self.go = self.driver.find_element(By.CLASS_NAME, 'start-text')
        self.go.click()

        time.sleep(60)
        self.up = self.driver.find_element(By.CLASS_NAME, '.download-speed')
        self.down = self.driver.find_element(By.CLASS_NAME, '.upload-speed')
        print(self.up)
        print(self.down)

    def tweet_at_them(self):
        self.driver.get('https://twitter.com/i/flow/login')


tweet = Twitter(serv)

tweet.get_speed()

# accept = driver.find_element(By.ID, 'start-text')

# go = driver.find_element(By.CLASS_NAME, 'start-text')
# go.click()
#
# up = driver.find_element(By.CLASS_NAME, 'download-speed')
# down = driver.find_element(By.CLASS_NAME, 'upload-speed')
#
# print(up.text)
# print(down.text)