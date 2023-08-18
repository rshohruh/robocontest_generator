import shutil
import sys
import os
title = sys.argv[1]
try:
    shutil.copytree(src="src", dst=title)
except:
    print("This folder is already exist")