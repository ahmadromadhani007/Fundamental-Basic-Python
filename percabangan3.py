# IF multikondisi AND dan OR

nilai1 = 55
nilai2 = 30

if nilai1 >= 60 and nilai2  >= 60:
    print("Selamat anda lulus")
elif nilai2 >= 60 or nilai2 >= 60:
    print("Anda harus remidi ")
else:
    print("Anda tidak lulus")

# juga bisa ditambah dengan Statement pass 
""" yaitu statement yang mana IF ini tidak boleh kosong dan pass ini digunakan
pada IF tanpa konten """

if nilai1 >= 60 and nilai2  >= 60:
    print("Selamat anda lulus")
elif nilai2 >= 60 or nilai2 >= 60:
    print("Anda harus remidi ")
else:
    pass

# Ternary 
""" Yaitu menampilkan nilai yang terbesar"""

a = 90
b = 30
print("Nilai variable terbesar adalah :")
print("a") if a > b else print("b") 
