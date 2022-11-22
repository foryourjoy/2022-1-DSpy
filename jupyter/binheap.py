from dspy.drawtree import draw_level_order 

class BinHeap:
    def __init__(self):                       # set more for min-heap, less for max-heap 
        self.heap = [0]                       # list, index 0 is not used
        self.N = 0                            # points the last valid heap element index
        self.comp = None                      # comparator to switch between min-heap & max-heap
        
    def swap(self, p, k):                     # swap two elements
        self.heap[p], self.heap[k] = self.heap[k], self.heap[p]

    def swim(self,i):                         # append key and swim up
        while i // 2 > 0:
            if self.heap[i] < self.heap[i // 2]:
                self.swap(i, i//2) 
            i = i // 2

    def insert(self, key):                     # check N and len(heap) before using
        self.heap.append(key)                  # append() or list index  
        self.N += 1  
        self.swim(self.N)

    def sink(self,i):                          # try this without using minChild()
        while (i * 2) <= self.N:               # code is shown above
            mc = self.minChild(i)
            if self.heap[i] > self.heap[mc]:
                self.swap(i, mc) 
            i = mc

    def minChild(self,i):                      # used in sink, but try not to use this
        if i * 2 + 1 > self.N:
            return i * 2
        else:
            if self.heap[i*2] < self.heap[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    
    def delete(self):
        retval = self.heap[1]                  # root is saved to return
        self.heap[1] = self.heap[self.N]       # last element becomes root - need sink it
        self.N -= 1                            # reduce size by one
        self.heap.pop()                        # remove the last element (it will be unnecessary)
        self.sink(1)                           # now, sink down the root to make it heap-ordered
        return retval
            
    def buildHeap(self, arr):                  # build heap from input arr list
        self.heap = [0] + arr[:]               # copy arr and set the initial heap
        self.N = len(arr)                      # set the size
        i = len(arr) // 2                      # get the last internal node
        while i > 0:                           # sink from the last internal node to root 1
            self.sink(i)                       # O(n) time complexity
            i -= 1
  
    def heapify(self):                         # build heap from existing self.heap
        self.buildHeap(self.heap[1:])
    
    def __str__(self):
        return str(list(bh.heap[1:]))
    
    def draw(self):                            # this works for numbers only
        draw_level_order(str(self.heap[1:]))
            
if __name__ == '__main__':
    bh = BinHeap()
    bh.buildHeap([9, 5, 6, 2, 3])
    print('number of elements N:', bh.N)
    print('  lengh of heap list:', len(bh.heap))
    print('    heap list stored:', bh.heap)
    bh.draw()
    
    print('\ninserting: 7 - already heap-ordered')
    bh.insert(7)
    bh.draw()
    print('\ninserting: 1 - swim up, become root')
    bh.insert(1)
    bh.draw()
    
    print('\ndeleting root to sort - heap depleted')
    bh_sorted = [ bh.delete() for x in range(bh.N) ]
    print('bh_sorted:', bh_sorted)
    print('number of elements N:', bh.N)
    print('  lengh of heap list:', len(bh.heap))
    print('    heap list stored:', bh.heap)
