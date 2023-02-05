import mysql.connector

def ankkalinnalaiset(sukunimi):
    sql = "select etunimi, sukunimi from ankkalinnalainen where sukunimi = '" + sukunimi +"'"
    print(sql) #printtaa sql lausekkeen
    kursori = yhteys.cursor()
    kursori.execute(sql) #Lähtee tietokantapalvelimelle
    tulos = kursori.fetchall() #Haetaan monta arvoa (olemassa myös vain yksi haku)
    return tulos


yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='ankkalinna',
         user='root',
         password='assiponi',
         autocommit=True
         )

ankkalinnalaiset_tuple = ankkalinnalaiset("Ankka")
print(ankkalinnalaiset_tuple)
for rivi in ankkalinnalaiset_tuple:
    print("Päivää! Olen", rivi[0], rivi[1])