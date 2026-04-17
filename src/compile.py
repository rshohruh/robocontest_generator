import os
import subprocess
import sys
from time import time

TIMEOUT = float(os.environ.get("TIMEOUT", 5))

# Optional: run only a specific test number
only = int(sys.argv[1]) if len(sys.argv) > 1 else None

lang = "cpp" if os.path.exists("env/solution.cpp") else "py"
tests_dir = "env/tests/"
executable = "env/solution"

if lang == "cpp":
    result = subprocess.run(
        ["g++", "-O2", "-o", executable, "env/solution.cpp"],
        capture_output=True,
    )
    if result.returncode != 0:
        print("Compilation failed:")
        print(result.stderr.decode())
        sys.exit(1)
    print("Compiled successfully\n")

cmd = [executable] if lang == "cpp" else ["python3", "env/solution.py"]

i = 1
max_time = (0.0, 0)
errors = []

while True:
    input_file = f"{tests_dir}{i:04}.in"
    output_file = f"{tests_dir}{i:04}.out"

    if not os.path.exists(input_file):
        break

    if only is not None and i != only:
        i += 1
        continue

    start_time = time()
    try:
        with open(input_file) as fin, open(output_file, "w") as fout:
            subprocess.run(cmd, stdin=fin, stdout=fout, check=True, timeout=TIMEOUT)
        elapsed = time() - start_time
        print(f"Test {i:04}: {elapsed:.3f}s")
        if elapsed > max_time[0]:
            max_time = (elapsed, i)
    except subprocess.TimeoutExpired:
        elapsed = time() - start_time
        print(f"Test {i:04}: TLE (>{TIMEOUT:.0f}s)")
        errors.append((i, "TLE"))
    except subprocess.CalledProcessError:
        print(f"Test {i:04}: Runtime Error")
        errors.append((i, "RE"))

    if only is not None:
        break
    i += 1

if lang == "cpp" and os.path.exists(executable):
    os.remove(executable)

total = i - 1 if only is None else 1
print(f"\n{total} test(s) run")
if errors:
    print("Errors:")
    for n, kind in errors:
        print(f"  {n:04}: {kind}")
elif only is None and max_time[1]:
    print(f"All passed. Slowest: {max_time[1]:04} ({max_time[0]:.3f}s)")
else:
    print("Passed")
