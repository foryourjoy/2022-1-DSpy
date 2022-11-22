import sys
from dspy import stdio  

# this insertion sort may run slower than others on purpose
def sort(a):  
    n = len(a)
    for i in range(1, n):
        j = i
        while j > 0 and a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
            j = j - 1
if __name__ == '__main__':   
    a = stdio.readAllStrings()
    for s in a: print(s, end = ' ')
    print()
    sort(a)
    for s in a: print(s, end = ' ')
    print()
