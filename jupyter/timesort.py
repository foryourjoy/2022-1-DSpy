from stopwatch import Stopwatch
from timeit import repeat
import random 

def timeTrials(func, n, trials):
    ''' Run func for an array a of n random[0..1), performing the 
        experiment trials times. Return the minimum wall-clock time it 
        took to run function.'''
    total = 0.0
    for t in range(trials):
        a = [random.uniform(0, 1) for i in range(n)]
        watch = Stopwatch()
        func(a)
        total += watch.duration
    return total

def doublingTest(func, n, trials, max_n = 8192):
    '''Perform a doubling test of the performance of function func starting
       at n, doubling n until n reaches max_n or over and writing the ratio of 
       the time for the current n and the time for the previous n each time 
       through the loop. Perform trials for each n.'''

    print(f"{func.__module__}.{func.__name__}()")
    print('%10s %6s %10s' % ('n', 'ratio', 'elapsed'))
    while n <= max_n:
        prev = timeTrials(func, n // 2, trials)
        curr = timeTrials(func, n,      trials)
        ratio = curr / prev
        print('%10d %6.2f %10.3f' % (n, ratio, curr))
        n *= 2
        
def repeatTest(f, n, trials=5, number=10):
    # generate an array of `n` items consisting of random integer 
    # values between 0 and n
    a = [random.randint(0, n) for i in range(n)]
    
    # set up the context and prepare the call to the specified f using the array. 
    # Only import the sort function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {f}" if f != "sorted" else ""
    stmt = f"{f}.sort({a})"

    # execute timeit() 'trials'(default = 5) different times and 
    # return the time in seconds that each 'number' executions took
    # repeat: set number of timeit() calls, number: set timeit()'s number 
    times = repeat(setup=setup_code, stmt=stmt, repeat=trials, number=number)
    
    # display the funtion name, n and the minimu time it took 
    print(f"{f:>20s} {len(a):>7d} {min(times):10.4f}")
