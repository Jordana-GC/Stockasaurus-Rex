import time

from datetime import datetime

#from signal import pause

from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder

from gpiozero import Button


picam = Picamera2()

button = Button(2)

config = picam.create_video_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
picam.configure(config)

encoder = H264Encoder(bitrate=10000000)

output = "/shared/project-innovate/Stockasaurus-Rex/videoScript/videos/test.h264"

def recordVideo():
    picam.start_preview(Preview.QTGL)
    picam.start_recording(encoder, output)
    
    time.sleep(10)
    
    picam.stop_recording()
    picam.stop_preview()

button.wait_for_press()
print("Recording started")
recordVideo()
