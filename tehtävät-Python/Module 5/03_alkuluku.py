luku = int(input("Syötä kokonaisluku:"))
kerratjaollinen = 0
jaetaan = luku

while jaetaan != 0:
    if luku % jaetaan == 0:
        kerratjaollinen = kerratjaollinen + 1
        jaetaan = jaetaan - 1
    else:
        jaetaan = jaetaan - 1

if kerratjaollinen == 2:
    print("Luku on alkuluku")
else:
    print("Luku ei ole alkuluku")



