d = {"nama":"Rama", "umur":20,"jenkel":"pria"}
print(d) # {'nama': 'Rama', 'umur': 20, 'jenkel': 'pria'}

print(d["nama"]) # Rama

print(d.get("nama")) # Rama

d["umur"] = 21 
print(d) # Merubah nilai nya {'nama': 'Rama', 'umur': 21, 'jenkel': 'pria'}

d["tinggi"] = 180 
print(d) # Membuat elemen baru {'nama': 'Rama', 'umur': 21, 'jenkel': 'pria', 'tinggi': 180}

d.pop("jenkel") 
print(d) # Menghapus elemen {'nama': 'Rama', 'umur': 21, 'tinggi': 180}

d.clear()
print(d) # {}