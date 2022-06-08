myList = [4,12,7,45,52,71,64,84,27,72]
print("List has the items: ",myList)

searchNum = int(input("enter the number:"))
found = False
for i in range(len(myList)):
    if myList[i] == searchNum:
        fount = True
        print(searchNum, " is present in the list at index",i)
      
    else:
        print(searchNum, "is not in the list")
