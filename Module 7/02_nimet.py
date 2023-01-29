nimet = set()
nimi = input("Kirjoita nimi: ")

while nimi != "":
    if nimi in nimet:
        print("Aiemmin syötetty nimi.")
    else:
        print("Uusi nimi.")
        nimet.add(nimi)
    nimi = input("Kirjoita nimi:")

for n in nimet:
    print(n)
