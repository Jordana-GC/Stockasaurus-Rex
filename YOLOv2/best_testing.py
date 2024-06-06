#Script for running best weight through webcam
import torch
import cv2
import time
import numpy as np

# Load the YOLOv5 model
model = torch.hub.load(r'C:\Users\jorda\Desktop\Stockasaurus-Rex\YOLOv2\yolov5', 'custom', path=r'C:\Users\jorda\Desktop\Stockasaurus-Rex\YOLOv2\yolov5\runs\train\exp3\weights\best.pt', source='local')

# Set model parameters
model.conf = 0.6  # NMS confidence threshold
model.iou = 0.5  # NMS IoU threshold
model.agnostic = True  # NMS class-agnostic
model.multi_label = False  # NMS multiple labels per box
model.max_det = 10  # Maximum number of detections per image

# Initialize a list to store detected labels and their bounding boxes
detected_objects = []

# Time interval for re-detection (in seconds)
detection_interval = 7
last_detection_time = 0

def get_latest_label():
    """Function to retrieve the latest detected label."""
    if detected_objects:
        return detected_objects[-1][0]
    return None

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    current_time = time.time()

    # Perform detection and update detected_objects list if the interval has passed
    if current_time - last_detection_time >= detection_interval:
        last_detection_time = current_time  # Update the last detection time

        results = model(frame)

        # Parse results
        predictions = results.pred[0]
        boxes = predictions[:, :4].detach().cpu().numpy()
        scores = predictions[:, 4].detach().cpu().numpy()
        categories = predictions[:, 5].detach().cpu().numpy()

        # Keep track of the current detections to avoid duplicates
        current_detections = []

        for box, score, category in zip(boxes, scores, categories):
            x1, y1, x2, y2 = box.astype(int)
            label = model.names[int(category)]

            # Add the detected label and bounding box to the list if not already detected in this interval
            current_detections.append((label, (x1, y1, x2, y2), score))

        # Update the detected objects list with the new detections
        detected_objects.extend(current_detections)

        # Print the detected labels
        print("Detected Labels: ", [obj[0] for obj in detected_objects])
        print("Latest Detected Label: ", get_latest_label())

    # Perform real-time detection for drawing bounding boxes
    results = model(frame)

    # Parse results for drawing
    predictions = results.pred[0]
    boxes = predictions[:, :4].detach().cpu().numpy()
    scores = predictions[:, 4].detach().cpu().numpy()
    categories = predictions[:, 5].detach().cpu().numpy()

    # Draw bounding boxes and labels on the frame
    for box, score, category in zip(boxes, scores, categories):
        x1, y1, x2, y2 = box.astype(int)
        label = model.names[int(category)]
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"{label}: {score:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow('YOLOv5 Object Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
