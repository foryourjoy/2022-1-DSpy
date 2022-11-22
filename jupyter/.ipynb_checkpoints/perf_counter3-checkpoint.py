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
    NSIZE = 100_000
    TIMES = 100_000
    list_time, deq_time = perf_timeit(NSIZE, TIMES)
    print(f"     list.insert() {list_time:>12.6} sec")
    print(f"deque.appendleft() {deq_time:>12.6} sec")
    ratio = list_time / deq_time
    print(f"  list/deque ratio {ratio:>12.6} x faster")