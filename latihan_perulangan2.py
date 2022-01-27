# Menggambar pola dengan bintang *

print("Ahmad ", end="")
print("Romadhani")

angka = input("Inputkan angka versi 1 anda : ")
angka = int (angka)

for i in range (1, angka + 1):
    for j in range(1, angka + 1):
        print("*", end="")
    print("")

angka = input("Inputkan angka versi 2 anda : ")
angka = int (angka)

for i in range (1, angka + 1):
    for j in range(i):
        print("*", end="")
    print("")

angka = input("Inputkan angka versi 3 anda : ")
angka = int (angka)

for i in range (angka, 0, -1):
    for j in range(i):
        print("*", end="")
    print("")