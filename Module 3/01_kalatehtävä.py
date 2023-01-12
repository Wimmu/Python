kala = float(input("Kuhan pituus senttimetreinä:"))
pituus = 37-kala

if kala>=37:
    print("Kuha on tarpeeksi pitkä")
else:
    print("Kuha on liian pieni, palauta se järveen.")
    print("Kuhan pitäisi olla", pituus, "cm pidempi.")