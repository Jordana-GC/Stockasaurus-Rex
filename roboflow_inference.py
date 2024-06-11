import sqlite3
from roboflow import Roboflow
import os
from collections import Counter
from datetime import datetime, timedelta
#########################################################
rf = Roboflow(api_key="Rw8HnFE67kKd916j4yqM")
project = rf.workspace().project("shelf-scanners")
model = project.version("2").model
#########################################################


#Running inference through Roboflow
job_id, signed_url, expire_time = model.predict_video(
    r"C:\Users\jorda\Desktop\training\banana.training.mp4",
    fps=5,
    prediction_type="batch-video",
)

results = model.poll_until_video_results(job_id)

# Get the path to the database file in the 'shelf-scanners' folder
db_path = os.path.join(os.path.dirname(__file__), 'stockdb.db')


def get_item_freshness(conn, item_name):
    """Get the freshness duration (in days) for the detected item from the 'item' table."""
    try:
        c = conn.cursor()
        c.execute("SELECT freshDay FROM item WHERE itemName = ?", (item_name,))
        result = c.fetchone()
        return result[0] if result else None
    except sqlite3.Error as e:
        print(e)
        return None

def insert_detection(conn, most_common_class, count, actual_time):
    """Insert the detection information into the 'item_fridge' table of your database."""
    try:
        c = conn.cursor()
        
        # Get the freshness duration for the detected item
        freshness_days = get_item_freshness(conn, most_common_class)
        if freshness_days is None:
            print(f"Item '{most_common_class}' not found in 'item' table.")
            return
        
        # Calculate entryDate and expiryDate
        entry_date = datetime.strptime(actual_time, r"%d/%m/%Y %H:%M")
        expiry_date = entry_date + timedelta(days=freshness_days)
        
        # Insert the detected item into the 'item_fridge' table
        c.execute("""
            INSERT INTO item_fridge (fridgeNumber, itemName, freshDay, entryDate, expiryDate, hidden)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (1, most_common_class, freshness_days, entry_date.strftime(r"%d-%m-%Y"), expiry_date.strftime(r"%d-%m-%Y"), 0))
        
        conn.commit()
        print("Detection information inserted into the database successfully.")
    except sqlite3.Error as e:
        print(e)

# Process and insert the most frequent detection
def printMostFrequentDetection(results):
    predictions = [prediction for scanner in results['shelf-scanners'] for prediction in scanner['predictions']]
    class_labels = [prediction['class'] for prediction in predictions]
    
    if class_labels:
        counter = Counter(class_labels)
        most_common_class, count = counter.most_common(1)[0]

        actual_time = datetime.now().strftime(r"%d/%m/%Y %H:%M")

        print(f"The most common detection is: {most_common_class} with {count} detections at time {actual_time}")

        # Connect to the database using the relative path
        conn = sqlite3.connect(db_path)
        insert_detection(conn, most_common_class, count, actual_time)  # Insert detection information into the database
        conn.close()
    else:
        print("No detections found")

printMostFrequentDetection(results)

