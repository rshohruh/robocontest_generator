# Create new problem
new:
    rm -rf env
    mkdir env
    code env/solution.cpp
    code env/generator.py

# Generate testcases based on env/generator.py
generate start end:
    python3 src/generate.py {{start}} {{end}}

# Generate answers based on env/solution.cpp
compile:
    python3 src/compile.py

# Export tests from other source
export folder:
    rm -rf env/tests
    mkdir env/tests
    python3 src/export.py {{folder}}