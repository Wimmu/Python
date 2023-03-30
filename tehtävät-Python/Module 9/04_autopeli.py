import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettumatka = 0

    def kiihdyntä(self, nopeudenmuutos):
        self.nopeus += nopeudenmuutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tuntimäärä):
        self.kuljettumatka = self.kuljettumatka + self.nopeus*tuntimäärä

# LUODAAN 10 AUTOA
autot = []
rekkari = 0
for i in range(10):
    huippunopeus = random.randint(100,200)
    rekisteritunnus = "ABC-"+str(rekkari)
    autot.append(Auto(rekisteritunnus, huippunopeus))
    rekkari = rekkari + 1

# PELATAAN PELI JA KATSOTAAN MILLOIN ENSIMMÄINEN MAALISSA
maalissa = 0
while maalissa != 1:
    for n in autot:
        n.kiihdyntä(random.randint(-10,15))
        n.kulje(1)
        if n.kuljettumatka > 10000:
            maalissa = 1

# JÄRJESTETÄÄN AUTOT TULOSJÄRJESTYKSEEN JA PRINTATAAN
autot.sort(key=lambda x: x.kuljettumatka, reverse=True)
sija = 1
for n in autot:
    print(str(sija)+".", n.rekisteritunnus,"- Kuljettu matka:", n.kuljettumatka, "- Huippunopeus:", n.huippunopeus)
    sija = sija + 1