# 코드 1

def gapInsertionSort(a,start,gap):
    for i in range(start+gap,len(a),gap):

        currentvalue = a[i]
        position = i

        while position>=gap and a[position-gap]>currentvalue:
            a[position]=a[position-gap]
            position = position-gap

        a[position]=currentvalue
        
def sort(a):
    sublistcount = len(a)//2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(a,startposition,sublistcount)
        # print("After increments of size",sublistcount, "The list is",a)
        sublistcount = sublistcount // 2
        
if __name__ == '__main__':
    a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("before: ", a)
    sort(a)
    print(" after: ", a)    
