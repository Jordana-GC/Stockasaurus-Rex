import cv2
import requests
import time

# Roboflow API settings
ROBOFLOW_URL = r'https://infer.roboflow.com/shelf-scanners/2?api_key=Rw8HnFE67kKd916j4yqM'


# Set up video capture (0 for default camera, or provide the stream URL)
cap = cv2.VideoCapture(0)  # Change this to your camera stream if needed

def get_inference(frame):
    _, img_encoded = cv2.imencode('.jpg', frame)
    response = requests.post(
        ROBOFLOW_URL,
        files={"file": img_encoded.tobytes()},
        headers={"Content-Type": "multipart/form-data"}
    )
    return response.json()

def main():
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        
        # Get inference results from Roboflow
        inference_result = get_inference(frame)
        
        print(inference_result)
        
        # Process and display the results
        if 'predictions' in inference_result:
            for prediction in inference_result['predictions']:
                x, y, w, h = prediction['x'], prediction['y'], prediction['width'], prediction['height']
                label = prediction['class']
                confidence = prediction['confidence']

                # Draw bounding box and label
                start_point = (int(x - w / 2), int(y - h / 2))
                end_point = (int(x + w / 2), int(y + h / 2))
                color = (0, 255, 0)  # Green color for bounding box
                thickness = 2
                frame = cv2.rectangle(frame, start_point, end_point, color, thickness)
                frame = cv2.putText(frame, f"{label} {confidence:.2f}", (int(x - w / 2), int(y - h / 2) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, thickness)

        # Display the resulting frame
        cv2.imshow('Roboflow Inference', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()