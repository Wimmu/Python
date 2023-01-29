"""
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa toisen listan,
joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki
parittomat luvut. Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja
tulostat sen jälkeen sekä alkuperäisen että karsitun listan.
"""
def parilliset(kokonaisluvut):
    for i in kokonaisluvut[:]:
        if i % 2 != 0:
            kokonaisluvut.remove(i)
    return kokonaisluvut

kokonaisluvut = [2, 5, 3, 4, 15, 22]
print(kokonaisluvut)
eiparittomia = parilliset(kokonaisluvut)
print(eiparittomia)