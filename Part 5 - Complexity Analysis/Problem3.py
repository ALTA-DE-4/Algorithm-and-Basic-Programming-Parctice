def join_array_remove_duplicate(arrayA, arrayB):
    array_gabungan = arrayA + arrayB
    arrayunik = []
    for item in array_gabungan:
        if item not in arrayunik:
            arrayunik.append(item)
    return arrayunik

print(join_array_remove_duplicate(['apel', 'anggur'], ['lemon', 'leci', 'nanas']))
# ['apel', 'anggur', 'lemon', 'leci', 'nanas']

print(join_array_remove_duplicate(['samsung', 'apple'], ['apple', 'sony', 'xiaomi']))
# ['samsung', 'apple', 'sony', 'xiaomi']

print(join_array_remove_duplicate(['football', 'basketball'], ['basketball', 'football']))
# ['football', 'basketball']
