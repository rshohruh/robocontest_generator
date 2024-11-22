# Create new problem
new:
    rm -rf ./env
    mkdir ./env
    code ./env/solution.cpp
    code ./env/generator.py

# Generate testcases based on env/generator.py
generate start end:
    python3 ./src/generate.py {{start}} {{end}}

# Generate answers based on env/solution.cpp
compile:
    python3 ./src/compile.py

# Import tests from other source
import folder:
    rm -rf ./env/tests
    mkdir ./env/tests
    python3 ./src/import.py {{folder}}
    mv ./src/env/tests ./env
    rm -r ./src/env/

# Swap order of tests
swap-tests file1 file2:
    mv ./env/tests/{{ file1 }}.in dummy.in
    mv ./env/tests/{{ file1 }}.out dummy.out
    mv ./env/tests/{{ file2 }}.in ./env/tests/{{ file1 }}.in
    mv ./env/tests/{{ file2 }}.out ./env/tests/{{ file1 }}.out
    mv dummy.in ./env/tests/{{ file2 }}.in
    mv dummy.out ./env/tests/{{ file2 }}.out

# Clean workspace
clean:
    rm -rf ./env/tests env/solution.cpp ./env/generator.py

# Archive testcases
archive:
    rm -f ./env/tests.zip
    zip -r ./env/tests.zip ./env/tests