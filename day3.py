def findDuplicate(arr):
    # Phase 1: Detect intersection
    slow = arr[0]
    fast = arr[0]
    
    while True:
        slow = arr[slow]       # move 1 step
        fast = arr[arr[fast]]  # move 2 steps
        if slow == fast:
            break

    # Phase 2: Find entrance of cycle (duplicate number)
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]

    return slow



print(findDuplicate([1, 3, 4, 2, 2]))       
print(findDuplicate([3, 1, 3, 4, 2]))        
print(findDuplicate([1, 1]))                 
print(findDuplicate([1, 4, 4, 2, 3]))        
print(findDuplicate(list(range(1,100000)) + [50000]))  
