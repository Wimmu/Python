"""
Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma,
joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
kunnes käyttäjä syöttää negatiivisen gallonamäärän. Yksi gallona on 3,785 litraa.

"""
def muunnos(gallonamäärä):
    litramäärä = gallonamäärä*3.785
    return litramäärä

gallonamäärä = float(input("Anna gallonamäärä:"))

while gallonamäärä > 0:
    litramäärä = muunnos(gallonamäärä)
    print(litramäärä, "litraa.")
    gallonamäärä = float(input("Anna gallonamäärä:"))

