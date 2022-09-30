def insertionSort(arr):
    for e in range(1, len(arr)):
        ind=e
        for b in range(e):
            if arr[ind-1] <= arr[ind]:
                break
            else:
                if ind:
                    temp=arr[ind]
                    arr[ind]=arr[ind-1]
                    arr[ind-1]=temp
                    ind-=1
                else:
                    break
                
    return arr

array=[8,2,2,5,4,7,10,9,4,8,6]
print(array)
print(insertionSort(array))
