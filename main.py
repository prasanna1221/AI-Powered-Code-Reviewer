import os
import subprocess

def main():
    file_path = input("Enter the file path for analysis: ")

    # Static Analysis
    print("Running Flake8...")
    subprocess.run(['python', 'static_analysis/run_flake8.py', file_path])

    # Bug Detection
    from intelligent_suggestions.bug_detection import detect_bugs
    with open(file_path, 'r') as file:
        code = file.read()
        print("Bug Detection Result:")
        print(detect_bugs(code))

    # Code Refactoring
    from intelligent_suggestions.code_refactor import refactor_code
    print("Refactored Code:")
    print(refactor_code(code))

if __name__ == "__main__":
    main()
