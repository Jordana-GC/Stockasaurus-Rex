from roboflow import Roboflow


rf = Roboflow(api_key="Rw8HnFE67kKd916j4yqM")
project = rf.workspace("stockasaurus-rex-dataset").project("shelf-scanners")
model = project.version(3).model
version = project.version(3)
dataset = version.download("yolov5")

version = project.version(3)
version.deploy("yolov5", r"C:\Users\jorda\Desktop\Stockasaurus-Rex\runs\train\exp2", r"C:\Users\jorda\Desktop\Stockasaurus-Rex\runs\train\exp2\weights\best.pt")


