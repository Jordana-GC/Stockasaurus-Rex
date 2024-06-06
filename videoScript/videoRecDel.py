from gpiozero import Button

from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder

import time
import os

# button is connected to gpio 2
button = Button(2)

picam = Picamera2()

encoder = H264Encoder(bitrate=10000000)

# configure the camera/video settings
videoConfig = picam.create_video_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
picam.configure(videoConfig)

# hope this makes the name increment if needed...
def nameIncr(directory:str, prefix:str, extension:str):
    index = 1
    while True:
        filename = f"{directory}/{prefix}{index:03d}.{extension}"
        if not os.path.exists(filename):
            return filename, index
        index += 1

# function to delete the latest video
def delVideo(directory:str, prefix:str, extension:str):
    index = 1
    latestVideo = None
    while True:
        filename = f"{directory}/{prefix}{index:03d}.{extension}"
        if not os.path.exists(filename):
            break
        latestVideo = filename
        index += 1
    if latestVideo:
        os.remove(latestVideo)
        print(f"{latestVideo} has been deleted")

# function to record video
def recordVideo():
#    picam.start()
    
    videoName, index = nameIncr("/shared/testing/videos", "video", "h264")
    
    # what index you bozo...
    if index > 1:
        delVideo("/shared/testing/videos", "video", "h264")
    
    picam.start_preview(Preview.QTGL)
    picam.start_recording(encoder, videoName)
    
    time.sleep(10)
    
    picam.stop_recording()
    picam.stop_preview()
    
    picam.stop()
    
    print(f"Video saved to {videoName}")
    
# wait for button press
button.wait_for_press()
print("Recording started")
recordVideo()
    