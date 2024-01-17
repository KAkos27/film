from Filmek import Filmek


def file_beolvasas():
    film_lista = []
    file = open("film.txt", "r", encoding="utf-8")
    file.readline()
    elso_lista = file.readlines()
    file.close()

    for i in range(0, len(elso_lista), 1):
        sor_lista = elso_lista[i].strip()
        sor_lista = sor_lista.split(";")

        film = Filmek(
            sor_lista[0],
            sor_lista[1],
            sor_lista[2],
            sor_lista[3],
            sor_lista[4],
        )

        film_lista.append(film)

    return film_lista


def legrovidebb(lista):
    min = 999999
    rovid_index = 0

    for i in range(0, len(lista), 1):
        if int(lista[i].perc) < min:
            min = int(lista[i].perc)
            rovid_index = i

    return lista[rovid_index].cim


def hosszu_filmek(lista):
    osszegzo = 0

    for i in range(0, len(lista), 1):
        if int(lista[i].perc) >= 110:
            osszegzo += 1

    return osszegzo


def ajanlas(lista):
    szinesz_nev = ""
    foszereplo_letezes = 0
    fo_film_lista = []

    while foszereplo_letezes == 0:
        szinesz_nev = str(input("Kérek egy nevet: "))
        for i in range(0, len(lista), 1):
            if lista[i].foszereplo == szinesz_nev:
                foszereplo_letezes += 1
                fo_film_lista.append(lista[i].cim)

    return fo_film_lista


def kiiras(film_lista):
    print("Ajánlott filmek:")

    for i in range(0, len(film_lista), 1):
        print(film_lista[i])


def file_kiir(film_lista):
    file = open("ajanlas.txt", "w", encoding="utf-8")
    file.write("Ajánlott filmek:\n")

    for i in range(0, len(film_lista), 1):
        file.write(film_lista[i] + "\n")

    file.close()
