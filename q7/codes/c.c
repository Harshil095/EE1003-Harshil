#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to simulate dice rolls and calculate probabilities for prime outcomes
void simulate_prime_rolls(int trials, double *probs) {
    int prime_counts[6] = {0}; // Counts for outcomes {1, 2, 3, 4, 5, 6}
    int roll, i;

    // Seed the random number generator
    srand(time(NULL));

    // Simulate dice rolls
    for (i = 0; i < trials; i++) {
        roll = (rand() % 6) + 1; // Generate numbers between 1 and 6
        if (roll == 2 || roll == 3 || roll == 5) {
            prime_counts[roll - 1]++; // Increment counts for prime numbers
        }
    }

    // Calculate probabilities
    for (i = 0; i < 6; i++) {
        if (i == 1 || i == 2 || i == 4) { // Indices 1, 2, and 4 correspond to primes {2, 3, 5}
            probs[i] = (double)prime_counts[i] / trials;
        } else {
            probs[i] = 0.0; // Non-prime outcomes have zero probability
        }
    }
}

// Exported function for Python
__attribute__((visibility("default"))) 
__attribute__((used)) 
void get_prime_probs(int trials, double *output_probs) {
    simulate_prime_rolls(trials, output_probs);
}

