def mergeSort(myList):


    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        
        mergeSort(left)
        mergeSort(right)

        
        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              
              myList[k] = left[i]
              
              i += 1
            else:
                myList[k] = right[j]
                j += 1
           
            k += 1

        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

    else:
        return myList

    
print("-------------------------------------------------------------")
myList =[]
while True:
    num = input("Enter the number( then press the 'q' key to exit): ")
    if num == 'q':
       
      break
    else:
        myList.append(int(num))

mergeSort(myList)
print("-------------------------------------------------------------")
print("Merge sort:",myList)


input()