import matplotlib.pyplot as plt

x = 2+4j
z = -1j
c = x*z

plt.scatter(x.real, x.imag, color="red")
plt.scatter(c.real, c.imag)

plt.show()
