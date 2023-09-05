import os
import random
from itertools import permutations
from datetime import datetime
from duplicates import check_for_duplicates


LETTERS = "EFPTOZLDC"
RESULTS_DIR = "/app/random_snellen_above_0.7142"

def letter_diversity(combination):
    return len(set(combination)) / len(combination)

def generate_initial_combinations(length):
    initial_combinations = set()
    for i in range(length, len(LETTERS) + 1):
        for combo in permutations(LETTERS, i):
            initial_combinations.add("".join(combo))
    return initial_combinations

def extend_combination(combo, final_length):
    missing_letters = [letter for letter in LETTERS if letter not in combo]
    
    while len(combo) < final_length:
        to_add = random.choice(missing_letters)
        
        # Check for consecutive repeats
        valid_positions = [i for i, c in enumerate(combo) if i == 0 or (combo[i-1] != to_add and (i == len(combo) - 1 or combo[i] != to_add))]
        
        if not valid_positions:
            continue  # Skip to the next iteration if no valid position is found for the current letter

        insert_pos = random.choice(valid_positions)
        
        # Insert the letter at the valid position
        combo = combo[:insert_pos] + to_add + combo[insert_pos:]

        # Now we must also check the newly formed combo for consecutive repeats.
        has_consecutive_repeats = any(combo[i] == combo[i+1] for i in range(len(combo) - 1))

        if not has_consecutive_repeats:
            if combo.count(to_add) >= 2:
                missing_letters.remove(to_add)
        else:
            # Revert the addition if it led to consecutive repeats
            combo = combo[:insert_pos] + combo[insert_pos+1:]
    
    return combo


def write_combinations_to_file(combinations):
    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)
    
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    file_path = os.path.join(RESULTS_DIR, f"results_{timestamp}.txt")
    
    with open(file_path, 'w') as file:
        for combination in combinations:
            file.write(combination + "\n")

if __name__ == '__main__':
    initial_combinations = generate_initial_combinations(5)
    print(f"Number of initial combinations: {len(initial_combinations)}")
    
    final_combinations = set()
    for combo in initial_combinations:
        if len(combo) == 7:  # If the initial combination is already 7 letters long
            final_combinations.add(combo)
        else:
            extended_combo = extend_combination(combo, 7)
            if letter_diversity(extended_combo) >= 0.7143 and len(extended_combo) == 7:
                final_combinations.add(extended_combo)

    print(f"Number of initial combinations: {len(initial_combinations)}")
    print(f"Number of final combinations: {len(final_combinations)}")
    
    write_combinations_to_file(final_combinations)
