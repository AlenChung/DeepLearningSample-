import numpy as np
from scipy import linalg

A = np.array([[1,3,5],[2,1,6],[3,6,4]])
print(A)
print(linalg.inv(A))
