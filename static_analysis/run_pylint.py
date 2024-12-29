import subprocess
import sys

def run_pylint(file_path):
    try:
        result = subprocess.run(['pylint', file_path], capture_output=True, text=True)
        print("Pylint Report:")
        print(result.stdout)
    except Exception as e:
        print(f"Error running Pylint: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_pylint.py <file_path>")
    else:
        run_pylint(sys.argv[1])
