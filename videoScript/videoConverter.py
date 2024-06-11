import subprocess

def videoConvert(inputVideo:str, outputVideo:str):
    try:
        command = [
            'ffmpeg',
            '-i', inputVideo,
            '-c:v', 'copy',
            '-c:a', 'copy',
            outputVideo
        ]
        
        subprocess.run(command, check=True)
        print(f"{inputVideo} converted to {outputVideo}")
        
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        
inputVideo = "/shared/projectInnovate/Stockasaurus-Rex/videoScript/videos/test.h264"
outputVideo = "/shared/projectInnovate/Stockasaurus-Rex/videoScript/videos/test.mp4"
videoConvert(inputVideo, outputVideo)
