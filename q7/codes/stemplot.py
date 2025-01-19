import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
dice_simulation = ctypes.CDLL('./c.so')

# Define the function prototype
dice_simulation.get_prime_probs.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_double)]

# Parameters
trials = 1000000
output_probs = (ctypes.c_double * 6)()  # One for each face (1-6)

# Call the C function
dice_simulation.get_prime_probs(trials, output_probs)

# Convert probabilities to a Python list
probs = list(output_probs)

# Define outcomes: 1-6
x_labels = ['1', '2', '3', '4', '5', '6']

# Update probabilities for non-prime outcomes
# Prime numbers are {2, 3, 5}; non-prime numbers {1, 4, 6} should have 0 probability.
probs = [0 if label in [1, 4, 6] else probs[label - 1] for label in range(1, 7)]

# Plot the probabilities
x = np.arange(len(x_labels))
plt.stem(x, probs, basefmt=" ", use_line_collection=True)
plt.xticks(x, x_labels)
plt.xlabel("Outcomes")
plt.ylabel("Probability")
plt.title("Stemplot")
plt.grid()
plt.show()

