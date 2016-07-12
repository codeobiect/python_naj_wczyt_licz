liczby = int(input("Podaj liczbę: "))
najmniejsza = liczby
while liczby != 0:
    liczby = int(input("Podaj liczbę: "))
    if liczby < najmniejsza and liczby != 0:
        najmniejsza = liczby
print(najmniejsza)


