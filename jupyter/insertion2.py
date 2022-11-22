def sort(a):
    for i in range(1, len(a)):
        j=i
        ivalue = a[i]
        while j > 0 and a[j - 1] > ivalue:
            j = j - 1
        a[j:i+1]=[a[i]]+a[j:i]
        
if __name__ == '__main__':
    a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("before:", a)
    sort(a)
    print(" after:", a)
