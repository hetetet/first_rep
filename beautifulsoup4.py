import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/index"
res=requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text,'lxml')
#print(soup.title)
#print(soup.title.get_text())
#print(soup.a) #처음으로 발견된 a element 반환/return first a element
#print(soup.a.attrs) #attrs: 속성
#print(soup.a["href"]) 
#print(soup.find("a",attrs={"Nbtn_upload"}))
#print(soup.find("li",attrs={"class":"rank01"}))
rank1=soup.find("li",attrs={"class":"rank01"})
print("---------------------------------------------------------------------")
#print(rank1.a)
#print(rank1.next_sibling.next_sibling) #줄바꿈 때문에 next_sibling 두번 해야할수도 있음/need to call next_sibling twice due to line change
#print(rank1.find_next_siblings("li"))

webtoon=soup.find("a",text="중증외상센터 : 골든 아워-2부 11화 : 중요한 사람이긴 한가 봐")
print(webtoon)