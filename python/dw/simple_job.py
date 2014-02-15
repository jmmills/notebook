from redis import Redis
from rq import Queue

from workermod import Foo

q = Queue(connection=Redis())

def _curried(url):
    f = Foo()
    return f.count_words_at_url(url)

print(_curried('http://python.org'))

foo = Foo()
job = q.enqueue(foo.count_words_at_url, 'http://python.org')

while job.result is None:
    pass

print(job.result)
