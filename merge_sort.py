def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step

    Takes O(n log n) time
    """

    if len(list) <=1:
        return list

    left_half, right_half = rsplit(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right

    Takes overall O(k log n) time , k is the size of the split
    Subdividing in 2 is a O(log n) operation
    Slicing takes O(k) time, with k the size of the slice 
    """

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:] 

    return left, right

def rsplit(list):
    """
    Change the slicing for a recursive operation
    Declare 2 variables to determine starting and ending position on the list
    """
    mid = len(list)//2
    ini = list[0]
    fin = list[len(list)]
 
    if len(list) == 0:
        return False
    
    if len(left) == 1 and len(right) ==1:
        return left, right

    elif len(left) == 1 and len(right) == 2:
        return left, rsplit(right)

    else:
        return rsplit(left), rsplit(right)
    

def merge(left, right):
    """
    Merges two lists (arrays) sorting them in the process
    Returns a new list

    Runs in overall O(n) time
    """

    l = []
    i = 0
    j = 0
    
    while i< len(left) and j< len(right):
        if left[i] < right [j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i+=1
    while j < len(right):
        l.append(right[j])
        j+=1

    return l

def verify_sorted(list):
    n = len(list)
    if n==0 or n==1:
        return True
    return list[0] <= list[1] and verify_sorted(list[1:])

alist = [2,454,676,4,535,8,747,6787,0,987,52,6]
print((alist))
print(verify_sorted(alist))
print("Recursive spliting")
l= merge_sort(alist)
print(verify_sorted(l))
print((l))
"""
alist = [2,454,676,4,535,8,747,6787,0,987,52,6]
l = merge_sort(alist)
print(l)
"""