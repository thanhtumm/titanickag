#import
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#set url
path = "C:\\Program Files\\Google\\Chrome\\Application.exe"
URL = "https://www.facebook.com/"
driver = webdriver.Chrome(executable_path = path)
driver.get(URL)
time.sleep(3)
print('Done')

#set id + pass
account = 'fakefb@gmail.com'
password = "alsofake"

#put in ID + Pass + Enter
account_entry = driver.find_element(By.XPATH,'//*[@id="email"]')
account_entry.send_keys(account)
time.sleep(3)
print('Done')

password_entry = driver.find_element(By.XPATH,'//*[@id="pass"]')
password_entry.send_keys(password)
time.sleep(3)
print('Done')

password_entry.send_keys(Keys.ENTER)
print('Done')