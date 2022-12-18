from bs4 import BeautifulSoup
import requests
import os

input_image = input("請輸入要下載的圖片：")

response = requests.get(f"https://www.wideshine.com/{input_image}")

soup = BeautifulSoup(response.text, "lxml")

results = soup.find_all("img", {"class": "_2VWD4 _2zEKz"}, limit=5)