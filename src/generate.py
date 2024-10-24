import os
import subprocess
import sys

# Create the tests directory if it doesn't exist
os.makedirs("env/tests", exist_ok=True)

try:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    
    if start < 1 or end < start:
        raise ValueError("Invalid range for test cases.")

except ValueError as e:
    print(f"Error: {e}")
    sys.exit(1)

# Generate input files
for i in range(start, end + 1):
    input_file_path = f'env/tests/{i:04}.in'
    try:
        # Use subprocess to run input.py and redirect output to the file
        with open(input_file_path, 'w') as input_file:
            subprocess.run(['python3', 'env/generator.py'], stdout=input_file, check=True)
        print(f'Created: {input_file_path}')
    except subprocess.CalledProcessError:
        print(f'Error generating input for test case {i:04}')
        continue

print(f'All testcases created without errors')