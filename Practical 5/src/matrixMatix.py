x = [[3, 2, 2],
    [4, 1, 5],
    [7, 2, 7]]
y = [[5, 3, 1, 2],
    [1, 7, 3, 0],
    [2, 5, 2, 1]]
mul = [[0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]]

print("Multiplication of two matrix is: ")
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            mul[i][j] += x[i][k] * y[k][j]

for r in mul:
    print(r)
