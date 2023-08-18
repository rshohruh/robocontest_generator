import os
import subprocess
s = ""
k = 0
starting_test = input("Starting test: ")
if starting_test < 1:
    print("Error of number starting test")
    exit(0)

ending_test = input("Ending test: ")
if ending_test < 1:
    print("Error of number ending test")
    exit(0)

input_file = ""
for i in range(starting_test, ending_test+1):
    input_file = f"tests/{i:04}.in"
    if os.name == 'nt':
        s = f"py input.py > {input_file}"
    else:
        s = f"python3 input.py > {input_file}"
    
    k = subprocess.call(s, shell=True)

    if k == 0:
        print(f"Test {i:04} OK")
    else:
        print(f"Test {i:04} ERROR Code {k}")
