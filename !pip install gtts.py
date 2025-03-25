!pip install gtts

from gtts import gTTS
from IPython.display import Audio, display

def text_to_speech(text):
    tts = gTTS(text, lang='en')
    tts.save('output.mp3')
    
    audio = Audio('output.mp3', autoplay=True)
    display(audio)

# Example usage
text = (input("enter text"))
text_to_speech(text)
