import os

RESULTS_DIR = "/app/random_snellen_letters_results"

def check_for_duplicates(RESULTS_DIR):
    print("checking for duplicates..")
    duplicates = {}
    for filename in os.listdir(RESULTS_DIR):
        if filename.endswith('.txt'):
            with open(os.path.join(RESULTS_DIR, filename), 'r') as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip()  # Remove any trailing newlines or whitespace
                    duplicates[line] = duplicates.get(line, []) + [filename]

    # Filter out non-duplicates (entries that appear in just one file)
    duplicates = {k: v for k, v in duplicates.items() if len(v) > 1}

    report = "DUPLICATE LINES REPORT\n" + "="*25 + "\n\n"

    if not duplicates:
        report += "Well, would ya look at that, the random function works. No duplicate lines were found.\n"
    else:
        for line, files in duplicates.items():
            report += f"Line '{line}' found in files: {', '.join(files)}\n"
    
    # Check if running
    report_path = os.path.join(RESULTS_DIR, 'duplicates_report.txt')

    with open(os.path.join(RESULTS_DIR, 'duplicates_report.txt'), 'w') as f:
        f.write(report)

if __name__ == "__main__":
    check_for_duplicates(RESULTS_DIR)
