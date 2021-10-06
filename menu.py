menu = '''
1. Tampilkan data
2. Masukkan data baru
3. Hapus data
4. Keluar
'''

data = []

while True:
    print(menu)
    pilihan = input('Masukkan pilihan: ')

    if pilihan == '4': # keluar
        break
    
    if pilihan == '1': # tampilkan
        for x in data:
            print(x)
    elif pilihan == '2': # masukkan
        x = input('Nilai baru: ')
        data.append(x)
    elif pilihan == '3': # hapus
        x = input('Nilai yang akan dihapus: ')
        data.remove(x) # untuk hapus by index, pakai x.pop


print('Terima kasih')