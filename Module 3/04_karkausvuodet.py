vuosi = int(input("Syötä vuosi:"))

if vuosi % 100 == 0:
    if vuosi % 400 == 0:
        print("Vuosi on karkausvuosi")
    else:
        print("Vuosi ei ole karkausvuosi")
else:
    if vuosi % 4 == 0:
        print("Vuosi on karkausvuosi")
    else:
        print("Vuosi ei ole karkausvuosi")