# 코드 2
def mergeSort(a):
    print("Split:", a)
    if len(a)>1:
        mid = len(a)//2
        left = a[:mid]
        right = a[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
        
        print(' merge:', left, right)
        while i < len(left) and j < len(right):   
            if left[i] <= right[j]:
                a[k]=left[i]
                i=i+1
            else:
                a[k]=right[j]
                j=j+1
            k=k+1

        while i < len(left):
            a[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            a[k]=right[j]
            j=j+1
            k=k+1
    print("merged:", a)
    
if __name__ == '__main__':
    a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("before: ", a)
    mergeSort(a)
    print(" after: ", a)  
