import matplotlib.pyplot as plt

x = 2+2j
a = [-2+4j, -1+2j, 0+2j, 1+2j, 2+2j, -1+4j, 0+4j, 1+4j]
x = [x.real for x in a]
y = [x.imag for x in a]
plt.scatter(x, y,color="red")
plt.show()
