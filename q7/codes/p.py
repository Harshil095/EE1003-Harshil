import ctypes
import matplotlib.pyplot as plt
import numpy as np

# Load the shared library (make sure to build the C shared library correctly)
one_die_sim = ctypes.CDLL('./c.so')

# Set up the C function's argument and return types
one_die_sim.roll_one_die.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]

# Parameters
trials = 1000000  # Increase trials for better accuracy
results = (ctypes.c_int * 6)()  # Results array for numbers 1-6 (no need for '>6')

# Call the C function
one_die_sim.roll_one_die(trials, results)

# Extract results and calculate probabilities
prime_indices = [1, 2, 4]  # Indices for prime numbers: 2, 3, 5 (corresponding to 1, 2, 4 in 0-indexed array)
prime_count = sum(results[i] for i in prime_indices)  # Sum the occurrences of prime numbers
non_prime_count = trials - prime_count  # Count for non-prime numbers

# Probabilities
prime_probability = prime_count / trials
non_prime_probability = non_prime_count / trials

# Categories for plotting
categories = ['Prime Numbers', 'Non-Prime Numbers']
probabilities = [prime_probability, non_prime_probability]

# Plot the probability distribution
plt.bar(categories, probabilities, color='skyblue')
plt.xlabel("Outcome Type")
plt.ylabel("Probability")
plt.ylim(0, 1)  # Set y-axis to range from 0 to 1 for clarity
plt.show()

