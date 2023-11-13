import shutil
import sys
import os
title = sys.argv[1]
if os.path.exists(title):
    os.system(f'rm -r {title}')
shutil.copytree(src="src", dst=title)
print('succes')