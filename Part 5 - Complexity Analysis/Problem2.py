def pow(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result

print(pow(2, 3))  # 8
print(pow(7, 2))  # 49
print(pow(10, 5))  # 100000
print(pow(17, 6))  # 24137569
print(pow(5, 3))  # 125
