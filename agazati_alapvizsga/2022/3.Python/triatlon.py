class versenyzo:
    def __init__(self, nev, nem, szul, uszas, kerekpar, futas, rajtszam):
        self.nev = nev
        self.nem = nem
        self.szul = szul
        self.uszas = uszas
        self.kerekpar = kerekpar
        self.futas = futas
        self.rajtszam = rajtszam
    def uszasossz(self):
         return (int(self.uszas[0:1])*3600) + (int(self.uszas[2:4])*60) + (int(self.uszas[5:7]))
    def kerekparossz(self):
         return (int(self.kerekpar[0:1])*3600) + (int(self.kerekpar[2:4])*60) + (int(self.kerekpar[5:7]))
    def futasossz(self):
         return (int(self.futas[0:1])*3600) + (int(self.futas[2:4])*60) + (int(self.futas[5:7]))
    
f = open("triatlon.txt")

adatok = []
for e in f:
    temp = e.strip().split(";")
    adatok.append(versenyzo(*temp))

f.close()

adatok.pop(0)
print(f"2.feladat: A versenyen {len(adatok)} induló volt.")

idok = []
for e in adatok:
    temp = e.uszasossz() + e.kerekparossz() + e.futasossz()
    idok.append(temp)

index = 0
for i in range(len(idok)):
    if idok[i] == min(idok):
        index = i

minnev = ""
minrajtszam = ""
for i,e in enumerate(adatok):
    if i == index:
        minnev = e.nev
        minrajtszam = e.rajtszam

print("3.feladat: A verseny nyertese:")
print(f"\tneve: {minnev}")
print(f"\trajtszáma: {minrajtszam}")
minido = f"{min(idok) // 3600}:{min(idok) % 3600 // 60}:{min(idok) % 60}"
print(f"\tösszideje: {minido}")


idok2 = []
for e in idok:
    idok2.append(f"{e // 3600}:{e % 3600 // 60}:{e % 60}")

f = open("osszidok.txt","w")

for i,e in enumerate(adatok):
    f.write(f"{e.rajtszam};{e.nev};{idok2[i]}\n")

f.close()




    
