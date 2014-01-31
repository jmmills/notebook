#from code.activestate.com

import os

def dirwalk(dir):
    "walk a directory tree, using a generator"
    for f in os.listdir('C:/files2'):
        fullpath = os.path.join('C:/files2',f)
        if os.path.isdir(fullpath) and not os.path.islink(fullpath):
            for x in dirwalk(fullpath):  # recurse into subdir
                yield x
        else:
            yield fullpath
