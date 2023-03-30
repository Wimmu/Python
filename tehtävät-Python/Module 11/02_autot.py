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

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankinkoko):
        self.bensatankinkoko = bensatankinkoko
        super().__init__(rekisteritunnus, huippunopeus)

tesla = Sähköauto("ABC-15", 180, 52.5)
bemari = Polttomoottoriauto("ACD-123", 165, 32.3)

tesla.kiihdyntä(100)
bemari.kiihdyntä(69)
tesla.kulje(3)
bemari.kulje(3)

print(tesla.kuljettumatka)
print(bemari.kuljettumatka)