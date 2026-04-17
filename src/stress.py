"""Stress test: compare solution vs brute force using generator.py for inputs."""
import os
import subprocess
import sys
from time import time

N = int(sys.argv[1]) if len(sys.argv) > 1 else 100
TIMEOUT = float(os.environ.get("TIMEOUT", 5))


def compile_cpp(src, out):
    result = subprocess.run(["g++", "-O2", "-o", out, src], capture_output=True)
    if result.returncode != 0:
        print(f"Compilation failed for {src}:")
        print(result.stderr.decode())
        sys.exit(1)


sol_lang = "cpp" if os.path.exists("env/solution.cpp") else "py"
brute_lang = "cpp" if os.path.exists("env/brute.cpp") else "py"

if not os.path.exists("env/generator.py"):
    print("Error: env/generator.py not found")
    sys.exit(1)

if sol_lang == "cpp":
    compile_cpp("env/solution.cpp", "env/solution")
    print("Compiled solution.cpp")
elif not os.path.exists("env/solution.py"):
    print("Error: env/solution.cpp or env/solution.py not found")
    sys.exit(1)

if brute_lang == "cpp":
    if not os.path.exists("env/brute.cpp"):
        print("Error: env/brute.cpp not found — create a brute force solution for stress testing")
        sys.exit(1)
    compile_cpp("env/brute.cpp", "env/brute")
    print("Compiled brute.cpp")
elif not os.path.exists("env/brute.py"):
    print("Error: env/brute.cpp or env/brute.py not found")
    sys.exit(1)

print(f"\nRunning {N} stress test(s) (timeout={TIMEOUT}s each)...\n")

sol_cmd = ["env/solution"] if sol_lang == "cpp" else ["python3", "env/solution.py"]
brute_cmd = ["env/brute"] if brute_lang == "cpp" else ["python3", "env/brute.py"]

passed = 0
for i in range(1, N + 1):
    gen = subprocess.run(
        ["python3", "env/generator.py", str(i)],
        capture_output=True, text=True,
    )
    if gen.returncode != 0:
        print(f"Test {i}: generator failed — {gen.stderr.strip()}")
        continue

    test_input = gen.stdout

    try:
        sol = subprocess.run(sol_cmd, input=test_input, capture_output=True, text=True, timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        print(f"Test {i}: FAIL — solution TLE (>{TIMEOUT:.0f}s)")
        print(f"Input:\n{test_input}")
        break

    try:
        brute = subprocess.run(brute_cmd, input=test_input, capture_output=True, text=True, timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        print(f"Test {i}: brute TLE — skipping")
        continue

    sol_out = sol.stdout.strip()
    brute_out = brute.stdout.strip()

    if sol_out != brute_out:
        print(f"Test {i}: FAIL")
        print(f"Input:\n{test_input}")
        print(f"Expected (brute):\n{brute_out}")
        print(f"Got (solution):\n{sol_out}")
        break

    passed += 1
    print(f"Test {i}: OK")

else:
    print(f"\nAll {passed} test(s) passed")

for path in ["env/solution", "env/brute"]:
    if os.path.exists(path):
        os.remove(path)
