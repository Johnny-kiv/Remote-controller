import os

os.system("./audio.py")
os.system("./video.py")
os.system("ffmpeg -i output.avi -i file.wav -c:v copy -c:a aac output.mp4 -y")