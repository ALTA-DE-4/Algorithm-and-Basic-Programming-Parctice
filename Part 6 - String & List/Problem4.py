def find_max__sum_sub_array(k, arr):
    if k > len(arr):
        return None
    max_sum = sum(arr[:k])
    window_sum = max_sum

    for i in range(1, len(arr) - k + 1):
        window_sum = window_sum - arr[i - 1] + arr[i + k - 1]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

print(find_max__sum_sub_array(3, [2, 1, 5, 1, 3, 2]))  
print(find_max__sum_sub_array(2, [2, 3, 4, 1, 5])) 
print(find_max__sum_sub_array(2, [2, 1, 4, 1, 1]))
print(find_max__sum_sub_array(3, [2, 1, 4, 1, 1]))
print(find_max__sum_sub_array(4, [2, 1, 4, 1, 1]))  
