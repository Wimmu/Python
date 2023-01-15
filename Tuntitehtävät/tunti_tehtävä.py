"""
        # LATTEN OSTAMINEN

raha = float(input("Paljonko siulla on rahaa?"))

if raha>=5:
    print("Saat ostettua Laten")
else:
    print("Sinulla ei ole tarpeeksi rahaa")

""""""
        # PITUUS OHJELMA (HUONOMPI)

pituus = int(input("Kuinka pitkä olet?"))

if 165<= pituus <185:
    print("Olet keskimittainen")
if pituus <165:
    print("Olet lyhyt")
if pituus >184:
    print("Olet pitkä")
    
"""
        # PITUUS OHJELMA AND

pituus = int(input("Kuinka pitkä olet?"))

if pituus >= 165 and pituus < 185:
    print("Olet keskimittainen")
elif pituus <165:
    print("Olet lyhyt")
else:
    print("Olet pitkä")

"""
        # PITUUS OHJELMA OR

pituus = int(input("Kuinka pitkä olet?"))

if pituus < 165 or pituus >= 185:
    print("Et ole keskimittainen")
    
"""



