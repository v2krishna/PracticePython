"""
  threading — Thread-based parallelism


 The Thread class represents an activity that is run in a separate thread of control.
 There are two ways to specify the activity: by passing a callable object to the constructor,
 or by overriding the run() method in a subclass. No other methods (except for the constructor)
 should be overridden in a subclass.


1) threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, daemon=None)
    This constructor should always be called with keyword arguments. Arguments are:

    group should be None; reserved for future extension when a ThreadGroup class is implemented.

    target is the callable object to be invoked by the run() method. Defaults to None,
            meaning nothing is called.

    name is the thread name. By default, a unique name is constructed of the form “Thread-N”
        where N is a small decimal number.

    args is the argument tuple for the target invocation. Defaults to ().

    kwargs is a dictionary of keyword arguments for the target invocation. Defaults to {}.

    If not None, daemon explicitly sets whether the thread is daemonic. If None (the default),
    the daemonic property is inherited from the current thread.

Methods of Threads:

1)start()
    Start the thread’s activity.

    It must be called at most once per thread object. It arranges for the object’s run() method to
    be invoked in a separate thread of control.

    This method will raise a RuntimeError if called more than once on the same thread object.

2)run()
    Method representing the thread’s activity.

    You may override this method in a subclass. The standard run() method invokes the callable
    object passed to the object’s constructor as the target argument, if any, with positional and
    keyword arguments taken from the args and kwargs arguments, respectively.

3) join(timeout=None)
    Wait until the thread terminates. This blocks the calling thread until the thread whose join()
    method is called terminates – either normally or through an unhandled exception – or until
    the optional timeout occurs.

---------------------------------------------------
threading.Lock:
    The class implementing primitive lock objects. Once a thread has acquired a lock,
    subsequent attempts to acquire it block, until it is released; any thread may release it.
Methods of Lock class:

1) acquire(blocking=True, timeout=-1)
    Acquire a lock, blocking or non-blocking.

    When invoked with the blocking argument set to True (the default), block until the lock is
    unlocked, then set it to locked and return True.

    When invoked with the blocking argument set to False, do not block. If a call with blocking set to
    True would block, return False immediately; otherwise, set the lock to locked and return True.

    When invoked with the floating-point timeout argument set to a positive value, block for at most
    the number of seconds specified by timeout and as long as the lock cannot be acquired. A timeout
    argument of -1 specifies an unbounded wait. It is forbidden to specify a timeout when blocking is
    false.

2)release()
    Release a lock. This can be called from any thread, not only the thread which has acquired the lock.

    When the lock is locked, reset it to unlocked, and return. If any other threads are blocked
    waiting for the lock to become unlocked, allow exactly one of them to proceed.

    When invoked on an unlocked lock, a RuntimeError is raised.

    There is no return value.

import threading, time
def square(seq):
    print("Calculating squares")
    for i in seq:
        print('square:',i*i)
        time.sleep(1)

def cube(seq):
    print("Calculating cubes")
    for i in seq:
        print('cube:',i**3)
        time.sleep(1)


l = [2,3,4,5,6,7]

t1 = threading.Thread(target=square,args=(l,))
t2 = threading.Thread(target=cube,args=(l,))

t1.start()
t1.join()
t2.start()
==================================================
import threading, time
tl = threading.Lock()

def timer(name,delay,repeat):
    print(f'{name} has started\n')
    tl.acquire()
    print(f'{name} has acquired lock')
    for i in range(repeat):
        print(f'{name}:{time.ctime(time.time())}')
        time.sleep(delay)
    print(f'{name} is releasing lock')
    tl.release()

t1 = threading.Thread(target=timer,args=('Thread-1', 1,3))
t2 = threading.Thread(target=timer,args=('Thread-2', 1,5))
t1.start()
t2.start()

"""
import threading, time

def add(a,b):
    print("Addition : ",a+b)

def sub(a,b):
    print("Subtraction : ",a-b)

def mult(a,b):
    print("Multiplication : ",a*b)


t1 = threading.Thread(target=add,args=(10,15))
t2 = threading.Thread(target=sub,args=(15,10))
t3 = threading.Thread(target=mult,args=(10,15))

l = [t1, t2,t3]
for i in l:
    i.start()
    time.sleep(2)

