#Bubble sort

def bubble_sort(arr):
    def swap(i,j):
        arr[i], arr[j] =  arr[j], arr[i]
        
    n = len(arr)
    swapped = True
    
    
    x = -1
    while swapped:
        swapped = False
        x = x+1
        for i in range(1,n-x):
            if arr[i-1]>arr[i]:
                swap(i-1,i)
                swapped = True
    return arr

myArr = [71,15,7,18,99]

print("Array before Sorting: ",myArr)


bubble_sort(myArr)
print("\n\nArray after Sorting: ",myArr)
