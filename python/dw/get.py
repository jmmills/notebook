from redis import Redis
from rq import Queue

import requests
import time
import timeit


class Get:

    def __init__(self, iterations):
        self.urls = []
        self.results = []
        self.iterations = iterations
        self.timer = 0
        pass

    def fetch_one(self, url):
        raise Exception('Sub-classes must define fetch_one method')

    def fetch_multi(self, urls):
        return [self.fetch_one(url.rstrip()) for url in urls]

    def _read_urls(self, file):
        with open(file) as data:
            self.urls = list(data)

    def run(self, file):
        self._read_urls(file)

        obj = self

        def _curried():
            obj.results = self.fetch_multi(obj.urls)

        self.timer = timeit.timeit(_curried, number=self.iterations)

        return self.results

    def stopwatch(self):
        return 'Ran {0} times, fetching {1} urls, took {2:.2f} seconds'.format(
            self.iterations,
            len(self.urls),
            self.timer
        )

class Std(Get):

    def fetch_one(self, url):
        r = requests.get(url)
        return [url, r.status_code]


class Distro(Get):

    def __init__(self, timeout):
        self.timeout = timeout
        self.q = self.build_queue()
        self.jobs = []

    def get_result(obj):
        raise Exception('define get_result method')

    def return_result_list(self):
        return [self.get_result(job) for job in self.jobs]

    def the_jobs_are_not_done(self):
        done = len(list(filter, self.return_result_list()))
        jobs = len(self.jobs)

        return done != jobs

    def time_is_up(self,t):
        return time.time() - t > self.timeout

    def wait_for_job(self):

        start = time.time();
        while self.the_jobs_are_not_done():
            if self.time_is_up(start):
                raise Exception('Reached fetch timeout')

    def fetch_multi(self, urls):
        self.jobs = super(Distro, self).fetch_mutli(urls)
        self.wait_for_job()
        return self.return_result_list()


class RQ(Distro):

    def __init__(self, timeout):
        self.q = Queue(connection=Redis())
        self.timeout = timeout

    def get_result(obj):
        return obj.result

    def fetch_one(self, url):
        return self.q.enqueue('fetch_one', url)
