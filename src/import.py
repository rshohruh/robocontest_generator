import os
import shutil
import sys


def parse_main_test(filename):
    """Parse a main test filename like '1.in', '2a.in', '3.suffix.b.in'.
    Returns (number, letter_offset) for sorting, or None if unrecognized."""
    base = filename[:-3]  # strip '.in'
    parts = base.split(".")
    raw = parts[0]
    letter_offset = 0
    if raw and raw[-1].isalpha():
        letter_offset = ord(raw[-1]) - ord("a") + 1
        raw = raw[:-1]
    try:
        return (int(raw), letter_offset)
    except ValueError:
        return None


def process_files(src, dest):
    dummy_tests = []
    main_tests = []

    for filename in os.listdir(src):
        if not filename.endswith(".in"):
            continue
        if "dummy" in filename:
            dummy_tests.append(filename)
        else:
            key = parse_main_test(filename)
            if key is None:
                print(f"Warning: skipping unrecognized filename: {filename}")
                continue
            main_tests.append((*key, filename))

    dummy_tests.sort()
    main_tests.sort()

    counter = 1

    def copy_pair(old_in):
        nonlocal counter
        old_out = old_in[:-3] + ".out"
        new_in = f"{counter:04}.in"
        new_out = f"{counter:04}.out"
        try:
            shutil.copy(os.path.join(src, old_in), os.path.join(dest, new_in))
            print(f"  {old_in} -> {new_in}")
            out_src = os.path.join(src, old_out)
            if os.path.exists(out_src):
                shutil.copy(out_src, os.path.join(dest, new_out))
                print(f"  {old_out} -> {new_out}")
            else:
                print(f"  Warning: no .out found for {old_in}")
        except IOError as e:
            print(f"  Error copying {old_in}: {e}")
        counter += 1

    for f in dummy_tests:
        copy_pair(f)
    for *_, f in main_tests:
        copy_pair(f)

    print(f"\nImported {counter - 1} test case(s) to {dest}")


def main():
    if len(sys.argv) < 2:
        print("Usage: import.py <source_directory>")
        sys.exit(1)

    src = sys.argv[1]
    if not os.path.isdir(src):
        print(f"Error: '{src}' is not a valid directory")
        sys.exit(1)

    dest = os.path.join(os.getcwd(), "env", "tests")
    os.makedirs(dest, exist_ok=True)
    process_files(src, dest)


if __name__ == "__main__":
    main()
