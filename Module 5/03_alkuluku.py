luku = int(input("Syötä kokonaisluku:"))
i = 1
luvut = []

while i < 1000:
    if i == 1:
        i = i + 1
    else:
        luvut.append(i)
        i = i + 1

for n in luvut:
    if luku % n == 0:
        print("Ei ole alkuluku")
    else:
        print("On alkuluku")



