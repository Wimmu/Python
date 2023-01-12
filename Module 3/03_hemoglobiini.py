skp = input("Sukupuoli:")
hem = int(input("Hemoglobiini:"))

if skp == "Nainen":
    if 117 <= hem <= 175:
        print("Hemoglobiinisi on normaali.")
    elif hem < 117:
        print("Hemoglobiinisi on alhainen.")
    elif hem > 175:
        print("Hemoglobiinisi on korkea.")
else:
    if 134 <= hem <= 195:
        print("Hemoglobiinisi on normaali.")
    elif hem < 134:
        print("Hemoglobiinisi on alhainen.")
    elif hem > 195:
        print("Hemoglobiinisi on korkea.")
