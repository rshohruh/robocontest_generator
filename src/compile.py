import os
import subprocess
from time import time

# Determine the language and paths
lang = 'cpp' if os.path.exists('env/solution.cpp') else 'py'
tests_dir = 'env/tests/'
executable = 'env/solution' if lang == 'cpp' else 'env/solution.py'

# Compile if C++
if lang == 'cpp':
    compile_process = subprocess.run(['g++', '-o', executable, 'env/solution.cpp'], capture_output=True)
    if compile_process.returncode != 0:
        print("Compilation failed:")
        print(compile_process.stderr.decode())
        exit(1)

# Initialize variables
i = 1
max_time = [0, 0]
errors = []

# Iterate through test cases
while True:
    input_file = f"{tests_dir}{i:04}.in"
    output_file = f"{tests_dir}{i:04}.out"
    
    if not os.path.exists(input_file):
        break  # Exit loop if no more test cases

    start_time = time()

    try:
        # Run the command
        if lang == 'cpp':
            subprocess.run([executable], stdin=open(input_file), stdout=open(output_file, 'w'), check=True)
        else:
            subprocess.run(['python3', executable], stdin=open(input_file), stdout=open(output_file, 'w'), check=True)
        
        print(f'Executed {output_file}')
    except subprocess.CalledProcessError:
        print(f'Test {i:04} error')
        errors.append(i)

    exec_time = time() - start_time
    if exec_time > max_time[0]:
        max_time[0] = exec_time
        max_time[1] = i

    i += 1

# Report results
if errors:
    print('Following test cases created with errors:')
    for error in errors:
        print(f'{error:04}')
else:
    print('\nAll test cases without errors')
    print(f'The slowest test case: {max_time[1]} - {"%.4f" % max_time[0]} seconds')

# Clean up if C++
if lang == 'cpp':
    os.remove(executable)