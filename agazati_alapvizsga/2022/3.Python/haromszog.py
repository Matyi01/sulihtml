def haromszog():
    a = ""
    while a == "":
        try:
            a = int(input("Kérem a(z) 1. egy egész számot: "))
        except:
            print("Ez nem egész szám!")
    b = ""
    while b == "":
        try:
            b = int(input("Kérem a(z) 2. egy egész számot: "))
        except:
            print("Ez nem egész szám!")
    c = ""
    while c == "":
        try:
            c = int(input("Kérem a(z) 3. egy egész számot: "))
        except:
            print("Ez nem egész szám!")
    return [a, b, c]
