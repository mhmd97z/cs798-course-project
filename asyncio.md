## Useful links
- https://realpython.com/async-io-python/

This documnet explains Async IO in Python, which is used in airhop eSON app.


Async IO is a concurrent programming design that has received dedicated support in Python, evolving rapidly from Python 3.4 through 3.7

Async IO is a bit lesser known than its tried-and-true cousins, multiprocessing and threading.

## Where Does Async IO Fit In?
### Existing methods
**Parallelism** consists of performing multiple operations at the same time. **Multiprocessing** is a means to effect parallelism, and it entails spreading tasks over a computer’s central processing units (CPUs, or cores). Multiprocessing is well-suited for CPU-bound tasks: tightly bound for loops and mathematical computations usually fall into this category.

**Concurrency** is a slightly broader term than parallelism. It suggests that multiple tasks have the ability to run in an overlapping manner. (There’s a saying that concurrency does not imply parallelism.)

**Threading** is a concurrent execution model whereby multiple threads take turns executing tasks. One process can contain multiple threads. Python has a complicated relationship with threading thanks to its GIL, but that’s beyond the scope of this article.

What’s important to know about threading is that it’s better for IO-bound tasks. While a CPU-bound task is characterized by the computer’s cores continually working hard from start to finish, an IO-bound job is dominated by a lot of waiting on input/output to complete.

To recap the above, **concurrency** encompasses both **multiprocessing** (ideal for CPU-bound tasks) and **threading** (suited for IO-bound tasks). **Multiprocessing** is a form of **parallelism**, with **parallelism** being a specific type (subset) of **concurrency**. The Python standard library has offered longstanding support for both of these through its _multiprocessing_, _threading_, and _concurrent.futures_ packages.

### New(!) method
Now it’s time to bring a new member to the mix. Over the last few years, a separate design has been more comprehensively built into CPython: asynchronous IO, enabled through the standard library’s asyncio package and the new async and await language keywords. To be clear, **async IO** is not a newly invented concept, and it has existed or is being built into other languages and runtime environments, such as Go, C#, or Scala.

The asyncio package is billed by the Python documentation as a library to write concurrent code. However, async IO is not threading, nor is it multiprocessing. It is not built on top of either of these.

In fact, async IO is a single-threaded, single-process design: it uses **cooperative multitasking**. async IO gives a _feeling of concurrency_ despite using a single thread in a single process. _Coroutines_ (a central feature of async IO) can be scheduled concurrently, but they are not inherently concurrent.

To reiterate, async IO is a style of concurrent programming, but it is not parallelism. It’s more closely aligned with threading than with multiprocessing but is very much distinct from both of these and is a standalone member in concurrency’s bag of tricks.

## Async IO Explained
Chess example: consider one player who watns to play with 24 amateur players! Two options: 
- Synchronous version: plays one game at a time, never two at the same time, until the game is complete.
- Asynchronous version: moves from table to table, making one move at each table, leaving the table and lets the opponent make their next move during the wait time
This second method saves lots of time! 

So, cooperative multitasking is a fancy way of saying that a program’s event loop (more on that later) communicates with multiple tasks to let each take turns running at the optimal time. Async IO takes long waiting periods in which functions would otherwise be blocking and allows other functions to run during that downtime. (A function that blocks effectively forbids others from running from the time that it starts until the time that it returns.)

## Async IO Is Not Easy
The truth is that building durable multithreaded code can be hard and error-prone. Async IO avoids some of the potential speedbumps that you might otherwise encounter with a threaded design.

But that’s not to say that async IO in Python is easy. Be warned: when you venture a bit below the surface level, async programming can be difficult too! Python’s async model is built around concepts such as callbacks, events, transports, protocols, and futures—just the terminology can be intimidating. The fact that its API has been changing continually makes it no easier.

Luckily, _asyncio_ has matured to a point where most of its features are no longer provisional, while its documentation has received a huge overhaul and some quality resources on the subject are starting to emerge as well.

## The asyncio Package and async/await
At the heart of async IO are _coroutines_. A _coroutine_ is a specialized version of a Python generator function. Let’s start with a baseline definition and then build off of it as you progress here: a _coroutine_ is a function that can suspend its execution before reaching return, and it can indirectly pass control to another _coroutine_ for some time.

``` Python
import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
```

Output: 
``` Bash
$ python3 countasync.py
One
One
One
Two
Two
Two
countasync.py executed in 1.01 seconds.
```

The usual vesrion: 
``` Python
import time

def count():
    print("One")
    time.sleep(1)
    print("Two")

def main():
    for _ in range(3):
        count()

if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
```

Output:
``` Bash
$ python3 countsync.py
One
Two
One
Two
One
Two
countsync.py executed in 3.01 seconds.
```
While using time.sleep() and asyncio.sleep() may seem banal, they are used as stand-ins for any time-intensive processes that involve wait time. (The most mundane thing you can wait on is a sleep() call that does basically nothing.) That is, time.sleep() can represent any time-consuming blocking function call, while asyncio.sleep() is used to stand in for a non-blocking call (but one that also takes some time to complete).

As you’ll see in the next section, the benefit of awaiting something, including asyncio.sleep(), is that the surrounding function can temporarily cede control to another function that’s more readily able to do something immediately. In contrast, time.sleep() or any other blocking call is incompatible with asynchronous Python code, because it will stop everything in its tracks for the duration of the sleep time.

## The Rules of Async IO

- The syntax _async def_ introduces either a **native coroutine** or an **asynchronous generator**. The expressions _async with_ and _async for_ are also valid, and you’ll see them later on.
- The keyword _await_ passes function control back to the event loop. (It suspends the execution of the surrounding coroutine.) If Python encounters an _await f()_ expression in the scope of _g()_, this is how await tells the event loop, “Suspend execution of _g()_ until whatever I’m waiting on—the result of _f()_—is returned. In the meantime, go let something else run.”
``` Python 
async def g():
    # Pause here and come back to g() when f() is ready
    r = await f()
    return r
```

- A function that you introduce with _async def_ is a **coroutine**. It may use await, return, or yield, but all of these are optional. Using await and/or return creates a coroutine function. To call a coroutine function, you must await it to get its results.
- Just like it’s a SyntaxError to use yield outside of a def function, it is a SyntaxError to use await outside of an async def coroutine. You can only use await in the body of coroutines.
``` Python
async def f(x):
    y = await z(x)  # OK - `await` and `return` allowed in coroutines
    return y

async def g(x):
    yield x  # OK - this is an async generator

async def m(x):
    yield from gen(x)  # No - SyntaxError

def m(x):
    y = await z(x)  # Still no - SyntaxError (no `async def` here)
    return y
```

## Async IO Design Patterns
