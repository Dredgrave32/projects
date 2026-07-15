def merge_sort(list):
    """
    Sorts the list in Ascending order
    Returns a new sorted list
    
    Divides: Finds the mid index of the list and divides into sublists
    Conquer: Recursivley sorts the sublist created int the prev
    Combine: merge the sorted sublist created the prev step
    """
    
    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at the midpoint into sublists
    returns two sublists - left and right
    """
    
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]
    
    return left, right

def merge(left, right):
    """
    Merges two list/arrays, sorting them in the process
    Returns a new merged list
    """
    merge_list = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right): #compares and appends the values in an order
        if left[i] < right[j]:
            merge_list.append(left[i])
            i += 1
        else:
            merge_list.append(right[j])
            j += 1
            
    while i < len(left):
        merge_list.append(left[i])
        i += 1     
            
    while j < len(right):
        merge_list.append(right[j])
        j += 1   
            
    return merge_list

def verify_sorted(list):
    n = len(list)
    
    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])

alist = [54, 62, 93, 17, 77, 31, 44, 55, 20]
l = merge_sort(alist)
print(verify_sorted(alist))
print(verify_sorted(l))

