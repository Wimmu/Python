"""
Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
"""
import random
def heitto():
    luku = random.randint(1, 6)
    print("Heitettiin luku", luku)
    return luku

luku = heitto()
while luku != 6:
    luku = heitto()
print("Sait numeron 6.")