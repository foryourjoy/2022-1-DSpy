from collections import deque
from time import perf_counter  # performance counter

def perf_timeit(NSIZE, TIMES):
    alist = list(range(NSIZE))
    adeq = deque(range(NSIZE))

    def elapsed(func):         # a helper function
        start = perf_counter()
        for i in range(TIMES):
            func(i)
        return perf_counter() - start
    
    list_time = elapsed(lambda x:alist.insert(0,x))
    deq_time  = elapsed(lambda x:adeq.appendleft(x))
    return list_time, deq_time

if __name__ == '__main__':
    list_time = []    # list of list_time values
    deque_time = []   # list of deque_time values
    n = []            # list of samples or i for plotting
    for i in range(20_000, 1_000_001, 20_000):
        l,d=perf_timeit(i,100)
        list_time.append(l)
        deque_time.append(d)
        n.append(i)