def remove_duplicates(array):
    if not array:
        return 0

    index1 = 1
    for index2 in range(1, len(array)):
        if array[index2] != array[index1 - 1]:
            array[index1] = array[index2]
            index1 += 1
    return index1

# Example usage:
print(remove_duplicates([2, 3, 3, 3, 6, 9, 9])) 
print(remove_duplicates([2, 3, 4, 5, 6, 9, 9])) 
print(remove_duplicates([2, 2, 11]))            
print(remove_duplicates([2, 2, 11]))
print(remove_duplicates([1, 2, 3, 11, 11]))