import mysql.connector

def haekentät(country):
    sql = "select type, name from airport where iso_country = '" + country +"'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='root',
         password='assiponi',
         autocommit=True
         )

helikopterikentät = 0
isotlentokentät = 0
keskilentokentät = 0
pienetlentokentät = 0
suljetut = 0

country = input("Anna maatunnus:")
haekentät_tuple = haekentät(country)
for rivi in haekentät_tuple:
    if rivi[0] == "heliport":
        helikopterikentät = helikopterikentät + 1
    if rivi[0] == "small_airport":
        pienetlentokentät = pienetlentokentät + 1
    if rivi[0] == "medium_airport":
        keskilentokentät = keskilentokentät + 1
    if rivi[0] == "large_airport":
        isotlentokentät = isotlentokentät + 1
    else:
        suljetut = suljetut + 1

print("Suuret lentokentät:", isotlentokentät)
print("Keskisuuret lentokentät:", keskilentokentät)
print("Pienet lentokentät:", pienetlentokentät)
print("Helikopterikentät:", helikopterikentät)
print("Suljetut kentät:", suljetut)