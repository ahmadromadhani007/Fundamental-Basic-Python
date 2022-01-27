# Perulangan For
""" Ialah mengulang blok statement dengan jumlah perulangan yang sudah di tentukan, 
dan menggunakan fungsi
Range() untuk menentukan jumlah perulangan.
> 3 bentuk range() :
^ range(n) melakukan perulangan dari 0 sampai(n-1)
^ range (m,n) melakukan perulangan dari m sampai n (n-1)
^ range (m,n,i) melakukan perulangan dari m sampai (n-1) dengan nilai penambahan(increment)=i"""
# Contoh range :
""" 
} range(6)= 0,1,2,3,4,5
} range (2,6)= 2,3,4,5
} range (2,6,2) = 2,4 
Dan juga For ini bisa menggunakan statement continue,break dan else.
"""
# Range (n)
for a in range(6):
    print(a)

# Range (m,n)
for b in range(2,6):
    print(b)

# Range (m,n,i)
for c in range(2,6,2):
    print(c)