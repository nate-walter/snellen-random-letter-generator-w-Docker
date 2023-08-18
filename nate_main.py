import os
import requests
import random
from datetime import datetime 
from duplicates import check_for_duplicates

LETTERS = 'EFPTOZLDC'
RESULTS_DIR = "./random_snellen_letters_results"

def generate_random_combinations(length, count):
    api_key = os.getenv('RANDOM_ORG_API_KEY') # Just noting this is not currently used

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

    with open(file_path, 'w') as file:
        for combination in combinations:
            file.write(combination + "\n")

# # Uncomment if you want this to be your main 

# if __name__ == '__main__':
#     random_combinations = generate_random_combinations(7, 20) # Generate 20 combinations of length 7)

#     if random_combinations:
#         write_combinations_to_file(random_combinations)
#     else:
#         print("No combinations generated.")