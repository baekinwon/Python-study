import numpy as np
import matplotlib.pyplot as plt

heart = np.array([[1,0,0,1,0,0,1],
                  [0,1,1,0,1,1,0],
                  [0,1,1,1,1,1,0],
                  [1,0,1,1,1,0,1],
                  [1,1,0,1,0,1,1],
                  [1,1,1,0,1,1,1]])

plt.xticks([])
plt.yticks([])
plt.imshow(heart,cmap = 'gray')
plt.show()