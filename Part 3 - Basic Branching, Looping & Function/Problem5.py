def Pangkat(base, pangkat):
    if pangkat == 0:
        return 1
    else:
        return base*Pangkat (base, pangkat-1)
print(Pangkat(2, 3))
print(Pangkat(5, 3))
print(Pangkat(10, 2))
print(Pangkat(2, 5))
print(Pangkat(7, 3))
