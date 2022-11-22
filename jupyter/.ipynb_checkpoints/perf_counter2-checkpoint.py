from collections import deque
from time import perf_counter  # performance counter

def list_timing(NSIZE, TIMES):
    alist = list(range(NSIZE))
    start = perf_counter()
    for i in range(TIMES):
        alist.insert(0, i)
    return perf_counter() - start

def deq_timing(NSIZE, TIMES):
    adeq=deque(range(NSIZE))
    start=perf_counter()
    for i in range(TIMES):
        adeq.appendleft(i)
    return perf_counter()-start

if __name__ == '__main__':
    NSIZE = 100_000
    TIMES = 100_000
    list_time = list_timing(NSIZE, TIMES)       
    print(f"     list.insert() {list_time:>12.6} sec")
    deq_time = deq_timing(NSIZE, TIMES)       
    print(f"deque.appendleft() {deq_time:>12.6} sec")
    ratio = list_time / deq_time
    print(f"  list/deque ratio {ratio:>12.6} x faster")
