import os
import requests
import random

LETTERS = 'EFPTOZLDC'

def generate_random_combinations(length, count):
    api_key = os.getenv('RANDOM_ORG_API_KEY')
    
    combinations = []
    while len(combinations) < count:
        random_indices = random.sample(range(len(LETTERS)), length)
        combination = ''.join(LETTERS[i] for i in random_indices)
        
        if combination not in combinations:
            combinations.append(combination)
    
    return combinations

if __name__ == '__main__':
    random_combinations = generate_random_combinations(7, 10)  # Generate 10 combinations of length 7
    
    if random_combinations:
        for combination in random_combinations:
            print(combination)
    else:
        print("No combinations generated.")
