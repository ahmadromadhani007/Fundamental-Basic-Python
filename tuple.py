y = (1,2,"a","b",True, False)
print(y) # (1, 2, 'a', 'b', True, False)

print (y[0]) # 1

print(y[-1]) # False

x = list(y) 
print(x) # konversi tuple ke list [1, 2, 'a', 'b', True, False]

y2 = tuple(x) 
print(y2) # konversi list ke tuple (1, 2, 'a', 'b', True, False) 