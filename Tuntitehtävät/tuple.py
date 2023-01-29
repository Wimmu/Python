"""
import random

viikonpäivät = ("Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai")
numero = int(input("Anna viikonpäivän numero: "))
viikonpäivä = viikonpäivät[numero-1]
print(viikonpäivä)

hedelmät = "Omena", "Banaani", "Päärynä"
(eka, toka, kolmas) = hedelmät
print(eka, toka, kolmas)

def heitä():
    eka = random.randint(1,6)
    toka = random.randint(1,6)
    return eka, toka

noppa1, noppa2 = heitä()
print(noppa1, noppa2)

pelit = {"shakki", "Monopoli", "Kimble"}
pelit.add("Pokeri")
pelit.remove("Kimble")
print(pelit)

"""

nimet={"Ankka":"Aku","Ankka":"Tupu","Magia":"Milla"}
print(nimet)
print(nimet["Ankka"])