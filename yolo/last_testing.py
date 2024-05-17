import yolov5

# load pretrained model
model = yolov5.load(r"C:\Users\jorda\Desktop\Stockasaurus-Rex\yolo\runs\train\yolov5_training2\weights\last.pt")

# set model parameters
model.conf = 0.25  # NMS confidence threshold
model.iou = 0.45  # NMS IoU threshold
model.agnostic = False  # NMS class-agnostic
model.multi_label = False  # NMS multiple labels per box
model.max_det = 100  # maximum number of detections per image

# set image
img = r"https://www.shutterstock.com/image-photo/smiling-face-depicted-two-mandarin-600nw-1806465613.jpg"

# perform inference
results = model(img)

# inference with larger input size
results = model(img, size=1280)

# inference with test time augmentation
results = model(img, augment=True)

# parse results
predictions = results.pred[0]
boxes = predictions[:, :4] # x1, y1, x2, y2
scores = predictions[:, 4]
categories = predictions[:, 5]

# show detection bounding boxes on image
results.show()

# save results into "results/" folder
results.save(save_dir='results/')
