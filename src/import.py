import os
import shutil
import sys

def get_new_filename(counter, suffix):
    """Generate a new filename based on the counter and suffix."""
    name = str(counter).zfill(4)
    return f"{name}.{suffix}"

def process_files(src, dest):
    """Process files in the source directory and copy them to the destination."""
    counter = 1
    dummy_tests = []
    main_tests = []

    # First, categorize files into dummy and other files
    for filename in os.listdir(src):
        if 'out' in filename:
            continue
        if 'dummy' in filename:
            dummy_tests.append(filename)
        else:
            base_name, suffix, number = filename.split('.')
            c = 0
            if number[-1] > '9':
                c = ord(number[-1]) - ord('a')
                number = number[:-1]
            main_tests.append((int(number), c, filename))

    # Sort files to maintain order
    dummy_tests.sort()
    main_tests.sort()

    # Process dummy files
    for old_input_file in dummy_tests:
        old_output_file = old_input_file.replace('in', 'out')
        new_input_file = get_new_filename(counter, 'in')
        new_output_file = get_new_filename(counter, 'out')
        
        try:
            shutil.copy(os.path.join(src, old_input_file), os.path.join(dest, new_input_file))
            print(f'Copied: {old_input_file} -> {new_input_file}')

            shutil.copy(os.path.join(src, old_output_file), os.path.join(dest, new_output_file))
            print(f'Copied: {old_output_file} -> {new_output_file}')
        except IOError as e:
            print(f"Error copying file: {e}")
        
        counter += 1

    # Process other files
    for number, c, old_input_file in main_tests:
        old_output_file = old_input_file.replace('in', 'out')
        new_input_file = get_new_filename(counter, 'in')
        new_output_file = get_new_filename(counter, 'out')
        
        try:
            shutil.copy(os.path.join(src, old_input_file), os.path.join(dest, new_input_file))
            print(f'Copied: {old_input_file} \t -> {new_input_file}')

            shutil.copy(os.path.join(src, old_output_file), os.path.join(dest, new_output_file))
            print(f'Copied: {old_output_file} \t -> {new_output_file}')
        except IOError as e:
            print(f"Error copying file: {e}")
        
        counter += 1

def main():
    if len(sys.argv) < 2:
        print("Usage: python export.py <source_directory>")
        sys.exit(1)

    src = sys.argv[1]
    if not os.path.isdir(src):
        print(f"Error: {src} is not a valid directory")
        sys.exit(1)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    dest = os.path.join(script_dir, "env", "tests")
    
    if not os.path.exists(dest):
        os.makedirs(dest)

    process_files(src, dest)

if __name__ == "__main__":
    main()