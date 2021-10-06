print('contoh variable -----------------------')
buah = 'jeruk'
print(buah)

print('contoh list ---------------------------')
buah_buahan = ['jeruk', 'strawberry', 'anggur']
print(buah_buahan)
print(buah_buahan[0])
print(buah_buahan[1])
print(buah_buahan[2])
print(len(buah_buahan))

print('parse list pakai index ----------------')
# range(0, 3)
# 0, 1, 2
for i in range(0, len(buah_buahan)):
    print(buah_buahan[i])

print('parse list tanpa pakai index ----------')
for b in buah_buahan:
    print(b)
# for i in range(0, len(buah_buahan)):
#     b = buah_buahan[i]
#     print(b)

