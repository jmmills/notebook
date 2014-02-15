#!/usr/bin/env python

import sys
import get

try:
    file = sys.argv[1]
except:
    file = 'urls.txt'

rq = get.RQ(1, 3)  # run once and timeout after 3 seconds
rq.run(file)
print('RQ request,', rq.stopwatch())

std = get.Std(1)
std.run(file)
print('Std request,', std.stopwatch())

