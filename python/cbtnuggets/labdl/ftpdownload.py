# Adapted from effbot.org

import ftplib
import sys
import os

def ftext(ftp, filename, outfile=None):
    # fetch a text file
    if outfile is None:
        #outfile = sys.stdout
        outfile = open('C:/Python26/outfile.txt', 'w')
    # Lambda expression to add newlines to the lines read from the server
    ftp.retrlines("RETR " + filename, lambda s, w=outfile.write: w(s+"\n"))

def fbin(ftp, filename, outfile=None):
    # fetch a binary file
    if outfile is None:
        outfile = sys.stdout
    ftp.retrbinary("RETR " + filename, outfile.write)

ftp = ftplib.FTP("ftp.redhat.com")
ftp.login()
d = 'redhat/dst2007/README'
ftp.cwd(d)
ftext(ftp, "README_FIRST.txt")
#fbin(ftp, "README_FIRST.txt")
ftp.close()

print 'Current working directory is: ', os.getcwd(), '\n'



