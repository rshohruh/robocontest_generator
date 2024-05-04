import os
import shutil
import sys

def main():
    # Prompt the user to enter the source directory
    source_dir = sys.argv[1]
    # Verify if the entered directory exists
    if not os.path.isdir(source_dir):
        print("Error: Source directory does not exist.")
        return

    # Set the destination directory
    destination_dir = "/home/rshohruh/Downloads/robocontest_generator/tests/"

    # Check if the destination directory exists, remove it if it does
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)

    # Recreate the destination directory
    os.makedirs(destination_dir)

    # Counter variable
    counter = 0

    # Loop through each .in file in the source directory
    for filename in os.listdir(source_dir):
        if filename.endswith(".in"):
            # Increment the counter
            counter += 1
            # Pad the counter with leading zeros
            padded_counter = str(counter).zfill(4)
            # Get the file extension
            _, extension = os.path.splitext(filename)
            # Create the new filename
            new_filename = f"{padded_counter}{extension}"
            # Copy the file to the destination directory with the new filename
            shutil.copy(os.path.join(source_dir, filename), os.path.join(destination_dir, new_filename))

if __name__ == "__main__":
    main()
