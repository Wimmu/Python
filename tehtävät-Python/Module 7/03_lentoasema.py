lentokentät = {"EFHK":"Helsinki-Vantaa"}
tehdään = 0
def uusikenttä():
    u_nimi = input("Anna lentoaseman nimi:")
    u_koodi = input("Syötä aseman ICAO-koodi:")
    lentokentät[u_koodi] = u_nimi
    print("- Lentokenttä nimeltä", u_nimi, u_koodi, "on lisätty tietoihin -")
def etsikenttä():
    koodi = input("Syötä aseman ICAO-koodi:")
    if koodi in lentokentät:
        print("- Haettiin lentokenttä:", lentokentät[koodi], "-")

while tehdään != 3:
    print("1. Syötä uusi lentoasema.")
    print("2. Hae lentoasemaa.")
    print("3. Lopeta ohjelma.")
    tehdään = int(input("> "))
    if tehdään == 1:
        uusikenttä()
    if tehdään == 2:
        etsikenttä()