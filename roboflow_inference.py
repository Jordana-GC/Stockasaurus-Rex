import sqlite3
from roboflow import Roboflow
from collections import Counter
from datetime import datetime
#########################################################
rf = Roboflow(api_key="Rw8HnFE67kKd916j4yqM")
project = rf.workspace().project("shelf-scanners")
model = project.version("2").model
#########################################################


#Running inference through Roboflow
job_id, signed_url, expire_time = model.predict_video(
    r"/shared/projectInnovate/Stockasaurus-Rex/videoScript/videos/test.mp4",
    fps=5,
    prediction_type="batch-video",
)

results = model.poll_until_video_results(job_id)

def insert_detection(conn, most_common_class, count, actual_time):
    """Insert the detection information into the 'fridge_items' table of your database."""
    try:
        c = conn.cursor()
        # Assuming 'item_id' is auto-incremented and 'stock_date' is the timestamp of detection
        c.execute("INSERT INTO fridge_items (item_id, stock_date) VALUES (?, ?)",
                  (most_common_class, actual_time))
        conn.commit()
        print("Detection information inserted into the database successfully.")
    except sqlite3.Error as e:
        print(e)

#Turning the information from roboflow into readable output with timestamp
def printMostFrequentDetection(results):
    predictions = [prediction for scanner in results['shelf-scanners'] for prediction in scanner['predictions']]
    classLabels = [prediction['class'] for prediction in predictions]
    
    if classLabels:
        counter = Counter(classLabels)
        most_common_class, count = counter.most_common(1)[0]

        for scanner in results['shelf-scanners']:
            if any(prediction['class'] == most_common_class for prediction in scanner ['predictions']):
                break

        
        actualTime = datetime.now().strftime(r"%d/%m/%Y %H:%M")

        print(f"The most common detection is: {most_common_class} with {count} detections with detection at time {actualTime}")

        conn = sqlite3.connect("mydatabase.db")
        insert_detection(conn, most_common_class, count, actualTime)  # Insert detection information into the database
        conn.close()
    else:
        print("No detections found")


printMostFrequentDetection(results)

