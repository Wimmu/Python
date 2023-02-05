import mysql.connector

def haekenttä(koodi):
    sql = "select name, municipality from airport where ident = '" + koodi +"'"
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

koodi = input("Anna lentokentän ICAO-koodi:")
haelentokenttä_tuple = haekenttä(koodi)
for rivi in haelentokenttä_tuple:
    print(rivi[0], "sijaitsee kunnassa", rivi[1])

