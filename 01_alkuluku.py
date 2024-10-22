import math
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/prime', methods=['GET'])
def prime():
    args = request.args

    alkuluku = int(args.get("Number", 31))
    on_alkuluku = True

    if alkuluku < 2:
        on_alkuluku = False

    for i in range(2, int(math.sqrt(alkuluku)) + 1):
        if alkuluku % i == 0:
            on_alkuluku = False


    if on_alkuluku:
        return jsonify({"Number": alkuluku, "isPrime": True})
    else:
        return jsonify({"Number": alkuluku, "isPrime": False})

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
