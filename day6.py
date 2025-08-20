def find_zero_sum_subarrays(arr):
    prefix_sum = 0
    hashmap = {0: [-1]}  
    result = []

    for i, num in enumerate(arr):
        prefix_sum += num

        if prefix_sum in hashmap:
            for start_index in hashmap[prefix_sum]:
                result.append((start_index + 1, i))

        hashmap.setdefault(prefix_sum, []).append(i)

    return result
print(find_zero_sum_subarrays([4, -1, -3, 1, 2, -1]))

print(find_zero_sum_subarrays([1, 2, 3, 4]))

print(find_zero_sum_subarrays([0, 0, 0]))


print(find_zero_sum_subarrays([-3, 1, 2, -3, 4, 0]))

print(find_zero_sum_subarrays([1, -1, 2, -2, 3, -3] * 2))
