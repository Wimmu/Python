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

a = Hissi(1, 10)

a.siirry_kerrokseen(5)
a.siirry_kerrokseen(1)