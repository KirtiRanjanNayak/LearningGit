import random

# Generate a list of 10 random numbers between 1 and 100
random_numbers = [random.randint(1, 100) for _ in range(10)]

# Calculate the sum of the random numbers
total = sum(random_numbers)

# Print the random numbers and their sum
print("Random Numbers:", random_numbers)
print("Sum:", total)

