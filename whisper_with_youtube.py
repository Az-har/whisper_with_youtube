#import
!pip install pytube
!pip install git+https://github.com/openai/whisper.git -q


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
model = whisper.load_model('medium')
text = model.transcribe('audio')
#printing the transcribe
text['text']
