import numpy as np

m = np.array([[1, 8, 3], [8, 9, 4], [4, 8, 23]])
t = np.array([[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]])

for i in range(len(m)):
    for j in range(len(m[0])):
        t[j][i] = m[i][j]

print(t)
