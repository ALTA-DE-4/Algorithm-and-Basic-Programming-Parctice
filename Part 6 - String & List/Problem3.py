def array_unique(arrayA, arrayB):
    arrB = set(arrayB)
    result = []    
    for angka in arrayA:
        if angka not in arrB:
            result.append(angka)
    return result

print(array_unique([1, 2, 3, 4], [1, 3, 5, 10, 16]))   
print(array_unique([10, 20, 30, 40], [5, 10, 15, 59]))
print(array_unique([1, 3, 7], [1, 3, 5]))
print(array_unique([3, 8], [2, 8]))
print(array_unique([1, 2, 3], [3, 2, 1]))
