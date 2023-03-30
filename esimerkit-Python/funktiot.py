"""

def tervehdi():
    print("Moi!")
    return

def tervehdys(sana, kerrat):
    for i in range (kerrat):
        print(sana, str(i+1), "kerran")

sana = input("Anna tervehdys:")
määrä = int(input("Montako kertaa tervehditään?"))

tervehdys(sana, määrä)
tervehdi()

"""
def suurempi(luku1, luku2):
    if luku1 > luku2:
        return luku1
    else:
        return luku2
l1 = 20
l2 = 40
suurempi = suurempi(l1, l2)
print(suurempi)
