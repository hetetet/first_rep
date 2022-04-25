import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/weekday"
res=requests.get(url)
res.raise_for_status()
soup=BeautifulSoup(res.text,'lxml')

#네이버 웹툰 전체목록 가져오기/return whole list of naver webtoon
cartoons=soup.find_all("a",attrs={"class":"title"})
#all이 없으면 조건에 해당하는 첫번째 엘리먼트만 찾음, class 속성이 title인 모든 엘리먼트 반환/if no all, just find first element which requires condition, class attribute will return all elements whose attribute is 'title'
for cartoon in cartoons:
    print(cartoon.get_text())
    