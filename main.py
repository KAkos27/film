import feladat

lista = feladat.file_beolvasas()
rovid_film=feladat.legrovidebb(lista)
print(f"A legrövidebb film címe: {rovid_film}")
hosszuk_szama = feladat.hosszu_filmek(lista)
print(f"A leglább 110 perces filmek száma: {hosszuk_szama}")

fo_filmek=feladat.ajanlas(lista)
feladat.kiiras(fo_filmek)
feladat.file_kiir(fo_filmek)