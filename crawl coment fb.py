from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd

#set url
path = "C:\\Program Files\\Google\\Chrome\\Application.exe"
URL = "https://www.facebook.com/MonNgonVNso1/posts/pfbid02buo1t9y69reohCkZgUopYKa3M7vzmJBhCeKSdG2nrnYz7XzdAGfJ17PMdHjyXPQSl"
driver = webdriver.Chrome(executable_path = path)
driver.get(URL)
time.sleep(5)
print('Done')

# Xem Comment
view_cmt = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/div[1]/div/div[3]/span[1]/a').click()
time.sleep(5)
print('Done')

#Xem them cmt
more_cmt  = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div[2]/div[3]/div[2]/div/a/div')
more_cmt.click()
time.sleep(10)
print('Done')

#Xem them cmt
more_cmt.click()
time.sleep(5)
print('Done')

#Xem them cmt
more_cmt.click()
time.sleep(5)
print('Done')

#Tim comment element dang. lists
lists = driver.find_elements(By.XPATH,'//div[@aria-label="Comment"]')

#chay vong lap for trong lists lay ra tung cai'

Name=[]
Comment=[]
for list in lists:
    name = list.find_element_by_class_name('_6qw4')
    comment = list.find_element_by_class_name("_3l3x")
    Name.append(name)
    Comment.append(comment)
    print(Name)

list_of_data = list(zip(Name,Comment))
df=pd.DataFrame(list_of_data,columns=['User','cmt'])