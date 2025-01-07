import numpy as np
import matplotlib.pyplot as plt

# Define the function y = 4x^2
def func(x):
    return 4 * x**2

# Generate x values from 0 to 2 to show the region in the first quadrant
x = np.linspace(0, 2, 1000)

# Generate y values for the curve y = 4x^2
y = func(x)

# Create the figure and axis with a smaller figure size
fig, ax = plt.subplots(figsize=(6, 4))

# Plot the curve y = 4x^2
ax.plot(x, y, label=r'$y = 4x^2$', color='blue')

# Plot the horizontal lines y=1 and y=4
ax.axhline(y=1, color='red', linestyle='--', label=r'$y = 1$')
ax.axhline(y=4, color='green', linestyle='--', label=r'$y = 4$')

# Shade the area between y=1 and y=4 under the curve y=4x^2 in the first quadrant (x >= 0)
x_fill = np.linspace(0, 2, 1000)
y_fill = func(x_fill)
ax.fill_between(x_fill, 1, y_fill, where=(y_fill >= 1) & (y_fill <= 4), color='lightgray', label="Shaded Area")

# Add labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Area Enclosed Between the Curves')

# Set axis limits for a better view
ax.set_xlim([-0.5, 2.5])
ax.set_ylim([0, 5])

# Add a legend
ax.legend()

# Display the plot
plt.grid(True)
plt.show()

