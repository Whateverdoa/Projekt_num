"""" functie  voor 13 over  stappen
hoe test ik dit????
"""
import pandas as pd

aantal = 5000
aantal_per_rol = 250
begin = 3000040000
eind = begin + aantal - 1

beginnummers = [num for num in range(begin, eind, aantal_per_rol)]  # set
nummers_13 = [num for num in range(begin + 13, eind, 13)]

print(len(nummers_13))

for num in beginnummers:
    print(f'{num} t/m {num + (aantal_per_rol - 1)}')

print('-' * 20)


def rol(begin_nummer):
    for num in range(begin_nummer, (begin_nummer + aantal_per_rol)):
        print(f'{num};leeg.pdf\n', end="")
        if num in [num for num in range(begin_nummer + 13, (begin_nummer + aantal_per_rol), 13)]:
            print(';stans.pdf\n', end="")

        elif num == (begin_nummer + aantal_per_rol) - 1:
            print(";stans.pdf\n", end="")
            print(";geel.pdf\n" * 4, end='')
            print(";stans.pdf", end="")


rol(begin)


def rollen(lijst_in):
    for rolnummer in lijst_in:
        rol(rolnummer)


rollen(beginnummers)
