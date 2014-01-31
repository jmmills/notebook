# Adapted from stackoverflow.com
# ActiveState Code is another great site

import os
import shutil
path=os.path.join("C:/", "files")
destination=os.path.join("\\192.168.1.106", "\share")
for r,d,f in os.walk(path):
     for files in f:
           if files.endswith(".txt"):
                 try:
                     shutil.copy(os.path.join(r,files) , destination)
                 except IOError as e:
                     print(e)
