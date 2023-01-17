tunnus = "python"
salasana = "rules"
yritykset = 1
oikein = 0

k_tunnus = input("Anna käyttäjätunnus:")
k_salasana = input("Anna salasana:")

while oikein != 1 and yritykset != 5:
    if k_tunnus != tunnus or k_salasana != salasana:
        yritykset = yritykset + 1
        print("Käyttäjätunnus tai salasana on väärin!")
        k_tunnus = input("Anna käyttäjätunnus:")
        k_salasana = input("Anna salasana:")
    elif k_tunnus == tunnus and k_salasana == salasana:
        oikein = 1

if yritykset == 5:
    print("Pääsy evätty! Syötit tunnukset 5 kertaa väärin!")
else:
    print("Tervetuloa!")