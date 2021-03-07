import numpy as np

u = np.array((3,4,5))
v = np.array((1,2,7))

print("Vector u",u)
print("Vector v",v)
print("Enter the value of a & b")

a = 2
b = 3
d = (a*u)+(b*v)
p = np.dot(u,v)

print("Vector au+bv",d)
print("Dot product of u & v",p)
