#!/usr/bin/env python3
 

from matplotlib import pyplot as plt
import numpy as np

x = np.array([
    [1,2,3],
    [4,5,6],
    [4,5,-1]
])
# #2x(2x3)
# tensor = np.array([
#     [[1,2,3],
#      [4,5,6]],
#     [[7,8,9],
#      [10,11,12]]
# ])
# print(type(x))
# print(x.shape)
# print(x.ndim)
# print(x)
# print(type(tensor))
# print(tensor.shape)
# print(tensor.ndim)
# print(tensor)

plt.imshow(x, cmap='Blues')
plt.colorbar()
plt.show()
