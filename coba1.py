barang = int(input("harga barang"))
pajak = barang / 100 * 10
print(pajak)

if pajak <= 1000000 :
    print(pajak,"pajak anda")
else:
    print("tidak ada pajak")

angka = int(input("masukkan angka anda"))
hasil = angka + 1
print(hasil)

if hasil %2 == 0:
    print("genap")
else:
    print("ganjil")

x = (input("masukkan kuliah"))

if x == "unuja":
    print("benar")
else:
    print("salah")