# -*- coding: utf-8 -*-
"""상관관계.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mZW5PTxkAsgw7C3hZJ_fhNXt_sOehWOD
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel('/content/drive/MyDrive/Colab Notebooks/머신러닝/자료/phone.xlsx')
df.head()

df.corr()
import seaborn as sns
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(),annot=True)

x = df[['Q3B_4','Q3B_5','Q3B_6','Q3B_10']].to_numpy()
y = df['KK1'].to_numpy()
print(x.shape,y.shape)

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,stratify = y)
print(x_train.shape,y_train.shape)

from sklearn.neural_network import MLPClassifier
model = MLPClassifier(hidden_layer_sizes=(100,50,25),verbose = True)
model.fit(x_train,y_train)

model.score(x_test,y_test)

question = ['스마트폰이 옆에 있으면 다른 일에 집중하기 어렵다.',
            '스마트폰 생각이 머리에서 떠나지 않는다.',
            '스마트폰을 이용하고 싶은 충동을 강하게 느낀다.',
            '스마트폰 때문에 학업 수행에 어려움이 있다.']

result = np.zeros(4)
print('다음 질문에 답해주세요 1(전혀아니다), 2(아니다),3(그렇다),4(매우 그렇다)')

for i,q in enumerate(question):
  result[i] = int(input((q)))
pred_result = model.predict([result])
print(pred_result)
if pred_result == 1:
  print("예상: 고위험군")
elif pred_result ==2:
  print("예상: 잠재적 위험군")
else:
  print("예상: 일반 사용자군")