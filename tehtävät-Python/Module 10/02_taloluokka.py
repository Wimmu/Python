class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.nykyinenkerros = alinkerros

    def siirry_kerrokseen(self, kerros):
        if kerros > self.ylinkerros:
            kerros = self.ylinkerros
        if kerros < self.alinkerros:
            kerros = self.alinkerros

        if kerros > self.nykyinenkerros:
            while self.nykyinenkerros != kerros:
                self.kerros_ylös()
        elif kerros < self.nykyinenkerros:
            while self.nykyinenkerros != kerros:
                self.kerros_alas()
        print("Hissi on kerroksessa:", self.nykyinenkerros)

    def kerros_ylös(self):
        self.nykyinenkerros = self.nykyinenkerros + 1
        print("Hissi menee ylös")

    def kerros_alas(self):
        self.nykyinenkerros = self.nykyinenkerros - 1
        print("Hissi menee alas")

class Talo:
    def __init__(self, alinkerros, ylinkerros, lukumäärä):
        self.hissit = []
        for i in range(lukumäärä):
            self.hissit.append(Hissi(alinkerros,ylinkerros))

    def aja_hissiä(self, nro, kerros):
        self.hissit[nro].siirry_kerrokseen(kerros)

talo = Talo(1, 10, 3)

talo.aja_hissiä(0, 3)

talo.aja_hissiä(2, 10)