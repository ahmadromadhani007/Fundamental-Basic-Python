z = {"c", 2, "a", 1, "b", 3 }
print(z) # {'b', 1, 2, 3, 'a', 'c'}

z.add ("d")
print(z) # menambah elemen d {1, 2, 3, 'b', 'c', 'd', 'a'}

z.remove ("b")
print(z) # menghapus elemen b {1, 2, 3, 'd', 'a', 'c'}

z.discard ("c")
print(z) # membuang elemen c {1, 2, 3, 'd', 'a'}

z.pop ()
print(z) # menghapus elemen terakhir {2, 3, 'd', 'a'}

z.clear ()
print(z) # menghapus semua elemen ()