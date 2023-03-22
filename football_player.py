import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

#headers에 'user agent' 값 넣기
#구글에서 my user agent 검색해서 가져오기

headers = {'User-Agent' : ''}

#url 주소 가져오기
#첫페이지 정보 가져오기

url = 'https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop?page=1'

#request.get()으로 요청하기

r = requests.get(url, headers = headers)

#200이 나오면 연결성공
print(r.status_code)

#페이지의 정보를 출력
soup = BeautifulSoup(r.text,'html.parser')


#선수들의 정보가 담긴 태그와 클래스 찾기
#사이트에서 112모드로 찾기

player_info = soup.find_all('tr',class_ = ['odd','even']) #클래스가 odd와 even인 태그들을 가져옴

#첫번째 요소 보기
print(player_info[0])

#전체 개수 확인하기
print(len(player_info))

#7개의 정보를 담을 빈 리스트 만들기

number = []
name = []
position = []
age = []
nation = []
team = []
value = []

#정보를 찾아서 각 리스트에 .append로 추가
for info in player_info:
  players = info.find_all('td')
  number.append(players[0].text)
  name.append(players[3].text)
  position.append(players[4].text)
  age.append(players[5].text)
  nation.append(players[6].img['alt'])
  team.append(players[7].img['alt'])
  value.append(players[8].text)

#데이터 프레임으로 저장
tf= pd.DataFrame(
    { 'number' : number,
     'name' : name,
     'position' : position,
     'age' : age,
     'nation' : nation,
     'team' : team,
     'value' : value}
)

print(tf)

#tf를 csv파일로 저장
tf.to_csv('transfermakt25.csv', index = False)

