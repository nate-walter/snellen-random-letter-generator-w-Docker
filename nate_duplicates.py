import os

# Path to the directory where the result files are located
RESULT_DIR = "./random_snellen_letters_results"

def check_for_duplicates(RESULTS_DIR):
    duplicates = {}
    for filename in os.listdir(RESULTS_DIR):
        if filename.endswith(".txt"):
            with open(os.path.join(RESULTS_DIR, filename), 'r') as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip() # Removing any trailing whitespace
                    duplicates[line] = duplicates.get(line, []) + [filename]

    # Filter out non-duplicates (entries that appear in just one file)
    duplicates = {k: v for k, v in duplicates.items() if len(v) > 1}
    
    # Generating a report for duplicates
    report = "DUPLICATE LINES REPORT\n" + "="*25 + "\n\n"
    if not duplicates:
        report += "Well look at that, one thing in this world works as intended...no duplicates found.\n"
    else:
        for line, files in duplicates.items():
            report += f"Line '{line}' was found in files: {', ',.join(files)}. I gues random doesn't mean what it used to smh.\n"

    # Save the report to a file
    with open(os.path.join(RESULTS_DIR, "duplicate_report.txt"), 'w') as f:
        f.write(report)
    print("Duplicate check completed. Report generated as 'duplicate_report.txt'.")

if __name__ == '__main__':
    check_for_duplicates()   