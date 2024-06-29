def pair_sum(arr, target):
    angka = {}  
    for i, n in enumerate(arr):
        complement = target - n
        if complement in angka:
            return [angka[complement], i]
        angka[n] = i
    return None  


print(pair_sum([1, 2, 3, 4, 6], 6))  
print(pair_sum([2, 5, 9, 11], 11))    
print(pair_sum([1, 3, 5, 7], 12))     
print(pair_sum([1, 4, 6, 8], 10))
print(pair_sum([1, 5, 6, 7], 6))          