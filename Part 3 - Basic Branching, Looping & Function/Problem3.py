def prime_number(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print(prime_number(11)) # True
print(prime_number(13)) # True
print(prime_number(17)) # True
print(prime_number(20)) # False
print(prime_number(35)) # False