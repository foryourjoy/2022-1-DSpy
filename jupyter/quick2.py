# This function takes last element as pivot, places the pivot element at its
# correct position in sorted array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right of pivot.
def partition(a, lo, hi):
    print(f'   partition: {lo} ~ {hi}')
    pivot = a[hi]                   # pivot
    i = lo - 1;                     # last index of smaller element on the left
    j = lo
    num_comp=0
    while j <= hi - 1:              # traverse the array
        num_comp+=1
        if a[j] < pivot:            # look for element less than pivot
            i += 1                  # increment only when a[j] is less than pivot
            if i != j:              # swap: smaller to left and greater to right
                a[j], a[i] = a[i], a[j]
                print(f'swap ({i} {j}):({a[i]} {a[j]}) {a}')
        j += 1
    
    a[hi], a[i+1] = a[i+1], a[hi]   # move the pivot at the position sorted
    #print(f'   number of comparison: {num_comp}')
    print(f'   move pivot: {hi}->{i+1}')
    print(f'   partitioned({pivot}) {a[lo:hi+1]} returns {i+1}')
    return i + 1                    # return index where pivot moved and sorted

# qsort helper function for recursive operation
# a: array to be sorted, lo: starting index, h: ending index
def qsort(a, lo, hi):
    if lo >= hi: return             # done, we have an empty array
    
    pi = partition(a, lo, hi)       # partition, get index of the pivot sorted
    print(f'    sort(le): {lo} ~ {pi-1}')
    qsort(a, lo, pi - 1)            # sort left of the pivot
    print(f'    sort(ri): {pi+1} ~ {hi}')
    qsort(a, pi + 1, hi)            # soft right of the pivot
    
    
def sort(a):
    qsort(a, 0, len(a) - 1)

if __name__ == "__main__":
    #a = [random.randint(10, 50) for i in range(15)]
    a = [32, 23, 81, 43, 92, 39, 57, 16, 75, 65]
    print('            input:', a)
    sort(a)
    print('           output:', a)
