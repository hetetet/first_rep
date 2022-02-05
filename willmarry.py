import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/list?titleId=616239&weekday=tue"
res=requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text,'lxml')
cartoons=soup.find_all("td",attrs={"class":"title"})
rates=soup.find_all("div",attrs={"class":"rating_type"})
#title=cartoons[0].a.get_text()
#link=cartoons[0].a["href"]
#print(title)
#print("https://comic.naver.com"+link)

# for cartoon in cartoons:
#     title=cartoon.a.get_text()
#     link="https://comic.naver.com"+cartoon.a["href"] 
#     print(title, link)

total_rates=0
for rate in rates:
    rat=rate.find("strong").get_text()
    total_rates+=float(rat)
    print(rat)
print("전체 점수: ", total_rates)
total_rates/=len(rates)
print("평균 점수: ", total_rates)