#存取網路資源
import requests

url = "https://www.webtoons.com/zh-hant/"
r = requests.get( url )
# if r.status_code == 200:
#     print(r.text)
# else:
#     print(r.status_code , r.reason)

#解析資料(bs4)
from bs4 import BeautifulSoup
bs = BeautifulSoup(r.text, "html.parser")
# print(bs.a["href"])

# print(bs.find_all("h3",{ "class" : "subj"}))
# for i in range(0,9,2):
#     print(bs.find_all("h3",{"class": "subj"})[i].text)

for i in range(0,9):
    print(bs.select("ul.card_lst li div.card_flipper div.card_front div.info h3.subj")[i].text)