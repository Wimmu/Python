# LISTA
nimet = ["Petra", "Mia", "Julia", "Silva", "Veeti"]

# TYHJÄ LISTA
tyhjä = []

# LISÄÄ JÄSENEN TIETTYYN KOHTAAN
nimet.insert(2, "Teppo")

# POISTAA JÄSENEN LISTASTA
nimet.remove("Teppo")

# JÄRJESTÄÄ SUURIMMASTA PIENIMPÄÄN
nimet.sort(reverse=True)

# KERTOO MONESKO INDEX JÄSEN ON
monesko = nimet.index("Mia")
print(monesko)

# KERTOO ONKO JÄSEN LISTASSA
if "Petra" in nimet:
    print("Löytyy listasta")
else:
    print("Ei löydy listasta")

# PRINTTAA TIETYN JÄSENEN
print(nimet[3])
print(nimet[1])

# LOPUSTA ALKAEN
print(nimet[-2])

# NIMET VÄLILTÄ 1-2
print(nimet[1:3])

# NIMET 2. ALKAEN
print(nimet[2:])

# PRINTTAA KAIKKI
print(nimet)

# KYSYY KUINKA PITKÄ LISTA ON
print(len(nimet))

# KATSOO KUINKA MONTA JÄSENTÄ LISTASSA JA TULOSTAA JUTUN KAIKILLE
i = 0
while i < len(nimet):
    print("Moi,", nimet[i])
    i = i + 1