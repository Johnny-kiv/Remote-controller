import cv2
import pyaudio # Soundcard audio I/O access library
import wave # Python 3 module for reading / writing simple .wav files
cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
# Setup channel info
FORMAT = pyaudio.paInt16 # data type formate
CHANNELS = 2 # Adjust to your number of channels
RATE = 44100 # Sample Rate
CHUNK = 1024 # Block Size
WAVE_OUTPUT_FILENAME = "urok.wav"

# Startup pyaudio instance
audio = pyaudio.PyAudio()

# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print ("recording...")
frames = []

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        data = stream.read(CHUNK)
        frames.append(data)
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord(' '):
            break
    else:
        break
print ("finished recording")
cap.release()

out.release()

cv2.destroyAllWindows()
stream.stop_stream()
stream.close()
audio.terminate()

# Write your new .wav file with built in Python 3 Wave module
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()