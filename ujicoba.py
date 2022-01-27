nilai = input ("silahkan inputkan nilai anda ! ")
nilai = int(nilai) #input ini merupakan string harus di rubah ke int

if nilai >= 60:
    print("Lulus")
else:
    if nilai >= 40:
        print("Remedi") #percabangan dalam percabangan else & if
    else:
        print("Tidak lulus")
"""
nama = input("Silahkan masukkan nama anda !")
print(nama)

print(type(nama))

nim = int (input("Silahkan masukkan NIM !"))
print(nim)

print(type(nim))

ipk = float (input("Berapa IPK anda !"))
print(ipk)

print(type(ipk))"""

"""varStr = "Ahmad"
print(type(varStr))

varInt = 3
print(type(varInt))

varFloat = 2.5
print(type(varFloat))

varBooelan = True
print(type(varBooelan))"""
"""
umur = input("Berapakah umur anda sekarang ? ")
umur = int(umur)

if umur >= 17:
    print("Anda lolos kategori")
else:
    print("Maaf anda masih di bawah umur") 

nilai1 = 70
nilai2 = 60

if nilai1 >= 60 and nilai2  >= 60:
    print("Selamat anda lulus")
elif nilai2 >= 60 or nilai2 >= 60:
    print("Anda harus remidi ")
else:
    print("Anda tidak lulus")"""