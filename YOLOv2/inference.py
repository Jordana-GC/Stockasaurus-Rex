import torch
from PIL import Image
import requests
from io import BytesIO

# Load the YOLOv5 model
model = torch.hub.load(r'C:\Users\jorda\Desktop\Stockasaurus-Rex\YOLOv2\yolov5', 'custom', path=r'C:\Users\jorda\Desktop\Stockasaurus-Rex\YOLOv2\yolov5\runs\train\exp3\weights\best.pt', source='local')


# Load an image from URL
img_url = r"https://upload.wikimedia.org/wikipedia/commons/0/03/Broccoli_and_cross_section_edit.jpg"
response = requests.get(img_url)
img = Image.open(BytesIO(response.content))

# Perform inference
results = model(img)

# Print and show results
results.print()  # Print results to console
results.show()   # Display results

# Save the results
results.save(save_dir='path/to/save/results')