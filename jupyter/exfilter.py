import sys

def binarysearch(arr, key, lo, hi):
    if lo>hi:
        return -1
    else:
        mid=(lo+hi)//2
        if arr[mid]==key:
            return 0
        else:
            if key<arr[mid]:
                return binarysearch(arr,key,lo,mid-1)
            else:
                return binarysearch(arr,key,mid+1,hi)
    
def search(arr, key):
    return binarysearch(arr,key,0,len(arr)-1)

if __name__ == "__main__":
    with open('dict.txt') as f:
        arr = f.read().splitlines()
    for line in sys.stdin:
        key = line.rstrip()
        if search(arr, key) < 0:
            print(key)              # not found in dict
