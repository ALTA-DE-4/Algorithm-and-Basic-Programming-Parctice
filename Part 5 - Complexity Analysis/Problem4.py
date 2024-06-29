def muncul(angka):
    count_dict = {}
    for char in angka:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    
    muncul_sekali = []
    
    for key, value in count_dict.items():
        if value == 1:
            muncul_sekali.append(int(key))
    return muncul_sekali

# Contoh penggunaan
print(muncul('1234123'))    
print(muncul('76523752'))
print(muncul('12345'))  
print(muncul('1122334455')) 
print(muncul('0872504')) 
