import torch
from yolov5 import train 

# Set parameters
data = r'C:\Users\jorda\Desktop\Stockasaurus-Rex\dataset\data.yaml'  # path to your data.yaml file
epochs = 100  # number of epochs to train
batch_size = 16  # batch size
img_size = 640  # image size
project = r'C:\Users\jorda\Desktop\Stockasaurus-Rex\runs\train'  # project directory
name = 'experiment'  # experiment name

# Train the model
train.run(data=data, epochs=epochs, batch_size=batch_size, imgsz=img_size, project=project, name=name)