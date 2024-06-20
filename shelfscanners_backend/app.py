from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS
from datetime import datetime, timedelta
import bcrypt

app = Flask(__name__)
CORS(app)


def get_db_connection():
    conn = sqlite3.connect('stockdb.db')
    conn.row_factory = sqlite3.Row
    return conn


def login_db_connection():
    conn = sqlite3.connect('logindb.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/api/fridge/<int:fridge_number>', methods=['GET'])
def get_fridge_items(fridge_number):
    print(f"Received request for fridge number: {fridge_number} (type: {type(fridge_number)})")
    conn = None
    try:
        conn = get_db_connection()
        query = 'SELECT itemName, entryDate, expiryDate FROM item_fridge WHERE fridgeNumber = :fridge_number'
        items = conn.execute(query, {'fridge_number': fridge_number}).fetchall()
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
        # refreshed_data = refresh_item_fridge()
        conn = sqlite3.connect("stockdb.db")
        cursor = conn.cursor()
        # Get the date of today and the date of 3 days later
        today = datetime.now().strftime('%d-%m-%Y')
        three_days_from_now = (datetime.now() + timedelta(days=3)).strftime('%d-%m-%Y')

        # Check if there is any item that is already expired or will expire within 3 days
        query = """
        SELECT itemID, itemName, fridgeNumber, expiryDate
        FROM item_fridge
        WHERE expiryDate <= :three_days_from_now AND hidden = 0
        """
        cursor.execute(query, {'three_days_from_now': three_days_from_now})
        notifications = cursor.fetchall()

        print(f"Number of notifications fetched: {len(notifications)}")
        print(f"Notifications fetched: {notifications}")

        return notifications
    except sqlite3.Error as e:
        print(f'Error checking expiry dates: {e}')
        return []
    finally:
        if conn:
            conn.close()


@app.route('/api/Notifications', methods=['GET'])
def notifications():
    try:
        expiry_lists = check_expiry_dates()
        return jsonify(expiry_lists), 200
    except Exception as e:
        print(f'Error retrieving notifications: {e}')
        return jsonify({"error": str(e)}), 500


@app.route('/api/Login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    conn = login_db_connection()
    query = 'SELECT * FROM users WHERE email = :email'
    user = conn.execute(query, {'email': email}).fetchone()
    conn.close()

    if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
        return jsonify({'success': True, 'message': 'Login is successful!'})
    else:
        return jsonify({'success': False, 'message': 'Incorrect email or password, please try again.'})


# New hide_notification route
@app.route('/api/HideNotification/<int:itemID>', methods=['POST'])
def mark_notification(itemID):
    try:
        conn = sqlite3.connect("stockdb.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE item_fridge SET hidden = 1 WHERE itemID = ?", (itemID,))
        conn.commit()
        return jsonify({"message": "Notification hidden successfully"}), 200
    except sqlite3.Error as e:
        print(f'Error hiding notification: {e}')
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    app.run(host='100.74.58.66', port=5000)