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

class Kilpailu:
    def __init__(self, kilpailunnimi, pituus):
        self.kilpailunnimi = kilpailunnimi
        self.pituus = pituus
        self.autot = []
        rekkari = 0
        for i in range(10):
            huippunopeus = random.randint(100,200)
            rekisteritunnus = "ABC-"+str(rekkari)
            self.autot.append(Auto(rekisteritunnus, huippunopeus))
            rekkari = rekkari + 1
    def tunti_kuluu(self):
        for n in self.autot:
            n.kiihdyntä(random.randint(-10, 15))
            n.kulje(1)
    def tulosta_tilanne(self):
        self.autot.sort(key=lambda x: x.kuljettumatka, reverse=True)
        sija = 1
        for n in self.autot:
            print(str(sija) + ".", n.rekisteritunnus, "- Kuljettu matka:", n.kuljettumatka, "- Huippunopeus:",
                  n.huippunopeus)
            sija = sija + 1
        print("--------------------------")
    def kilpailu_ohi(self):
        for n in self.autot:
            if n.kuljettumatka > self.pituus:
                return 1

romuralli = Kilpailu("Suuri Romuralli", 8000)

tunnit = 1
loppu = 0
while loppu != 1:
    romuralli.tunti_kuluu()
    loppu = romuralli.kilpailu_ohi()
    if tunnit % 10 == 0:
        print("TUNTEJA KULUNUT", tunnit)
        romuralli.tulosta_tilanne()
    tunnit = tunnit + 1
print("LOPPUTULOKSET")
romuralli.tulosta_tilanne()