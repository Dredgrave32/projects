def binary_search(list, target): #Works only if the list is sorted
    first = 0
    last = len(list) - 1
    
    while first <= last:
        mid = (first + last) // 2 #Finds the middle index of the list rounded down
        
        if list[mid] == target:
            return mid
        elif list[mid] < target:
           first = mid + 1
        else:
            last = mid - 1
    return None

def verify(index):
    if  index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in List")
        
number = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(number, 12)
verify(result)

result = binary_search(number, 6)
verify(result)