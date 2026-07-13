def liner_search(list, target):
    """
    Return the index of the target if found else returns None
    """
    #Runs in O(1) / Constant Time
    #Each loop of the for loop runs sequentially
    for i in range(0, len(list)):
        if list[i] == target:
            return i
        else:
            return None