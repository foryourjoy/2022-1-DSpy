class QueueCircular:
    def __init__(self,size):
        self.items=[None]*size
        self.MAX=size
        self.front=-1
        self.back=-1
    
    def __repr__(self):
        '''
        is_empty=True
        for items in self.items:
            if items != None:
                is_empty=False
        if is_empty==True:
        '''
        return f"QueueCircular({self.items})"
        
    def enqueue(self,item): #if not full
        if (self.back+1)%self.MAX ==self.front: #queue is full
            print("The circular queue is full")
        elif self.front==-1: #빈 queue에 처음 담을 때
            self.front=0
            self.back=0
            self.items[self.back]=item
        else:
            self.back=(self.back+1)%self.MAX # 그다음 칸에 enqueue
            self.items[self.back]=item
    
    def dequeue(self): #if not empty
        if self.front==-1: #비어있을때
            print("The circular queue is empty")
        elif self.front==self.back: #??
            temp=self.items[self.front]
            self.front=-1
            self.back=-1
            self.items[self.back]=temp
        else:#??
            temp=self.items[self.front]
            self.front=(self.front+1)%self.MAX
            return temp
if __name__=='__main__':
    q=QueueCircular(10)
    q.enqueue(12)
    q.enqueue(17)
    q.enqueue(25)
    q.enqueue(11)
    q.dequeue()
    q.dequeue()
    q.enqueue(30)
    
    print(f"Front: {q.front} points ({q.items[q.front]})")
    print(f"Back: {q.back} points ({q.items[q.back]})")
