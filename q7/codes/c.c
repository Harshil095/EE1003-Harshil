#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to simulate rolling a single die
void roll_one_die(int trials, int *results) {
    for (int i = 0; i < trials; i++) {
        int die = (rand() % 6) + 1; // Generate numbers from 1 to 6
        results[die - 1]++; // Increment corresponding die face count
    }
}

// Main function to calculate the probability of rolling a prime number
int main() {
    srand(time(0)); // Seed the random number generator only once
    int trials = 1000000; // Number of trials
    int results[6] = {0}; // Array to store counts for each face (1 to 6)
    int primes[] = {2, 3, 5}; // Prime numbers on the die
    int prime_count = 0;

    // Simulate die rolls
    roll_one_die(trials, results);

    // Count occurrences of prime numbers
    for (int i = 0; i < 3; i++) { // Iterate through prime numbers
        prime_count += results[primes[i] - 1]; // Accumulate counts for primes
    }

    // Calculate and display the probability
    double probability = (double)prime_count / trials;
    printf("Estimated Probability of rolling a prime number: %f\n", probability);

    // Optional: Display individual counts for each face
    for (int i = 0; i < 6; i++) {
        printf("Face %d appeared %d times.\n", i + 1, results[i]);
    }

    return 0;
}

