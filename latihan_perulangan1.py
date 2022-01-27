"""Menghitung rata-rata dari sejumlah bilangan 
dengan INPUT : Beberapa angka dan OUTPUT : rata-rata dari angka-angka yang menjadi input """

total = 0 
jumlah = 0

for i in range (0, 5): 
     angka = input("Input angka : ")
     angka = float(angka)

     total += angka
     jumlah += 1

print(total)
print(jumlah)

rata2 = total / jumlah
print(rata2)