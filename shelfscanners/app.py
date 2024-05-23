from flask import Flask, jsonify
import sqlite3
from flask_cors import CORS
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)


# create a trigger in database to calculate expiry date
def create_trigger():
    try:
        conn = sqlite3.connect("stock.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TRIGGER IF NOT EXISTS calculate_expiry_date
            AFTER INSERT ON STOCK
            FOR EACH ROW
            BEGIN
                UPDATE STOCK
                SET expiryDate = date(NEW.entryDate, '+' || NEW.freshDay || ' days')
                WHERE itemID = NEW.itemID;
            END;
        ''')
        conn.commit()
    except sqlite3.Error as err:
        print(f'Error creating trigger: {err}')
    finally:
        if conn:
            conn.close()


def get_db_connection():
    conn = sqlite3.connect('stock.db')
    conn.row_factory = sqlite3.Row
    return conn


# npm package "concurrently" has been installed, frontend and backend server will both run when npm start
@app.route('/api/fridge/<int:fridge_number>', methods=['GET'])
def get_fridge_items(fridge_number):
    print(f"Received request for fridge number: {fridge_number} (type: {type(fridge_number)})")
    conn = None
    try:
        conn = get_db_connection()
        items = conn.execute(
            'SELECT itemName, entryDate, expiryDate FROM STOCK WHERE fridgeNumber = ?', (fridge_number,)
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


def check_expiry_dates():
    try:
        conn = sqlite3.connect("stock.db")
        cursor = conn.cursor()
        # get the date of today and the date of 3 days later
        today = datetime.now().strftime('%Y-%m-%d')
        three_days_from_now = (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
        # check if there is any item that will expiry within 3 days
        cursor.execute("SELECT itemName, expiryDate FROM STOCK WHERE expiryDate BETWEEN ? AND ?", (today, three_days_from_now))
        notifications = cursor.fetchall()

        if notifications:
            cursor.execute("DELETE FROM notifications")
            for notification in notifications:
                cursor.execute("INSERT INTO notifications (itemName, expiryDate) VALUES (?, ?)", notification)
            conn.commit()
        print(f"Notifications to be returned: {notifications}")
        return notifications
    except sqlite3.Error as e:
        print(f'Error checking expiry dates: {e}')
        return []
    finally:
        if conn:
            conn.close()


@app.route('/api/Notifications', methods=['GET'])
def notifications():
    expiry_lists = check_expiry_dates()
    create_trigger()
    return jsonify(expiry_lists)


if __name__ == '__main__':
    app.run(debug=True)
