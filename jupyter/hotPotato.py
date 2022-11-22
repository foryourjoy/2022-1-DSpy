from queue import Queue

def hotPotato(namelist, num):
    que=Queue()
    for name in namelist:
        que.put(name)
    assert len(namelist) == que.qsize()
        
    while que.qsize() >1:
        for i in range(num):
            que.put(que.get())
        que.get()
    assert que.qsize() ==1
    return que.get()

if __name__=="__main__":
    namelist=['Bill','David','Susan','Jane']
    print("The winner is", hotPotato(namelist, 3))
