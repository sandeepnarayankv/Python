import numpy as np

np.random.seed(411960)

matrix = np.random.randint(1, 51, size=(5,5))

print(matrix)

# filter the numbers above 25 and replace by 0

matrix[matrix > 25] = 0

print(matrix)

# Calculate summary stats

print(f"Sum: {np.sum(matrix)}")

print(f"Mean: {np.mean(matrix)}")

print(f"Standard Deviation: {np.std(matrix)}")