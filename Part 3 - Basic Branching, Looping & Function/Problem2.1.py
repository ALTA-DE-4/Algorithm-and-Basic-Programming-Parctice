bilangan = int(input('Masukan Bilangan : '))

def faktor(bilangan):
    angka  =[]
    for i in range(1, bilangan + 1):
        if bilangan % i == 0:
            angka.append(i)
    return angka 

cetak = faktor(bilangan)
for angka in cetak:
    print(angka)