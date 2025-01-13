import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared object file
newton_solver = ctypes.CDLL('./c.so')

# Set the return type for the C function
newton_solver.newton_method.restype = ctypes.c_double

# Call the Newton's method function in C
initial_guess = 10.0  # Starting guess for the root
tolerance = 1e-6      # Convergence tolerance
max_iter = 1000       # Maximum number of iterations

# Invoke the Newton's method from the shared C library
root = newton_solver.newton_method(ctypes.c_double(initial_guess), ctypes.c_double(tolerance), ctypes.c_int(max_iter))

print(f"Root found: {root}")

# Plot the function and mark the root
x = np.linspace(-5, 15, 500)  # Define the range of x values
y = x**2 - 7 * x - 60         # Define the function f(x) = x^2 - 7x - 60

plt.plot(x, y, label='f(x) = x^2 - 7x - 60')
plt.axhline(0, color='black', linewidth=0.7, linestyle='--')
plt.scatter([root], [0], color='red', label=f'Root at x = {root:.6f}')
plt.title('Newton\'s Method: Finding Roots')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()

