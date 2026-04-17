import os
import subprocess
import sys

os.makedirs("env/tests", exist_ok=True)

try:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    if start < 1 or end < start:
        raise ValueError("start must be >= 1 and end >= start")
except (IndexError, ValueError) as e:
    print(f"Usage: generate.py <start> <end>")
    print(f"Error: {e}")
    sys.exit(1)

errors = []
for i in range(start, end + 1):
    input_file = f"env/tests/{i:04}.in"
    try:
        with open(input_file, "w") as f:
            subprocess.run(["python3", "env/generator.py", str(i)], stdout=f, check=True)
        print(f"Created: {input_file}")
    except subprocess.CalledProcessError:
        print(f"Error: failed to generate test {i:04}")
        errors.append(i)

if errors:
    print(f"\nFailed: {', '.join(f'{e:04}' for e in errors)}")
else:
    print(f"\nGenerated {end - start + 1} test case(s) successfully")
