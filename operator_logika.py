#Operator logika digunakan untuk membandingkan 2 kondisi logika
# AND (bernilai benar jika semua kondisi itu benar)
# OR (bernilai benar jika salah satu kondisi itu benar)
# NOT (membalikkan hasil, jika benar disalahkan jika salah dibenarkan)

x = 5
y = 10

print(x == 5 and x > 10)
print(x == 5 or x < 10)
print(not (x < 5 and x < 10))