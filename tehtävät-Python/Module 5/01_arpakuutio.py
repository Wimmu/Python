import random
kuutiot = []
yhteensä = 0
määrä = int(input("Kuinka monta arpakuutiota heitetään?"))

# ARVOTAAN LUVUT
while määrä > 0:
    luku = random.randint(1,6)
    kuutiot.append(luku)
    määrä = määrä - 1

print("Heitit luvut:", kuutiot)

# LASKETAAN SUMMA
for n in kuutiot:
    if yhteensä == 0:
        yhteensä = n
    else:
        yhteensä = yhteensä + n

print("Silmälukujen summa on", yhteensä)


