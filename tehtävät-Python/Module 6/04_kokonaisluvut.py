"""
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien
lukujen summan. Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja
tulostat sen palauttaman summan.
"""
def summa(kokonaisluvut):
    yhteensä = sum(kokonaisluvut)
    return yhteensä

kokonaisluvut = [2, 5, 3, 4]
yhteensä = summa(kokonaisluvut)
print(yhteensä)
