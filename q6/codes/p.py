import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared object file (c.so)
c_lib = ctypes.CDLL('./c.so')  # Make sure the path to c.so is correct

# Define the function prototypes from the C library
c_lib.gen_line_points.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
c_lib.gen_line_points.restype = None

c_lib.free_ptr.argtypes = [ctypes.POINTER(ctypes.c_double)]
c_lib.free_ptr.restype = None

# Constants for the equations
slope1 = 5.0 / 4.0
c1 = 2.0
slope2 = -7.0 / 6.0
c2 = 3.0 / 2.0
num_points = 100  # Number of points for each line

# Create ctypes arrays to hold points for each line
points_line1 = (ctypes.c_double * (2 * num_points))()  # Points for the first line
points_line2 = (ctypes.c_double * (2 * num_points))()  # Points for the second line

# Call the C function to generate points for both lines
c_lib.gen_line_points(slope1, c1, num_points, points_line1)
c_lib.gen_line_points(slope2, c2, num_points, points_line2)

# Extract points from the ctypes arrays
x_line1 = np.array([points_line1[2 * i] for i in range(num_points)])
y_line1 = np.array([points_line1[2 * i + 1] for i in range(num_points)])

x_line2 = np.array([points_line2[2 * i] for i in range(num_points)])
y_line2 = np.array([points_line2[2 * i + 1] for i in range(num_points)])

# Calculate the point of intersection (solve for x and y)
# 5x - 4y + 8 = 0
# 7x + 6y - 9 = 0
# Solving the system of equations
A = np.array([[5, -4], [7, 6]])
B = np.array([-8, 9])
intersection = np.linalg.solve(A, B)
x_intersect, y_intersect = intersection

# Plot the lines and the intersection point
plt.plot(x_line1, y_line1, label='5x - 4y + 8 = 0', color='blue')
plt.plot(x_line2, y_line2, label='7x + 6y - 9 = 0', color='red')
plt.scatter(x_intersect, y_intersect, color='green', zorder=5, label=f'Intersection: ({x_intersect:.2f}, {y_intersect:.2f})')

plt.xlabel('X')
plt.ylabel('Y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()
plt.grid(True)
plt.show()

# Free the allocated memory
c_lib.free_ptr(points_line1)
c_lib.free_ptr(points_line2)

