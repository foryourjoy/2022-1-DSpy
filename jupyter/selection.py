# 코드 3
def sort(a):
    for fillslot in range(len(a)-1,0,-1):
        maxslot=0
        for slot in range(1,fillslot+1):
            if a[slot]>a[maxslot]:
                maxslot = slot
        a[fillslot], a[maxslot] = a[maxslot], a[fillslot]

if __name__ == '__main__':
    a = [54,26,93,17,77,31,44,55,20]
    sort(a)
    print(a)
