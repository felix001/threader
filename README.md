Threader
========

Multi-threader with threadpool. Currently configured to use a maximum of 12 threads.
Further code for each task (thread) can be added to ```Thread()._run.task()```. 

Usage
=====

```
>>> from threader import Threader
>>> t = Threader(range(100))
>>> t.run_threads()

... threads are run
```
