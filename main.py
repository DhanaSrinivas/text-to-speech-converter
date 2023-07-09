# Importing the library
from gtts import gTTS
import os

# Providing the text
input_text = input("Enter your text\n")

# Setting the language to English
language = "en"

# Passing the text to gtts engine
voice = gTTS(text=input_text, lang=language, slow=False)

# Creating and saving the audio file
voice.save("demo.mp3")

# To play the audio on Mac
os.system("afplay demo.mp3")

# To play the audio on Windows, use the below line instead of the above
# os.system("start demo.mp3")

