def find_missing_number(arr):
    n = len(arr) + 1  # since one number is missing
    total_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return total_sum - actual_sum


# Alternative XOR method
def find_missing_number_xor(arr):
    n = len(arr) + 1
    xor_all = 0
    xor_arr = 0
    
    # XOR of 1 to n
    for i in range(1, n+1):
        xor_all ^= i
    
    # XOR of given array
    for num in arr:
        xor_arr ^= num
    
    return xor_all ^ xor_arr


# ✅ Example test cases
print("Missing number (Sum Method):", find_missing_number([1, 2, 4, 5])) 
print("Missing number (XOR Method):", find_missing_number_xor([1, 2, 4, 5]))
print(find_missing_number([2,3,1,5]))  
print(find_missing_number([1]))         
print(find_missing_number([2]))         
print(find_missing_number([1,2,3,4,6])) 
