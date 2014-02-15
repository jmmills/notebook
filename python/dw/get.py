from redis import Redis
from rq import Queue

import requests
import time
import timeit


class Get:

    def __init__(self, iterations):
        self.urls = []
        self.results = []
        self.iterations = iterations or 0
        self.timer = 0
        pass

    def fetch_one(self, url):
        raise Exception('Sub-classes must define fetch_one method')

    def fetch_multi(self, urls):
        return [self.fetch_one(url.rstrip()) for url in urls]

    def fetch(self):
        return self.fetch_multi(self.urls)

    def _read_urls(self, file):
        with open(file) as data:
            self.urls = list(data)

    def run(self, file):
        self._read_urls(file)
        #self.timer = timeit.timeit(_curried, number=self.iterations)
        self.results = self.fetch()

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

    def __init__(self, iterations, timeout):
        super(Distro, self).__init__(iterations)
        self.timeout = timeout
        self.jobs = []
        self.build_queue()

    def build_queue(self):
        raise Exception('define build_queue method')

    def get_result(self, obj):
        raise Exception('define get_result method')

    def return_result_list(self):
        return [self.get_result(job) for job in self.jobs]

    def the_jobs_are_not_done(self):
        done = len(list(self.return_result_list()))
        jobs = len(self.jobs)

        return done != jobs

    def time_is_up(self, t):
        return time.time() - t > self.timeout

    def wait_for_jobs(self):

        start = time.time();
        while self.the_jobs_are_not_done():
            if self.time_is_up(start):
                raise Exception('Reached fetch timeout')

    def fetch(self):
        self.jobs = super(Distro, self).fetch()
        self.wait_for_jobs()
        return self.return_result_list()


class RQ(Distro):

    def build_queue(self):
        self.q = Queue(connection=Redis())

    def get_result(self, obj):
        return obj.result

    def fetch_one(self, url):
        return self.q.enqueue(super(Distro, self).fetch_one, url)
