import haromszog

def bekeres():
    haromszogek = []
    for i in range(3):
        print(f"{i+1}. adatsor")
        temp = haromszog.haromszog()
        haromszogek.append(temp)
    for e in haromszogek:
        print(f"\ta={e[0]}, b={e[1]}, c={e[2]}")
    return haromszogek

def haromszoge(oldalak):
    a = oldalak[0]
    b = oldalak[1]
    c = oldalak[2]
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

adatok = bekeres()
for i,e in enumerate(adatok):
    if haromszoge(e) == True:
        print(f"{i+1}. számsor lehet háromszög")
    else:
        print(f"{i+1}. számsor nem lehet háromszög")
