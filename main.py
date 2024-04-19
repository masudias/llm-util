import os
import ffmpeg
import subprocess
import speech_recognition as sr

def extract_audio(video_file, audio_file):
    try:
        ffmpeg.input(video_file).output(audio_file, format='wav').run(overwrite_output=True)
    except ffmpeg.Error as e:
        print('stdout:', e.stdout.decode('utf8'))
        print('stderr:', e.stderr.decode('utf8'))
        raise

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        try:
            # Use the recognize_google method of the Recognizer class to transcribe audio
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError as e:
            return "Error with Google Speech Recognition service: {0}".format(e)

def main():
    video_file = "input_video.mp4"
    audio_file = "output_audio.wav"

    extract_audio(video_file, audio_file)
    text = transcribe_audio(audio_file)

    print("Transcribed Text:")
    print(text)

if __name__ == "__main__":
    main()
