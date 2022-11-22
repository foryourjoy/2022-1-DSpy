from collections import deque
from time import perf_counter  # performance counter

NSIZE = 100_000
TIMES = 100_000
alist = list(range(NSIZE))
t_start = perf_counter()
for i in range(TIMES):
    alist.insert(0, i)
list_time = perf_counter() - t_start        
print(f"     list.insert() {list_time:>12.6} sec")

adeq = deque(range(NSIZE))
t_start = perf_counter()
for i in range(TIMES):
    adeq.appendleft(i)
deq_time = perf_counter() - t_start       
print(f"deque.appendleft() {deq_time:>12.6} sec")

ratio = list_time / deq_time
print(f"  list/deque ratio {ratio:>12.6} x faster")
