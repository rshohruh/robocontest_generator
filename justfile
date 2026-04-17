# Initialize new problem workspace with template files
new:
    python3 ./src/new.py

# Generate test inputs from start to end (inclusive)
# generator.py receives the test index as sys.argv[1]
generate start end:
    python3 ./src/generate.py {{start}} {{end}}

# Generate a single test input
gen n:
    python3 ./src/generate.py {{n}} {{n}}

# Run solution on all tests, producing .out files
# Set TIMEOUT env var to change per-test limit (default: 5s)
compile:
    python3 ./src/compile.py

# Run solution on a single test only
run n:
    python3 ./src/compile.py {{n}}

# Stress test: compare solution vs brute force for N random tests (default: 100)
stress n="100":
    python3 ./src/stress.py {{n}}

# Manually add a test case by typing input (Ctrl+D to finish)
add:
    python3 ./src/add.py

# Show input (and output if available) for a test
view n:
    @echo "=== {{n}}.in ==="
    @cat env/tests/{{n}}.in
    @[ -f env/tests/{{n}}.out ] && printf "\n=== {{n}}.out ===\n" && cat env/tests/{{n}}.out || true

# List all test cases
list:
    @ls env/tests/*.in 2>/dev/null | wc -l | xargs -I{} echo "{} test case(s):" && ls env/tests/*.in 2>/dev/null | xargs -n1 basename | sed 's/\.in//' || echo "No tests found"

# Import and renumber tests from an external directory
import folder:
    rm -rf ./env/tests
    mkdir -p ./env/tests
    python3 ./src/import.py {{folder}}

# Swap two test case numbers (e.g. just swap 0001 0003)
swap file1 file2:
    mv ./env/tests/{{file1}}.in /tmp/_swap.in
    mv ./env/tests/{{file1}}.out /tmp/_swap.out
    mv ./env/tests/{{file2}}.in ./env/tests/{{file1}}.in
    mv ./env/tests/{{file2}}.out ./env/tests/{{file1}}.out
    mv /tmp/_swap.in ./env/tests/{{file2}}.in
    mv /tmp/_swap.out ./env/tests/{{file2}}.out

# Archive test cases into env/tests.zip (inputs and outputs only, no subdirectory)
archive:
    rm -f ./env/tests.zip
    zip -j ./env/tests.zip ./env/tests/*.in ./env/tests/*.out
    @echo "Archived to env/tests.zip"

# Remove the entire env/ workspace
clean:
    rm -rf ./env
