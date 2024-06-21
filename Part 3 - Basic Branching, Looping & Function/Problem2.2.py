bilangan = int(input('Masukan Bilangan : '))

def faktor(bilangan):
    angka  =[]
    for i in range(bilangan, 0, -1):
        if bilangan % i == 0:
            angka.append(i)
    return angka 

cetak = faktor(bilangan)
for angka in cetak:
    print(angka)