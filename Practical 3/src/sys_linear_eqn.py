import numpy as np

a = np.array([[1,-3,-2],[0,2,4],[0,0,-10]])
print("A :",a)

b = np.array([7,4,12])
c = np.linalg.solve(a,b)

print("C :",c)
