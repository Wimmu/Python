luku = input("Syötä luku tai paina enter lopettaaksesi:")
luvut = []

while luku != "":
    luvut.append(int(luku))
    luku = input("Syötä luku tai paina enter lopettaaksesi:")

luvut.sort(reverse=True)

print(luvut[0:5])