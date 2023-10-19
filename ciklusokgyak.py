def feladat1():
    print("1. Feladat")
    a: int = int(input("Adjon meg egy pozitív egész számot: "))
    i: int = 1
    while (i<=a):
        if i == a:
           print(i, end=" ")
        else:
            print(i, end="; ")
        i+=1

def feladat2():
    print(" ")
    print("2. Feladat")
    a: int = int(input("Adjon meg egy pozitív egész számot: "))
    i: int = 1
    osszeg: int = 0
    while (i<=a):
        if a % i == 0:
            print(i)
            osszeg += i
        i += 1
    print("Az összeg:" + str(osszeg))

def feladat3():
    print(" ")
    print("3. Feladat")
    a: int = int(input("Adjon meg egy pozitív egész számot: "))
    b: int = int(input("Adjon meg még egy pozitív egész számot: "))
    i: int= a
    while(i<=b):
        if i % 2 == 0:
            print(i)
        i += 1
