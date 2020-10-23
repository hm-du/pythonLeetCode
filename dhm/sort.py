import time
import numpy

def display_time(func):
    def wrapper(*args):
        stime = time.time()
        func(*args)
        etime = time.time()
        print "cost time:"+str(etime -stime)
        print "------------------------------"
    return wrapper


@display_time
def bubbleSort(arr):
    lens = len(arr)
    while lens > 0 :
        i = lens
        lens = 0
        for j in range(0 , i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                lens = j+1
    print u"bubbleList:"+str(arr)


def partition(arr,left,right):
    pivot = arr[left]
    while left<right:
        while left <right and arr[right] >= pivot:
            right -= 1
        if left < right:
            arr[left] = arr [right]
        while left <right and arr[left] <= pivot:
            left += 1
        if left < right:
            arr[right] = arr [left]
    arr[left] = pivot
    return left
            

def quickSort(arr,left,right):
    if left < right:
        db=partition(arr, left, right)
        quickSort(arr, left, db - 1)
        quickSort(arr, db + 1, right)
    return arr

@display_time
def insertSort(arr):
    for i in range(1,len(arr)):
        cur = i
        temp = arr[i]
        while cur > 0 and arr[cur -1] >= temp :
            arr[cur] = arr[cur -1]
            cur -=1
        arr[cur] = temp
    print u"insertList:"+str(arr)  
    
def selectSort(arr):
    
    pass





if __name__=='__main__':

    # arrlist = [x * x for x in range(10000)]
    arrlist = list(numpy.random.randint(1000,size=200))
    print u"List:"+str(arrlist)
    # bubbleSort(arrlist)
#     r = quickSort(arrlist,0,len(arrlist)-1)
#     print u"quickList:"+str(arrlist)
    insertSort(arrlist)
    
    
    