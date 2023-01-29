"""
Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
joka kysytään käyttäjältä ohjelman suorituksen alussa.
"""
import random
def heitto(yhteismäärä):
    luku = random.randint(1, yhteismäärä)
    print("Heitettiin luku", luku)
    return luku

yhteismäärä = int(input("Anna nopan maksimi silmäluku:"))
luku = heitto(yhteismäärä)

while luku != yhteismäärä:
    luku = heitto(yhteismäärä)
print("Sait numeron", luku)