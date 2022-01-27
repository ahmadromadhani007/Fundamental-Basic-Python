from os import umask


tahun_lahir = input("Masukkan tahun lahir Kamu !")
tahun_lahir = int (tahun_lahir)

# Umur - tahun sekarang - tahun lahir
umur = 2021 - tahun_lahir

print("Umur kamu sekarang adalah = ",umur)

if umur <= 13 :
    print("Kategori kamu masih anak-anak")
elif umur <= 20 :
    print("Kategori kamu sudah remaja")
elif umur <= 39 :
    print("Kategori kamu memasuki tahapan kedewasaan")
else:
    print("Kategori kamu sudah tua")

