"""Append a manually typed test case as the next numbered .in file."""
import os
import sys

tests_dir = "env/tests"
os.makedirs(tests_dir, exist_ok=True)

existing = sorted(f for f in os.listdir(tests_dir) if f.endswith(".in"))
n = len(existing) + 1
path = f"{tests_dir}/{n:04}.in"

print(f"Enter input for test {n:04} (Ctrl+D when done):")
try:
    data = sys.stdin.read()
except KeyboardInterrupt:
    print("\nAborted.")
    sys.exit(0)

with open(path, "w") as f:
    f.write(data)

print(f"Saved to {path}")
