from roboflow import Roboflow


rf = Roboflow(api_key="Rw8HnFE67kKd916j4yqM")
project = rf.workspace("stockasaurus-rex-dataset").project("shelf-scanners")
model = project.version(2).model
version = project.version(2)
dataset = version.download("yolov5")

version = project.version(2)
version.deploy("yolov5", r"C:\Users\jorda\Desktop\Stockasaurus-Rex\runs\train\exp", r"C:\Users\jorda\Desktop\Stockasaurus-Rex\runs\train\exp\weights\best.pt")


