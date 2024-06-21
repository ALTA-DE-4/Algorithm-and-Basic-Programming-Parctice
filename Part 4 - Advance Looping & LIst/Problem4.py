def mean_median(array_input):
    # Menghitung mean
    mean_value = sum(array_input) / len(array_input)
    
    # Menghitung median
    sorted_array = sorted(array_input)
    n = len(sorted_array)
    mid = n // 2

    if n % 2 == 0:
        # Jika jumlah elemen genap, median adalah rata-rata dari dua elemen tengah
        median_value = (sorted_array[mid - 1] + sorted_array[mid]) / 2
    else:
        # Jika jumlah elemen ganjil, median adalah elemen tengah
        median_value = sorted_array[mid]

    print(f"({mean_value}), ({median_value})")


mean_median([1, 2, 3, 4])
mean_median([1, 2, 3, 4, 5])
mean_median([7, 8, 9, 13, 15])
mean_median([10, 20, 30, 40, 50])
mean_median([15, 20, 30, 60, 120])
