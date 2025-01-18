import numpy as np
import matplotlib.pyplot as plt

# Define the outcomes of a die throw and their probabilities
outcomes = np.array([1, 2, 3, 4, 5, 6])
probabilities = np.ones_like(outcomes) / len(outcomes)  # Uniform distribution

# Function to check for prime numbers
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Get the prime outcomes
prime_outcomes = np.array([outcome for outcome in outcomes if is_prime(outcome)])
prime_probabilities = probabilities[np.isin(outcomes, prime_outcomes)]

# Plotting the stem plot for prime number distribution
plt.stem(prime_outcomes, prime_probabilities, basefmt=" ", use_line_collection=True)
plt.xlabel("Die Outcome (Prime Numbers)")
plt.ylabel("Probability")
plt.xticks(prime_outcomes)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

