Harga = 370000  # harga awal
Diskon = 15

harga_diskon = (Diskon/100) * Harga
harga_akhir = Harga - harga_diskon

print(f'Harga yang harus dibyar adalah Rp. {harga_akhir:.0f}')