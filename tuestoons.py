import csv
import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/weekdayList?week=tue"
res=requests.get(url)
res.raise_for_status()
soup=BeautifulSoup(res.text,'lxml')

alltoons=soup.find_all("ul",attrs={"class":"img_list"})#list_area daily_img
titles=soup.find("ul",attrs={"class":"img_list"}).find_all("dt")
authors=soup.find("ul",attrs={"class":"img_list"}).find_all("dd",attrs={"class":"desc"})
rates=soup.find("ul",attrs={"class":"img_list"}).find_all("dd")

filename="화요웹툰.csv"
f=open(filename,"w",encoding="utf-8-sig",newline="")
writer=csv.writer(f)
info="제목/작가/평점".split('/')
writer.writerow(info)

col_1=[]
col_2=[]
col_3=[]

for title in titles:
    columns=title.find_all("a")
    data=[column.get_text() for column in columns]
    col_1.append(data[0])

for author in authors:
    columns=author.find_all("a")
    data=[column.get_text() for column in columns]
    col_2.append(data[0])

for rate in rates:
    columns=rate.find_all("strong")
    data=[column.get_text() for column in columns]
    if len(columns)<1:
        continue
    col_3.append(data[0])

for i in range(0,len(col_1)):
    writer.writerow([col_1[i],col_2[i],col_3[i]])
