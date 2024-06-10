#import time

from datetime import datetime

#from signal import pause

from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder

from gpiozero import Button


picam = Picamera2()

button = Button(2)

#config = picam.create_video_configuration(main={"size": (640, 480)}, , lores={"size": (640, 480)}, display="lores")
#picam.configure(config)

picam.video_configuration.enable_lores()
picam.video_configuration.lores.size = (640, 480)
picam.video_configuration.main.size = (640, 480)
picam.video_configuration.controls.FrameRate = 60.0
picam.configure("video")

encoder = H264Encoder(bitrate=25000000)

output = "/shared/projectInnovate/Stockasaurus-Rex/videoScript/videos/test.h264"

def recordVideo():
    picam.start_preview(Preview.QTGL)
    picam.start_recording(encoder, output)
    
#    time.sleep(10)
    print("Press the button again to end the recording")
    button.wait_for_press()
    print("Recording ended")
    picam.stop_recording()
    picam.stop_preview()

while True:    
    print("Press to start the recording")
    button.wait_for_press()
    print("Recording started")
    recordVideo()
