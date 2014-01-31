#Adapted from ozoneasylum.com

import win32wnet
from win32netcon import RESOURCETYPE_DISK as DISK

drive_letter = "R:"
path = "\\\\192.168.1.106\\share"
win32wnet.WNetAddConnection2(DISK, drive_letter, path)
