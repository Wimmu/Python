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

mersu = Auto("ABC-123", 142)

mersu.kiihdyntä(30)
mersu.kiihdyntä(70)
mersu.kiihdyntä(50)

print("Auton nykyinen nopeus on:", mersu.nopeus, "km/h.")

mersu.kiihdyntä(-200)

print("Auton nykyinen nopeus on:", mersu.nopeus, "km/h.")