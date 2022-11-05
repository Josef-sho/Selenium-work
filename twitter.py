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
        self.username = None
        self.password = None
        self.login = None



    def get_speed(self):
        self.driver.get('https://fast.com/')
        # accept_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        # accept_button.click()
        time.sleep(40)
        self.go = self.driver.find_element(By.ID, 'show-more-details-link')
        self.go.click()

        self.up = self.driver.find_element(By.ID, 'up-mb-value')
        self.down = self.driver.find_element(By.ID, 'down-mb-value')
        print(self.up.text)
        print(self.down.text)

    def tweet_at_them(self):
        self.driver.get('https://twitter.com/login')
        self.username = self.driver.find_element(By.NAME, 'text')
        self.username.send_keys(f'{TWITTER_USERNAME}')
        time.sleep(3)
        self.username.send_keys(Keys.ENTER)
        try:
            self.password = self.driver.find_element(By.NAME, 'password')
            self.password.send_keys(f'{TWITTER_PASSWORD}')
            self.login = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div/div/span/span')
            self.login.click()
        except:
            time.sleep(3)
            self.username = self.driver.find_element(By.NAME, 'text')
            self.username.send_keys(f'{TWITTER_USERNAME}')



tweet = Twitter(serv)

tweet.tweet_at_them()

# accept = driver.find_element(By.ID, 'start-text')

# go = driver.find_element(By.CLASS_NAME, 'start-text')
# go.click()
#
# up = driver.find_element(By.CLASS_NAME, 'download-speed')
# down = driver.find_element(By.CLASS_NAME, 'upload-speed')
#
# print(up.text)
# print(down.text)
