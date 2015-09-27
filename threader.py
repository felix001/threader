import re,Queue,traceback,urllib2,glob
from threading import Thread

class ThreadPool(object):
    """
    thread pool to limit number of concurrent threads
    """

    def __init__(self, no=10):
        self.alive = True
        self.tasks = Queue.Queue()
        self.threads = []
        for _ in range(no):
            t = Thread(target=self._worker)
            t.start()
            self.threads.append(t)

    def _worker(self):
        while self.alive:
            try:
                fn, args, kwargs = self.tasks.get(timeout=0.5)
            except Queue.Empty:
                continue
            except ValueError:
                self.tasks.task_done()
                continue

            try:
                fn(*args, **kwargs)
            except Exception:
                traceback.print_exc()

            self.tasks.task_done()

    def get_qsize(self):
        return self.tasks.qsize()
    
    def run_threads(self, fn, args=[], kwargs={}):
        self.tasks.put((fn, args, kwargs))

    def join(self):
        self.tasks.join()

    def deactivate(self):
        self.alive = False
        for t in self.threads:
            t.join()

class Threader:
    """
    multi threaded class. input list of tasks and return list of results.
    """

    def __init__(self,tasks,max_pool=12):
        self.q = Queue.Queue()
        self.results = dict()
        self.tasks = tasks
        self.max_threadpool = max_pool

    def _assign_task(self,q,task):
        self.q.put(self._run_task(task))

    def run_task(self,task):
        # self.results.update({task:"complete"})

    def run_threads(self):
        tp = ThreadPool(self.max_pool)
        for i in self.tasks:
            tp.run_threads(self._assign_task, args=(self.q, i))
        tp.join()
        tp.deactivate()

        return self.results
