class Koira:

    tehty = 0 # <- Kuinka monta koiraa on tehty

    # Konstruktori / Alustaja
    def __init__(self, nimi, syntymävuosi, haukahdus="Hau-Hau"): # <- Jos haukahdusta ei ole määritelty niin se on tämä
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus
        Koira.tehty = Koira.tehty + 1

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.haukahdus)
        return

soni = Koira("Soni", 2014, "*Hanhiääniä*")
cara = Koira("Cara", 2017)

"""cara = Koira()
cara.nimi = "Cara"
cara.syntymävuosi = 2017"""

print(soni.nimi, "on syntynyt", soni.syntymävuosi)
soni.hauku(2)

print(cara.nimi, "on syntynyt", cara.syntymävuosi)
cara.hauku(4)