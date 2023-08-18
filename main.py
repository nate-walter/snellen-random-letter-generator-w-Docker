import os
import requests
import random
from datetime import datetime

LETTERS = 'EFPTOZLDC'
RESULTS_DIR = "/app/random_snellen_letters_results" # Uncomment this to run in Docker container
# RESULTS_DIR = "random_snellen_letters_results" # Uncomment to run in terminal

def generate_random_combinations(length, count):
    api_key = os.getenv('RANDOM_ORG_API_KEY')  # Just noting that this isn't used in your current code
    
    combinations = []
    while len(combinations) < count:
        random_indices = random.sample(range(len(LETTERS)), length)
        combination = ''.join(LETTERS[i] for i in random_indices)
        
        if combination not in combinations:
            combinations.append(combination)
    
    return combinations

def write_combinations_to_file(combinations):
    # Ensure the directory exists
    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)
    
    # Use current timestamp to make each filename unique
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    file_path = os.path.join(RESULTS_DIR, f"results_{timestamp}.txt") 
    
    print(random_combinations)

    with open(file_path, 'w') as file:
        for combination in random_combinations:
            file.write(combination + "\n")

if __name__ == '__main__':
    random_combinations = generate_random_combinations(7, 10)  # Generate 10 combinations of length 7
    
    if random_combinations:
        write_combinations_to_file(random_combinations)
    else:
        print("No combinations generated.")
