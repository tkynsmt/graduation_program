import numpy as np

A=np.array([[3,2,1],[1,2,4]])
B=np.dot(A.T,A)
values,vectors=np.linalg.eig(B)
singular_values=np.sqrt(values)
print(np.argsort(singular_values)[::1])