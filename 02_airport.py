import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/icao', methods=['GET'])
def icao():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            database='lp',
            user='root',
            password=''
        )

        connection.autocommit = True

        icao_koodi = request.args.get('icao')

        if not icao_koodi:
            return jsonify({"error": "ICAO code is required"}), 400

        koodi_tietokannassa = "SELECT name, municipality FROM airport WHERE ident=%s"
        cursor = connection.cursor()
        cursor.execute(koodi_tietokannassa, (icao_koodi,))

        results = cursor.fetchone()

        if results:
            return jsonify({"ICAO": icao_koodi, "Name": results[0], "Location": results[1]})
        else:
            return jsonify({"error": "Invalid ICAO code"}), 404

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

    finally:
        if connection:
            connection.close()


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
