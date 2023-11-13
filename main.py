import shutil
import sys
import os
title = sys.argv[1]
os.system(f'rm -r {title}')
shutil.copytree(src="src", dst=title)
print('succes')