# Perulangan pada List, Tuple, Set dan Dictionary

buah = ["Semangka", "Mangga", "Pisang"]

#list set and tuple
for a in buah:
    print(a) 

# list dan set (menggunakan index)
for i in range(len(buah)):
    print(buah[i])

i = 0
while i < len(buah):
    print(buah)
    i +=1

# dictionary
dic = {"nama":"Shinta","umur": 17,"jenkel": "Wanita"}

for x in dic:
    print(x)

for y in dic:
    print(dic[y])

