import time
import subprocess
import os


s = ""
k, task_id = 0, 0
mx_time, time_taken = 0, 0
i = 1
input_file = f"tests/{i:04}.in"
output_file = f"tests/{i:04}.out"
while os.path.exists(input_file):
    if os.name == 'nt':
        s = f"py main.py < {input_file} > {output_file}"
    else:
        s = f"python3 main.py < {input_file} > {output_file}"

    start = time.time()
    k = os.system(s)
    end = time.time()

    time_taken = round(end - start, 5)
    if k == 0:
        print(f"Test {i:04} OK Time: {time_taken} sec")
        
        if mx_time < time_taken:
            task_id = i
            mx_time = time_taken
    else:
        print(f"Test {i:04} ERROR Code {k}")

    i += 1
    input_file = f"tests/{i:04}.in"
    output_file = f"tests/{i:04}.out"

print(f"\nThe slowest task is {task_id:04} Time: {mx_time} sec")
