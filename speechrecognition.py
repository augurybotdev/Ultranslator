import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
filename = "snoop_dogg_white_girl.wav"

r = sr.Recognizer()

def transcribe_single_audio(path):
    with sr.AudioFile(path) as source:
        audio_listened = r.record(source)    
        text = r.recognize_google(audio_listened)
        print(text)
    return text

def transcribe_audio(path):
    sound = AudioSegment.from_file(path)  
    chunks = split_on_silence(sound,    
        min_silence_len = 500,    
        silence_thresh = sound.dBFS-14,    
        keep_silence=500,
    )
    folder_name = "audio-chunks"
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    for i, audio_chunk in enumerate(chunks, start=1):        
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")    
        try:
            text = transcribe_single_audio(chunk_filename)
        except sr.UnknownValueError as e:
            print("Error:", str(e))
        else:
            text = f"{text.capitalize()}. "
            print(chunk_filename, ":", text)
            whole_text += text

    return whole_text