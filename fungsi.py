""" Fungsi merupakan kode yang di beri nama dan hanya akan dieksekusi ketika di panggil, dan kita juga bisa
mengirimkan data ke fungsi (biasa di sebut parameter). Fungsi bisa mengembalikan nilai keluaran (output) dan
cukup di tulis sekali akan tetapi bisa digunakan berkali-kali """

def cetakName(nama): # parameter
    print("selamat datang", nama)

# argument
cetakName("Ahmad")
cetakName("Rama")
cetakName("Dhan")

def tambah (angka1 = 0, angka2 = 0):
    jumlah = angka1 + angka2
    return jumlah

hasil = tambah (1 , 2)
print(hasil)

hasil = tambah()
print(hasil)

hasil = tambah(3)
print(hasil)