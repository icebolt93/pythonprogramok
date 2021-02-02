import random
a = random.randrange (1,101) #egy és száz között
tipp = int(input("Adjon meg egy számot egy és száz között:"))
print (tipp)
if a < tipp:
    print ("Kisebb")
else:
    print ("Nagyobb")
if a == tipp:
  print ("Nyertél!")
else:
  print ("Vesztettél")
