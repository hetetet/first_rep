from selenium import webdriver
import time
import random

browser=webdriver.Chrome("D:\python\webscraping_basic\chromedriver.exe")#이 py파일과 다른 경로에 있을 경우 소괄호 안에 경로를 적어 주어야 함
browser.get("https://www.naver.com")
elem=browser.find_element_by_class_name("link_login")
elem.click()
time.sleep(random.uniform(1,3))
browser.find_element_by_id("id").send_keys("id")
browser.find_element_by_id("pw").send_keys("passworld")
#id and password is just example
browser.find_element_by_id("log.login").click()
#time.sleep(3)