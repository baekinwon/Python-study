# -*- coding: utf-8 -*-

# 전체 데이터 리스트(생선의 길이와 무게)
fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8, 
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7, 
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

import numpy as np

fish_data = np.column_stack((fish_length,fish_weight))

fish_target = np.concatenate((np.ones(35),np.zeros(14)))

from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(
    fish_data,fish_target,stratify = fish_target,random_state=42)

from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier()
kn.fit(train_input,train_target)
kn.score(test_input,test_target)

if kn.predict([[25,150]]) ==0:
  print('빙어')
else:
  print('도미')

import matplotlib.pyplot as plt
plt.scatter(train_input[:,0],train_input[:,1])
plt.scatter(25,150,marker='^',color='red')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

distances, indexes = kn.kneighbors([[25,150]])

import matplotlib.pyplot as plt
plt.scatter(train_input[:,0],train_input[:,1])
plt.scatter(25,150,marker='^',color='red')
plt.scatter(train_input[indexes,0],train_input[indexes,1],marker = 'D')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

import matplotlib.pyplot as plt
plt.scatter(train_input[:,0],train_input[:,1])
plt.scatter(25,150,marker='^',color='red')
plt.scatter(train_input[indexes,0],train_input[indexes,1],marker = 'D')
plt.xlim((0,1000))
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

mean = np.mean(train_input, axis=0)
std = np.std(train_input,axis=0)

train_scaled = (train_input-mean)/std

new=([25,150]-mean) /std

plt.scatter(train_scaled[:,0],train_scaled[:,1])
plt.scatter(new[0],new[1],marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

#정확한 데이터로 다시 kn모듈에 학습
kn.fit(train_scaled,train_target) #target은 0과 1

test_scaled = (test_input - mean) /std

if kn.predict([new]) ==0:  #임의의 물고기 new를 정답데이터로 비교한다. 0=빙어 1=도미
  print('빙어')
else:
  print('도미')

distances,indexes = kn.kneighbors([new]) #가장 가까운 거리와 인덱스를 저장한다.

plt.scatter(train_scaled[:,0],train_scaled[:,1])
plt.scatter(new[0],new[1],marker='^')
plt.scatter(train_scaled[indexes,0],train_scaled[indexes,1],marker = 'D') #가장 가까운 훈련 데이터를 사각형으로 표시
plt.xlabel('length')
plt.ylabel('weight')
plt.show()