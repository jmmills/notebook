#!/usr/bin/env python

from redis import Redis
from rq import Queue

from workermod import Foo

q = Queue(connection=Redis())

foo = Foo()
fun = foo.count_words_at_url

job = q.enqueue(fun, 'http://python.org')

while job.result is None:
    pass

print(job.result)
