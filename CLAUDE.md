# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A test case generator and management system for [Robocontest](https://robocontest.uz), an Uzbek competitive programming platform. Users write a `generator.py` and a `solution.cpp` (or `solution.py`) per problem; this toolchain generates inputs, runs the solution to produce outputs, stress-tests against a brute force, and manages test file organization.

## Common Commands

All tasks run via the `just` task runner:

```bash
just new                       # Create env/ with template generator.py, solution.cpp, brute.cpp
just generate <start> <end>    # Generate test inputs start..end (generator.py gets index as argv[1])
just gen <n>                   # Generate a single test
just compile                   # Compile and run solution on all tests → produces .out files
just run <n>                   # Run solution on one test only
just stress [n]                # Compare solution vs brute.cpp/brute.py for n random tests (default 100)
just add                       # Type a test case manually (Ctrl+D to finish)
just view <n>                  # Print .in and .out for test n (e.g. just view 0001)
just list                      # List all test cases
just import <folder>           # Import + renumber tests from external directory
just swap <file1> <file2>      # Swap two test case numbers (e.g. just swap 0001 0003)
just archive                   # Zip all .in/.out into env/tests.zip
just clean                     # Delete entire env/ workspace
```

Set `TIMEOUT=<seconds>` env var to override the per-test time limit (default: 5s).  
Example: `TIMEOUT=2 just compile`

No external Python dependencies — only stdlib and `g++` are required.

## Architecture

### Runtime Directory Layout

Each problem lives in `env/` (git-ignored):

```
env/
├── solution.cpp      # Main solution (or solution.py for Python)
├── brute.cpp         # Brute force for stress testing (or brute.py)
├── generator.py      # Test case generator — receives test index as sys.argv[1]
└── tests/
    ├── 0001.in / 0001.out
    ├── 0002.in / 0002.out
    └── ...           # 4-digit zero-padded pairs, max 9999
```

### Source Scripts (`src/`)

| File | Role |
|------|------|
| `new.py` | Creates `env/` with template files; prompts before overwriting |
| `generate.py` | Runs `generator.py <i>` for each index i and writes stdout to `env/tests/NNNN.in` |
| `compile.py` | Detects language (C++ if `solution.cpp` exists), compiles with `-O2`, runs each `.in` with timeout, reports TLE/RE and slowest test. Accepts optional test number arg for single-test mode. |
| `stress.py` | Compiles both solution and brute, generates tests via `generator.py <i>`, compares outputs, stops and prints the failing input on first mismatch |
| `import.py` | Scans external folder for `.in` files, sorts `dummy*` first then by numeric+letter suffix, renumbers to `0001..N`, copies pairs to `env/tests/` |
| `add.py` | Reads stdin until EOF and saves as the next numbered `.in` file |

### Key Conventions

- Test files are always 4-digit zero-padded pairs: `0001.in` + `0001.out`.
- `generator.py` receives the test index as `sys.argv[1]` — use it as a `random.seed()` for reproducible, varied tests.
- `import.py` sort order: `dummy*` files first (sorted lexically), then main tests sorted by number then letter suffix (e.g., `1.in` → `1a.in` → `2.in`).
- `compile.py` removes the compiled binary (`env/solution`) after each run.
- `stress.py` removes both `env/solution` and `env/brute` after finishing.
- `testlib.h` (Codeforces library) is available for writing validators and checkers in C++.
