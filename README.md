# YouTube Video Transcription

## Description

This Python script downloads the audio from a YouTube video, transcribes the audio using OpenAI Whisper, and generates an audio file with the transcribed text using TTS.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Installation

To install the required dependencies, run the following commands:

```bash
pip install -q TTS
pip install numpy
pip install -q gradio
pip install -U numpy==1.21.6
pip install gTTS
pip install pytube
pip install git+https://github.com/openai/whisper.git -q
```

##Usage

Replace <youtube video link> in the transcribe_youtube_video.py script with the actual YouTube video link you want to transcribe.
Run the script:

The script will download the YouTube video's audio, 
transcribe it using the Whisper library, and generate 
an audio file with the transcribed textusing TTS.
The output will be saved as output.wav.

##License
This code is released under the MIT License.
You are free to use, modify, and distribute the code as long as you include the original license and attribution to the author. See the LICENSE file for more details.

##Contributing
If you'd like to contribute to this project,
please fork the repository and submit a pull request.

##Contact
If you have any questions or comments about this project,
please feel free to contact me at azharayyash999@gmail.com

Thank you for visiting!
