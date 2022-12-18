from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("./learning/chromedriver.exe")
driver.get("https://tc.nutc.edu.tw/cas/login?service=https%3A//tc.nutc.edu.tw/user/index&locale=zh_TW&ts=1670417649.365797")
sleep(5)

