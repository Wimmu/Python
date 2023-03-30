from flask import Flask, request
import mysql.connector

app = Flask(__name__)

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='root',
         password='assiponi',
         autocommit=True
         )
@app.route('/haekentta')
def alkuluku():
    args = request.args
    koodi = str(args.get("koodi"))

    sql = "select name, municipality from airport where ident = '" + koodi + "'"
    # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    vastaus = {
        "luku1": tulos
    }

    return vastaus

# SELAIMEEN: http://127.0.0.1:3000/alkuluku?luku1=4

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)