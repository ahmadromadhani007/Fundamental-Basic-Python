# Perulangan adalah intruksi yang dapat mengulang sederetan intruksi sesuai dengan persyaratan yang diterapkan.
"""" Struktur intruksi pengulangan :
> Kondisi perulangan yaitu suatu kondisi yang harus dipenuhi agar perulangan dapat terjadi
> Badan (Body) perulangan yaitu deretan instruksi yang akan di ulang-ulang pelaksanaan nya
> Pencacah (Counter) perulangan yaitu suatu variable yang nilainya harus berubah agar perulangan dapat
terjadi dan pada akhrinya membatasi jumlah perulangan yang dapat dilaksanakan """

# Perulangan While yaitu mengeksekusi sekumpulan statement selama kondisinya benar.

i = 1

while i < 5 :
    print(i)
    i += 1

# Statement Break yaitu digunakan untuk menghentikan perulangan walau kondisi nilai masih benar.

i = 1

while i < 5 :
    print(i)
    if i == 2:
        break
    i += 1

# Statement Countinue yaitu digunakan untuk melewati/skip 1 perulangan yang sedang terjadi dan lanjut ke - 
# perulangan selanjutnya  

i = 1

while i < 5 :
    i += 1
    if i == 3:
        continue
    print(i)

# Perulangan else yaitu digunakan untuk menjalankan blok statement saat perulangan selesai

i = 1

while i < 5 :
    i += 1
    if i == 3:
        continue
    print(i)
else:
    print("Have been done and finished")    