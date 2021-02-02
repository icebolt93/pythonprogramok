import random
b = int(input("Adja meg a véletlenszám alsó határát!:"))
c = int(input("Adja meg a véletlenszám felső határát!(szám+1):"))
veletlenszam = random.randrange (b,c) #egy és száz között
tipp = int(input("Adjon meg egy számot a véletlenszám alsó és felső határa között:"))
print (tipp)
jatekmod = int(input("Adja meg a játékmódot(1: a játékos tippeli a számítógép számát 2: a számítógép tippeli a játékos számát)"))
if jatekmod == 1:
     jatekostipp = 0
     while veletlenszam != jatekostipp:
       jatekostipp = int(input("Tippelje meg a számítógép számát:"))
if jatekmod == 2:
    szamgeptippeli = 0
    while(tipp != szamgeptippeli):
       print("A számítógép tippe:")
       szamgeptippeli = random.randrange(b,c)
       print (szamgeptippeli)
