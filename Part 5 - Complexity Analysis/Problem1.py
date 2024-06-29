def bilangan_prima(bilangan):
    if bilangan <= 1:
        return False
    if bilangan == 2:
        return True
    if bilangan % 2 == 0:
        return False
    for i in range(3, bilangan, 2):
        if bilangan % i == 0:
            return False
    return True

# Test kasus
print(bilangan_prima(1000000007))  # True
print(bilangan_prima(1500450271))  # True
print(bilangan_prima(1000000000))  # False
print(bilangan_prima(10000000019)) # True
print(bilangan_prima(10000000033)) # True
