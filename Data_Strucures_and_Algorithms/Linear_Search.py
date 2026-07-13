def linear_search(list, target):
    """
    Return the index of the target if found else returns None
    """
    #Runs in O(1) / Constant Time
    #Each loop of the for loop runs sequentially
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None
        

def verify(index):
    if  index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in List")
        
number = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(number, 12)
verify(result)

result = linear_search(number, 6)
verify(result)