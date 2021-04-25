import numpy as np

m = np.array([[1, 8, 3], [8, 9, 4], [4, 8, 23]])

y = m[0:2]
print(y)

y = m[0:3]
print(y)

x = m[:, 0:1]
print(x)

x = m[:, 0:2]
print(x)

x = m[:, 0:3]
print(x)
