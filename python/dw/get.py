from redis import Redis
from rq import Queue

import requests

class Get:

    def __init__(self):
        pass

    def fetch_one(self, url):
        raise Exception('Sub-classes must define fetch_one method')

    def fetch_multi(self, urls):
        return [self.fetch_one(url.rstrip()) for url in urls]

class Std(Get):

    def fetch_one(self, url):
        r = requests.get(url)
        return [url, r.status_code]

class RQ(Get):

    def __init__(self, rq):
        self.rq = rq

    def fetch_one(self, url):
        result = q.enq

