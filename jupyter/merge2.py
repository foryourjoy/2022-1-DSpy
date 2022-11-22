from random import *

def merge(a, lo, mi, hi, aux):
    n = hi - lo
    i = lo
    j = mi
    for k in range(n):
        if   i == mi:     aux[k] = a[j]; j += 1
        elif j == hi:     aux[k] = a[i]; i += 1
        elif a[j] < a[i]: aux[k] = a[j]; j += 1
        else:             aux[k] = a[i]; i += 1
    a[lo:hi] = aux[0:n]
    
def _sort(a, lo, hi, aux):
    n = hi - lo
    if n <= 1: return
    
    mi = (lo + hi) // 2
    _sort(a, lo, mi, aux)
    _sort(a, mi, hi, aux)
    merge(a, lo, mi, hi, aux)

def sort(a):
    n = len(a)
    aux = [0] * n
    _sort(a, 0, n, aux)
    
if __name__ == "__main__":
    #a = [randint(10, 99) for i in range(20)]
    a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("before: ", a)
    sort(a)
    print(" after: ", a)
