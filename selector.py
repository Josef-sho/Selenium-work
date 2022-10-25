from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


opera_path = "C:\dev\chromedriver.exe"
ser = Service(opera_path)
driver = webdriver.Chrome(service=ser)
driver.get("https://www.python.org")

lists =[]


time = driver.find_elements(By.CSS_SELECTOR, f'.event-widget time')
times = [i.text for i in time]

event = driver.find_elements(By.CSS_SELECTOR, f'.event-widget li a')
events = [i.text for i in event]


for i in range(len(events)):
    dict = {'time': times[i],
            'event': events[i]}
    lists.append(dict)

print(lists)
driver.close()
