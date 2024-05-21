from flask import Flask, request, render_template
import sqlite3
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

# define the root route
@app.route('/')
def index():
    return render_template('main.html')

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

# dafine the route when submit the request to add one record
@app.route('/submit', methods=['POST'])
def submit():
    fridgeNumber = request.form['fridgeNumber']
    itemName = request.form['itemName']
    freshDay = int(request.form['freshDay'])
    entryDate = request.form['entryDate']

    try:
        conn = sqlite3.connect("stock.db")
        cursor = conn.cursor()
        sql = "INSERT INTO STOCK(fridgeNumber, itemName, freshDay, entryDate) VALUES (:fridgeNumber, :itemName, :freshDay, :entryDate)"
        bindParam = {'fridgeNumber': fridgeNumber, 'itemName': itemName, 'freshDay': freshDay, 'entryDate': entryDate}
        cursor.execute(sql, bindParam)
        conn.commit()

        return 'Data inserted successfully!'

    except sqlite3.Error as err:
        return f'Error: {err}'

    finally:
        if conn:
            conn.close()

create_trigger()

# define the route when fetch all records from database
@app.route('/fetch', methods=['GET'])
def fetch():
    try:
        conn = sqlite3.connect("stock.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM STOCK")
        fridge_data = cursor.fetchall()
        return render_template('fridge.html', fetched_data=fridge_data)
    except sqlite3.Error as e:
        return f"An error occurred: {e}"
    finally:
        if conn:
            conn.close()

# define the route and specify the ID to delete a record in the database
@app.route('/delete/<int:itemID>')
def delete_record(itemID):
    try:
        conn = sqlite3.connect("stock.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM STOCK WHERE itemID = :itemID", {'itemID': itemID})
        conn.commit()
        return 'Record deleted successfully!'
    except sqlite3.Error as e:
        return f'Error deleting record: {e}'
    finally:
        if conn:
            conn.close()

def check_expiry_dates():
    try:
        conn = sqlite3.connect("stock.db")
        cursor = conn.cursor()
        # 获取今天的日期和三天后的日期
        today = datetime.now().strftime('%Y-%m-%d')
        three_days_from_now = (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
        # 查询即将过期的产品
        cursor.execute("SELECT itemName, expiryDate FROM STOCK WHERE expiryDate BETWEEN ? AND ?", (today, three_days_from_now))
        notifications = cursor.fetchall()

        if notifications:
            cursor.execute("DELETE FROM notifications")
            for notification in notifications:
                cursor.execute("INSERT INTO notifications (itemName, expiryDate) VALUES (?, ?)", notification)
            conn.commit()
        return notifications
    except sqlite3.Error as e:
        print(f'Error checking expiry dates: {e}')
        return []
    finally:
        if conn:
            conn.close()

@app.route('/notifications', methods=['GET'])
def notifications():
    notifications = check_expiry_dates()
    return render_template('notifications.html', notifications=notifications)


if __name__ == '__main__':
    app.run(debug=True)
