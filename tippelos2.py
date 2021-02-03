import random
veletlenszam = random.randrange(1,101) #1 és 100 között
print (veletlenszam)
tipp = int(input("Tippelje meg a véletlenszámot 1 és 100 között"))
if tipp < veletlenszam:
    print ("Kisebb")
elif veletlenszam == tipp:
    print("Egyenlő")
else:
   print ("Nagyobb")
if tipp == veletlenszam:
    print ("Eltaláltad")
else:
   print ("Nem találtad el")
