import numpy as np
from numpy.linalg import inv

a = np.array([[1,2],[4,5]])
b = np.array([[3,6],[7,9]])

print(a)
print(b)

print(np.sum(a))
print(np.max(a))

print(a * b)

print(a.dot(b))
print(a.transpose())
print(a.T)
print(inv(a))
print(a.dot(inv(a)))