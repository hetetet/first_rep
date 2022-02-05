import csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/detail?titleId=733074&no=1&weekday=mon/comment/comment?titleId=733074&no=1"
# url2="&weekday=tue"
# filename="백수세끼 댓글.csv"
# f=open(filename,"w",encoding="utf-8-sig",newline="")
# writer=csv.writer(f)
# subtitle="화 댓글"
# writer.writerow(subtitle)
# row="작성자/내용/좋아요/싫어요/좋아요 비율".split('/')
# writer.writerow(row)

#1화만 시험삼아 출력 중
driver = webdriver.Chrome()
driver.get("https://comic.naver.com/webtoon/detail?titleId=733074&no=1&weekday=mon/comment/comment?titleId=733074&no=1")
driver.implicitly_wait(1)

driver.switch_to.frame("commentIframe")
elem=driver.find_element_by_id("cbox_module_wai_u_cbox_sort_option_tab2")
elem.click()
time.sleep(0.02)

r = driver.page_source
soup = BeautifulSoup(r, "html.parser")


nicks=soup.find_all("span",attrs={"class":"u_cbox_id"})
for nick in nicks:
    print(nick.get_text())

elem=driver.find_element_by_name('2')
elem.click()
time.sleep(0.02)

nicks=soup.find_all("span",attrs={"class":"u_cbox_id"}).next_sibling.next_sibling
for nick in nicks:
    print(nick.get_text())