import os
import random
from datetime import datetime
from duplicates import check_for_duplicates

LETTERS = 'EFPTOZLDC'
RESULTS_DIR = "/app/random_snellen_letters_results"

def generate_random_combination(length, existing_combinations):
    while True: # This outer loop ensures we keep generating until we find a unique combination.
        combination = random.choice(LETTERS)
    
        while len(combination) < length:
            next_letter = random.choice(LETTERS)
            
            if next_letter != combination[-1]:  # Ensure no consecutive repeats
                combination += next_letter
            
        if combination in existing_combinations:
                return combination

def generate_random_combinations(length, count):
    combinations = set()

    while len(combinations) < count:
        combination = generate_random_combination(length, combinations)
        combinations.add(combination)
            
    return list(combinations)

def write_combinations_to_file(combinations):
    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)
    
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    file_path = os.path.join(RESULTS_DIR, f"results_{timestamp}.txt")
    
    print(combinations)

    with open(file_path, 'w') as file:
        for combination in combinations:
            file.write(combination + "\n")

        # # Add a duplicate on purpose
        # file.write(combinations[0] + '\n')

if __name__ == '__main__':
    random_combinations = generate_random_combinations(7, 100_000)
    
    if random_combinations:
        write_combinations_to_file(random_combinations)
        check_for_duplicates(RESULTS_DIR)
    else:
        print("No combinations generated.")
