#!/usr/bin/env python

import sys
import get

std = get.Std(1)
file = sys.argv[1]

std.run(file)
print(std.stopwatch())
