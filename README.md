Threader
========

Multi-threader with threadpool. 

Usage
=====

To use, create a class using Threader as the base class. Then build your task function. The task function must be named `run_task`.

```
from threader import Threader

class ThreadTask(Threader):
     def run_task(self,task):
         print "run an action on task"
 
t = ThreadTask(range(100))
t.run_threads()

# to set the thread pool size max_pool can be used. Default is 12.
t = ThreadTask(range(100),max_pool=100)
```
