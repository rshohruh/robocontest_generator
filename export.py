import os
import shutil
import sys

def main():
    src = sys.argv[1]
    if not os.path.isdir(src):
        print("Source directory does not exist!!!")
        return

    dest = "/home/rshohruh/robocontest_generator/tests/"

    if os.path.exists(dest):
        shutil.rmtree(dest)

    os.makedirs(dest)
    counter = 3
    for filename in os.listdir(src):
        counter = int(filename.split('.')[-1])
        if 'dummy' not in filename: counter += 2
        name = str(counter).zfill(4)
        suffix = filename.split('.')[-2]
        # if suffix == "out": continue
        new_filename = f"{name}.{suffix}"
        
        shutil.copy(os.path.join(src, filename), os.path.join(dest, new_filename))
        counter += 1

if __name__ == "__main__":
    main()


# add to terminal alias export="/home/rshohruh/robocontst_generator/export.py"