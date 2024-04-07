# Basic Speech Recognition and Text-to-Speech (TTS) App 🗣️📝

This repository contains a simple Python application for speech recognition and text-to-speech (TTS) using Streamlit and the Whisper library.

## Overview ℹ️

The application provides two main functionalities:
1. **Speech Recognition:** It allows users to upload an audio file or record audio directly through the app and transcribe the speech into text.
2. **Text-to-Speech:** It utilizes the OpenAI-Whisper library to generate synthetic speech from text.

## Requirements 🛠️

- Python 3.x
- Streamlit
- OpenAi-Whisper
- PyAudio
- Wave

## Usage 🚀

1. Clone the repository:
    ```bash
    git clone https://github.com/HimanshuMohanty-Git24/Basic-Speech-Recognition-TTS.git
    cd Basic-Speech-Recognition-TTS
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    streamlit run app.py
    ```

4. Choose an option:
   - **Upload Audio:** Upload an audio file in WAV, MP3, or FLAC format for speech recognition.
   - **Record Audio:** Record audio directly through the app using your device's microphone.

5. View the transcript or synthesized speech based on your selection.


## Note 📌

- The application uses two pre-trained models: a base model for recorded audio and a medium model for uploaded audio. These models are provided by the Whisper library.
- Ensure that you have a working microphone if you choose to record audio through the app.

For any issues or suggestions, please feel free to open an issue on GitHub.
