print('contoh dictionary ---------------------')
# {'key1': 'value1', 'key2': 'value2'}
orang = {
    'nama': 'Dono',
    'alamat': 'Jakarta',
    'hobby': 'Memancing'
}
orang['pendidikan'] = 'D3'
print(orang)
print(orang['nama'])
print(orang['alamat'])
print(orang['hobby'])

print('parse dictionary ---------------------')
for key in orang:
    print(key, orang[key])

print('parse dictionary (cara lain) --------')
for key, value in orang.items():
    print(key, value)
