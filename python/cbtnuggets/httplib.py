#!/usr/bin/env python2.7
import httplib

files = ['/index.html','/doc/index.html']

h = httplib.HTTPConnection('www.python.org', 80)
h.connect()

for f in files:
    h.request('GET',f)
    r = h.getresponse()

    if r.status == httplib.OK:
        data = r.read()
        print(':::: %s ::::' + f)
        print(data)

f.close()
