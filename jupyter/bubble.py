# 코드 1
def sort(a):
    for passn in range(len(a)-1,0,-1):
        for i in range(passn):
            if a[i]>a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]

if __name__ == '__main__':
    a = [54,26,93,17,77,31,44,55,20]
    sort(a)
    print(a)
