from time import sleep
from selenium import webdriver
import pandas as pd

browser = webdriver.Chrome()
#建立webdriver的Chrome類別建立瀏覽器物件
#建立後就可用這個物件來操作Chrome了

browser.get("https://zh-tw.facebook.com/")
#讀取網頁資料
sleep(1)
browser.find_element("id","email").send_keys("wxes10330121@gmail.com")
#輸入帳號
sleep(1)
browser.find_element("id","pass").send_keys("2066942841")
#輸入密碼
sleep(1)
browser.find_element("name","login").click()
sleep(100)
#登入
browser.quit()
#關閉視窗結束驅動

import selenium
print(selenium.path)