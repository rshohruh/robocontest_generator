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

# Clean workspace
clean:
    rm -rf ./env/tests env/solution.cpp ./env/generator.py

# Archive testcases
archive:
    rm -f ./env/tests.zip
    zip -r ./env/tests.zip ./env/tests