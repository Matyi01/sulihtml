print("1. feladat")
szoveg = input("Kérek egy szöveget: ")
szam = ""
while type(szam) != int:
    try:
        szam = int(input("Kérek egy egész számot: "))
    except:
            print("Ez nem egy egész szám!")
try:
    print(szoveg[szam-1]*szam)
except:
    print("Sajnos nincs ilyen betű.")
