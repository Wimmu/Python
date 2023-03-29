from flask import Flask, request

app = Flask(__name__)
@app.route('/alkuluku')
def alkuluku():
    args = request.args
    luku1 = float(args.get("luku1"))
    kerratjaollinen = 0
    jaetaan = luku1
    while jaetaan != 0:
        if luku1 % jaetaan == 0:
            kerratjaollinen = kerratjaollinen + 1
            jaetaan = jaetaan - 1
        else:
            jaetaan = jaetaan - 1
    if kerratjaollinen == 2:
        vastaus = {
            "Luku": luku1,
            "Onko alkuluku:": "On alkuluku"
        }
    else:
        vastaus = {
            "Luku": luku1,
            "Onko alkuluku:": "Ei"
        }
    return vastaus

# SELAIMEEN: http://127.0.0.1:3000/alkuluku?luku1=4

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)