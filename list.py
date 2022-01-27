x = [1 , 2, "a", "b", True, False]
print(x)

# mendapatkan panjang list
print(len(x)) # output - 5

# mengubah nilai pada index ke 1
x [1] = 3
print(x) # [1,3,'a','a''true','false']

# menambah element pada index terakhir
x.append(4)
print(x) # [1,3,'a','b','true','false',4]

# menambah elemen pada index ke 1
x.insert(1, "c")
print(x) # [1,'c',3,'a','b',true,false,4]

# menghapus elemen c 
x.remove('c')
print(x) # [1,3,'a','b','true','false',4]

# menghapus elemen pada index ke 0 atau tertentu
x.pop(0)
print(x) # [3, 'a', 'b', True, False, 4]

# membersihkan semua elemen
x.clear()
print(x) # []
 