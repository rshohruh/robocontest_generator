import os
from time import time

i = 1
input_file = f"tests/{i:04}.in"
output_file = f"tests/{i:04}.out"

lang = 'cpp' if os.path.exists('solution.cpp') else 'py'

max_time = [0, 0]
errors = []

command = 'g++ -o solution solution.cpp' if lang == 'cpp' else 'python3 solution.py'
while os.path.exists(input_file):
    start_time = time()
    
    try:
        os.system(f'{command} < {input_file} > {output_file}')
        print(f'test {i:04} ok')
    except:
        print(f'test {i:04} error')
        errors.append(i)

    exec_time = time() - start_time
    if max_time[0] < exec_time:
        max_time[0] = exec_time
        max_time[1] = i
    
    i += 1
    input_file = f"tests/{i:04}.in"
    output_file = f"tests/{i:04}.out"

if len(errors):
    print('following testcases created with errors:')
    for error in errors:
        print(f'{i:04}', sep='\t')
else:
    print('all testcases created succesfully')
    print(f'the slowest testcase: {max_time[1]}: {max_time[1]} seconds')
