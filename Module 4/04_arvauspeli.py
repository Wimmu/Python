import random

numero = random.randint(1, 10)
arvaus = float(input("Arvaa luku:"))

while arvaus != numero:
    if arvaus > numero:
        print("Liian suuri arvaus.")
        arvaus = float(input("Arvaa luku:"))
    elif arvaus < numero:
        print("Liian pieni arvaus.")
        arvaus = float(input("Arvaa luku:"))
print("Arvasit oikein! :)")
