import os
import shutil
import sys

GENERATOR = """\
import sys
import random

seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
random.seed(seed)

# Write your test generator here.
# sys.argv[1] is the test index — use it as a seed for reproducible tests.
n = random.randint(1, 10)
print(n)
print(*random.sample(range(1, 100), n))
"""

SOLUTION_CPP = """\
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Write your solution here

    return 0;
}
"""

BRUTE_CPP = """\
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Brute force solution for stress testing

    return 0;
}
"""


def main():
    if os.path.exists("env"):
        answer = input("env/ already exists. Overwrite? [y/N] ").strip().lower()
        if answer != "y":
            print("Aborted.")
            sys.exit(0)
        shutil.rmtree("env")

    os.makedirs("env/tests")

    with open("env/generator.py", "w") as f:
        f.write(GENERATOR)
    with open("env/solution.cpp", "w") as f:
        f.write(SOLUTION_CPP)
    with open("env/brute.cpp", "w") as f:
        f.write(BRUTE_CPP)

    print("Created:")
    print("  env/generator.py  — edit to generate varied test inputs")
    print("  env/solution.cpp  — your main solution")
    print("  env/brute.cpp     — brute force for stress testing")
    print("  env/tests/        — test cases go here")


if __name__ == "__main__":
    main()
