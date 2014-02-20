Threader
========

Multi-threader with threadpool. 

Usage
=====

To use, create a mixin, then pass it a list of values. You can then process each value (i.e tasks) within your custom run_task function.

```
>>> from threader import Threader

>>> class ThreadTask():
>>>     def run_task(self,task):
>>>        print "run an action on task"
    
>>> class ThreadRunner(Threader,ThreadTask):
>>>     pass
    
>>> t = ThreadRunner(range(100))
>>> t.run_threads()

... threads are run
```

Note : Currently configured to use a maximum of 12 threads.
