def sort(a):
    for i in range(1, len(a)):  
        ivalue = a[i]  
        while i > 0 and a[i - 1] > ivalue:  
            a[i] = a[i - 1]
            i = i - 1
        a[i] = ivalue
        #print(i, "-", a) # enable to see each pass

if __name__ == '__main__':
    a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("before: ", a)
    sort(a)
    print(" after: ", a)
