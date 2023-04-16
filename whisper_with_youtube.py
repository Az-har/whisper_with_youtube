#import
!pip install -q TTS
!pip install numpy
!pip install -q gradio
!pip install -U numpy==1.21.6
!pip install gTTS
!pip install pytube
!pip install git+https://github.com/openai/whisper.git -q

#import gradio
import gradio as gr
#import gtts
from gtts import gTTS
#import os
import os
#import TTS
from TTS.api import TTS

#selecting the voice model
tts_en_slow_fm = TTS('tts_models/en/ljspeech/tacotron2-DDC')
#Importing Pytube library
import pytube
#Importing Whisper library
import whisper

# Reading the above Taken movie Youtube link
video = <youtube video link>
data = pytube.YouTube(video)
# Converting and downloading as 'MP4' file
#saving the audio file as "audio.mp4" for future use
audio = data.streams.get_audio_only()
audio.download(filename="audio.mp4")

#choosing model refer to whisper page for more info
model = whisper.load_model(“large”)
text = model1.transcribe(“audio”)
#printing the transcribe
text['text']
#selecting the audio as input
tts_en_slow_fm.tts_to_file(text=text['text'], file_path="output.wav")
from IPython.display import Audio, display
#if run on google colab the below line wont work if the file size is large
display(Audio('outpu.wav', autoplay=True))