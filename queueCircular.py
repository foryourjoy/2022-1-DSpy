
class QueueCircular:
    
    def __init__(self, size):
        self.items = [None] * size
        self.MAX = size
        self.front = -1
        self.back = -1
        
    def enqueue(self, item): # if not full
        if (self.back + 1) % self.MAX == self.front:
            print("The circular queue is full")
        elif self.front == -1:
            self.front = 0
            self.back = 0
            self.items[self.back] = item
        else:
            self.back = (self.back + 1) % self.MAX  
            self.items[self.back] = item

    def dequeue(self): # if not empty
        if self.front == -1:
            print("The circular queue is empty")
        elif self.front == self.back:
            temp = self.items[self.front]
            self.front = -1
            self.back = -1
            self.items[self.back] = temp
        else:
            temp = self.items[self.front]
            self.front = (self.front + 1) % self.MAX  
            return temp

    def is_empty():
        return self.front == -1

    def is_full():
        return self.front == (self.back + 1) % self.MAX or  \
               (self.front == 0 and self.back == self.MAX - 1)

    def __repr__(self):
        pstr = 'QueueCircular(['
        if self.front == -1:
            return pstr + '])'
        elif (self.back >= self.front):
            pstr += ', '.join([str(self.items[i]) for i in range(self.front, self.back + 1)])
        else:
            pstr += ', '.join([str(self.items[i]) for i in range(self.front, self.MAX)])
            pstr += ', '
            pstr += ', '.join([str(self.items[i]) for i in range(0, self.back + 1)])
        return pstr + '])'
    
if __name__ == '__main__':
    q = QueueCircular(4)  
    print(q)
    q.enqueue(12)  
    q.enqueue(17)  
    q.enqueue(25)  
    q.enqueue(11)  
    q.enqueue(30)
    print(q)
    q.dequeue()  
    q.dequeue()  
    print(q)
