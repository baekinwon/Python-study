# -*- coding: utf-8 -*-
"""grape.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I1v_ltkXBYS_5oZ5LOdBT3mlfPER5pG3
"""

import numpy as np
import matplotlib.pyplot as plt

grape = np.array([[19,300,0],[20,500,0],[18,400,0],[25,500,1],[27,700,1],[28,600,1]])

x= grape[:, :2]
y = grape[:, 2]
print(x)
print(y)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(x,y)
print(model.coef_)
model.coef_
print(model.intercept_)

print(model.predict([[22,600]]))
print(model.predict([[20,500]]))

print(model.score(x,y))

size = float(input('포도 한알의 크기는(mm): '))
weight = float(input('포도 한 송이의 무게는(g): '))
result = model.predict([[size,weight]])
if result == 1:
  print('거봉')
else:
  print('일반 포도')