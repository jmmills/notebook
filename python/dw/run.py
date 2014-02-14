#!/usr/bin/env python

import sys
import get

std = get.Std()
urls = [x for x in sys.stdin]

for x in std.fetch_multi(urls):
    print('{0}: {1}'.format(x[0],x[1]))

