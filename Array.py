 # Write a function which returns an array of seven random numbers in a range 0-9. All the numbers must be unique

import random
def generate_unique_random_nums():
    unique_numbers = random.sample(range(10), 7)
    return unique_numbers




print(generate_unique_random_nums())