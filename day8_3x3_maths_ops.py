import numpy as np

a = np.array([[1,2,3], [4, 5, 6], [7, 8, 9]])

b = a.T

print(f"Original Matrix: {a}")

print(f"Transpose Matrix: {a.T}")

print (f"Add: {a+b}")

print (f"Subtract: {b-a}")

print (f"Multiply: {a*b}")

print (f"Divide: {a/b}")

norm_arr = (a - np.min(a)) / (np.max(a) - np.min(a))

print(f"Normalized Matrix: {norm_arr}")

c = np.random.rand(3, 2)

print(c)