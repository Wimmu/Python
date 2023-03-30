from flask import Flask, request

app = Flask(__name__)
@app.route('/summa')
def summa():
    args = request.args
    luku1 = float(args.get("luku1"))
    luku2 = float(args.get("luku2"))
    summa = luku1+luku2
    "return str(summa)"

    vastaus = {
        "luku1" : luku1,
        "luku2" : luku2,
        "lopputulos": summa
    }

    return vastaus

# SELAIMEEN: http://127.0.0.1:3000/summa?luku1=13&luku2=28

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)