from flask import Flask, jsonify, render_template
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('SpecificFridge.js')


def get_db_connection():
    conn = sqlite3.connect('stock.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/api/fridge/<int:fridge_number>', methods=['GET'])
def get_fridge_items(fridge_number):
    print(f"Received request for fridge number: {fridge_number} (type: {type(fridge_number)})")
    conn = None
    try:
        conn = get_db_connection()
        items = conn.execute(
            'SELECT itemName, entryDate, expiryDate FROM STOCK WHERE fridgeNumber = ?',
            (fridge_number,)
        ).fetchall()
        items_list = [dict(item) for item in items]
        print(f"Query result: {items_list}")
        return jsonify(items_list)
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "An error occurred while fetching data"}), 500
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    app.run(debug=True)
