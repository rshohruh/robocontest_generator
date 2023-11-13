import os
from time import time

if not os.path.exists("tests"):
    os.system('mkdir tests')


start = int(input("Starting testcase: "))
end = int(input("Ending testcase: "))

for i in range(start, end + 1):
    os.system(f'python3 input.py > tests/{i:04}.in')

print(f'{end-start+1} .in files created')