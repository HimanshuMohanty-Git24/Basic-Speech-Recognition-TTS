import streamlit as st
import whisper
import tempfile
import os
import pyaudio
import wave
import sys
import traceback

medium_model = whisper.load_model("medium")
base_model = whisper.load_model("base")

def transcribe_audio_file(audio_file, model):
    try:
        with st.spinner("Transcribing audio..."):
            result = model.transcribe(audio_file)
        return result["text"]
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return "Error occurred during transcription."

def record_audio():
    st.write("Recording audio...")
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 1
    fs = 44100
    seconds = 10
    p = pyaudio.PyAudio()
    print('Recording')
    stream = p.open(format=sample_format, channels=channels, rate=fs, frames_per_buffer=chunk, input=True)
    frames = []
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()
    st.write("Finished recording")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_wav_file:
        temp_wav_filename = temp_wav_file.name
        wf = wave.open(temp_wav_filename, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
        wf.close()
        return temp_wav_filename

def main():
    st.title("Speech Recognition App")
    option = st.selectbox("Choose an option", ("Upload Audio", "Record Audio"))
    if option == "Upload Audio":
        audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "flac"])
        if audio_file is not None:
            try:
                model = medium_model  # Use medium model for uploaded audio
                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_wav_file:
                    temp_wav_filename = temp_wav_file.name
                    with open(temp_wav_filename, "wb") as f:
                        f.write(audio_file.getvalue())
                    transcript = transcribe_audio_file(temp_wav_filename, model)
                    st.write("Transcript:")
                    st.write(transcript)
                    os.unlink(temp_wav_filename)
            except Exception as e:
                print(f"Error: {e}", file=sys.stderr)
                traceback.print_exc(file=sys.stderr)
    elif option == "Record Audio":
        try:
            model = base_model  # Use base model for recorded audio
            temp_wav_filename = record_audio()
            transcript = transcribe_audio_file(temp_wav_filename, model)
            st.write("Transcript:")
            st.write(transcript)
            os.unlink(temp_wav_filename)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)

if __name__ == "__main__":
    main()
