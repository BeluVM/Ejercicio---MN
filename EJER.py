import numpy as np

# Coefficients matrix
A = np.array([[0.52, 0.20, 0.25],
              [0.30, 0.50, 0.20],
              [0.18, 0.30, 0.55]])

# Constants matrix
b = np.array([4800, 5810, 5690])

# Solve the system of equations
x = np.linalg.solve(A, b)

print(f"Quarry 1: {x[0]:.2f} cubic meters")
print(f"Quarry 2: {x[1]:.2f} cubic meters")
print(f"Quarry 3: {x[2]:.2f} cubic meters")
