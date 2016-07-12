"""liczby = int(input("Podaj liczbę: "))
najmniejsza = liczby
while liczby != 0:
    liczby = int(input("Podaj liczbę: "))
    if liczby < najmniejsza and liczby != 0:
        najmniejsza = liczby
print(najmniejsza)"""
#min = 99999999999
#sec =9999999999

def druga_najmniejsza(min, sec):
    liczby = int(input("Podaj liczbę: "))
    min = liczby
    while liczby != 0: # I brakowało !=0
        liczby = int(input("Podaj liczbę: "))
        if liczby < min and min < sec and liczby != 0:
            sec = min
            min = liczby
    print(sec)
druga_najmniejsza(999999999999,9999999999999)

"""def hetman(rows, columns):
    rozwiazania = [[]]
    for row in range(rows):
        rozwiazania = add_one_queen(row, columns, rozwiazania)
    return rozwiazania

def add_one_queen(new_row, columns, prev_solutions):
    return [solution + [new_column]
            for solution in prev_solutions
            for new_column in range(columns)
            if no_conflict(new_row, new_column, solution)]

def no_conflict(new_row, new_column, solution):
    return all(solution[row]       != new_column           and
               solution[row] + row != new_column + new_row and
               solution[row] - row != new_column - new_row
               for row in range(new_row))

for solution in hetman(8, 8):
    print(solution)"""