# 코드 3
def sort(a):
    qsort(a,0,len(a)-1)

def qsort(a,first,last):
    if first<last:
        splitpoint = partition(a,first,last)

        qsort(a,first,splitpoint-1)
        qsort(a,splitpoint+1,last)

def partition(a,first,last):
    pivotvalue = a[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and a[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while a[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            a[leftmark], a[rightmark] = a[rightmark], a[leftmark]

    a[first], a[rightmark] = a[rightmark], a[first]

    return rightmark

if __name__ == '__main__':
    a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("before: ", a)
    sort(a)
    print(" after: ", a)  
