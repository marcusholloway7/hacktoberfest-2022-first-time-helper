from gtts import gTTS
import os
text = "Hello! My name is Bharath."
tts = gTTS(text)
tts.save("hi.mp3")
os.system("hi.mp3")