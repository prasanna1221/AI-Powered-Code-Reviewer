import subprocess
import sys

def run_flake8(file_path):
    try:
        result = subprocess.run(['flake8', file_path], capture_output=True, text=True)
        print("Flake8 Report:")
        print(result.stdout)
    except Exception as e:
        print(f"Error running Flake8: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_flake8.py <file_path>")
    else:
        run_flake8(sys.argv[1])
