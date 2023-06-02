from bs4 import BeautifulSoup
import requests
from pprint import pprint
import json

response = requests.post(
    'https://auction.realestate.daum.net/ajax/main_list.php',
    params={
        'addr1': '서울',
        'result': '99',
        'yongdo': '99',
        'yongdo_detail': '99',
        'sort': '13D'
    },
    headers={
        'Referer': 'https://auction.realestate.daum.net/v15/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
)

# with open('./code_1.html','w',encoding = 'euc-kr') as f:
#     f.write(response.text)

soup = BeautifulSoup(response.text,'html.parser')

trs = soup.select('#frm_myreg > table > tbody > tr')

datas = []
for tr in trs:
    data = {
        '사건번호' : tr.select_one('td:nth-child(1) a').text ,
    '물건용도' : tr.select_one('td:nth-child(2) > div:nth-child(2) > a > p.used').text, 
    '감정가' : tr.select_one('td.price_new > div.mapList_price.price_icon1 > p').text , 
    '소재지' : tr.select_one('td:nth-child(2) > div:nth-child(2) > a > p.address').text, 
    '면적' : tr.select_one('td:nth-child(2) > div:nth-child(2) >  p.area > span').text, 
    '상태' : tr.select_one('td.auctioned_new > div > p:nth-child(1) > span').text
    }
    datas.append(data)

with open('./code_1.json','w',encoding='utf-8') as f:
    f.write(json.dumps(datas, ensure_ascii=False))