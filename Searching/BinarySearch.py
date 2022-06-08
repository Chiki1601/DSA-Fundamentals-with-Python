#binary search
def Binarysearch(list,item):
    first = 0
    last = len(list) - 1
    
    found = False
    while(first <= last and not found):
        mid = (first + last)//2
        if list[mid] == item:
            found = True
        else:
            if item<list[mid]:
                last = mid - 1
            else:                
                first = mid + 1
    return found



myList = [4,12,7,45,52,71,64,84,27,72]
print("List has the items: ",myList)

searchNum = int(input("enter the number:"))

found = Binarysearch(myList,searchNum)

if found == True:   
    print(searchNum, " is present in the list ")
else:
    print(searchNum, "is not in the list")
