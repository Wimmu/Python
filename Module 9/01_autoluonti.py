class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettumatka = 0

mersu = Auto("ABC-123", 142)

print("Auton rekisteritunnus on :", mersu.rekisteritunnus)
print("Auton huippunopeus on    :", mersu.huippunopeus, "km/h.")
print("Auton nykyinen nopeus on :", mersu.nopeus, "km/h.")
print("Auton on ajanut          :", mersu.kuljettumatka, "km.")