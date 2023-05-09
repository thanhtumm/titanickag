# ADD thư viện
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

#Get source
col1=[]
col2=[]
col3=[]
for i in range(1,10):
    print(i)
    url = "https://zingnews.vn/kinh-doanh-tai-chinh/trang" +str(i) + ".html"
    page = requests.get(url)
    source = BeautifulSoup(page.text,"html.parser")
    #print(source)
    lists_title = source.findAll("p",class_="article-title")
    lists_date  = source.findAll("span",class_='article-publish')
    lists_type  = source.find_all("span",class_="category-parent")
    for list_title in lists_title:
        title = list_title.find("a").text
        col2.append(title)
    for list_date in lists_date:
        date_publish = list_date.find('span',class_="date").text
        col1.append(date_publish)
    for type in lists_type:
        if type.text == 'Kinh doanh':
            col3.append(type.text)
list_of_data = list(zip(col1,col2,col3))
df=pd.DataFrame(list_of_data,columns=['Date_publish','News','Category'])
print(df)